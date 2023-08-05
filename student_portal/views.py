from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.http import HttpResponse
from num2words import num2words
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from school_setting.models import SchoolGeneralInfoModel, SchoolAcademicInfoModel
from finance.models import FeeMasterModel, OnlinePaymentModel
from school_setting.models import SchoolGeneralInfoModel
from ebooklib import epub
import ebooklib
from finance.utility import *
from student.models import StudentsModel
from library.models import BookModel, PDFBookModel, BookBorrowModel, BookCopyModel, EBookModel
from student_portal.view.result_view import *


def setup_test():
    if 1:
        return True
    return False


class StudentDashboardView(TemplateView):
    template_name = 'student_portal/dashboard.html'

    def dispatch(self, *args, **kwargs):
        if setup_test():
            return super(StudentDashboardView, self).dispatch(*args, **kwargs)
        else:
            pass
            # return redirect(reverse('site_info_create'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StudentFeeView(SuccessMessageMixin, TemplateView):
    template_name = 'student_portal/fee/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        student = self.request.user.profile.student
        if school_setting.separate_school_section:
            academic_setting = SchoolAcademicInfoModel.objects.filter(type=student.type).first()
            termly_fee_list = FeeMasterModel.objects.filter(type=student.type,
                                                            fee__fee_occurrence='termly')
            one_time_fee_list = FeeMasterModel.objects.filter(type=student.type).exclude(
                fee__fee_occurrence='termly')
            payment_method = OnlinePaymentModel.objects.filter(type=student.type, status='active')

        else:
            academic_setting = SchoolAcademicInfoModel.objects.first()
            termly_fee_list = FeeMasterModel.objects.filter(fee__fee_occurrence='termly')
            one_time_fee_list = FeeMasterModel.objects.exclude(fee__fee_occurrence='termly')
            payment_method = OnlinePaymentModel.objects.filter(status='active')

        context['academic_setting'] = academic_setting
        context['student'] = student
        context['termly_fee_list'] = termly_fee_list
        context['one_time_fee_list'] = one_time_fee_list
        context['payment_method_list'] = payment_method

        return context


def select_fee_method(request):
    if request.method == 'POST':
        student = StudentsModel.objects.get(pk=request.POST.get('student'))
        fee = FeeMasterModel.objects.get(pk=request.POST.get('fee'))
        session = request.POST.get('session')
        term = request.POST.get('term')
        amount = request.POST.get('amount')
        amount_in_word = num2words(amount)
        method = request.POST.get('payment_method')

        return select_payment_method(request, student, fee, amount, amount_in_word, method, session, term)

    return redirect(reverse('student_fee'))


class StudentBookListView(LoginRequiredMixin, ListView):
    model = BookModel
    permission_required = 'finance.view_feemodel'
    fields = '__all__'
    template_name = 'student_portal/library/book/index.html'
    context_object_name = "book_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return BookModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return BookModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()

        return context


class StudentPDFListView(LoginRequiredMixin, ListView):
    model = PDFBookModel
    permission_required = 'finance.view_feemodel'
    fields = '__all__'
    template_name = 'student_portal/library/pdf/index.html'
    context_object_name = "pdf_book_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return PDFBookModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return PDFBookModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class StudentPDFDetailView(LoginRequiredMixin, DetailView):
    model = PDFBookModel
    permission_required = 'finance.delete_feemodel'
    fields = '__all__'
    template_name = 'student_portal/library/pdf/detail.html'
    context_object_name = "pdf_book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StudentEBookListView(LoginRequiredMixin, ListView):
    model = EBookModel
    permission_required = 'finance.view_feemodel'
    fields = '__all__'
    template_name = 'student_portal/library/e_book/index.html'
    context_object_name = "e_book_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return EBookModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return EBookModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class StudentEBookDetailView(LoginRequiredMixin, DetailView):
    model = EBookModel
    permission_required = 'finance.delete_feemodel'
    fields = '__all__'
    template_name = 'student_portal/library/e_book/detail.html'
    context_object_name = "e_book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = epub.read_epub(self.object.e_file.path)
        content = ""

        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                item_content = item.get_content().decode('utf-8')
                content += item_content

        context['e_book_content'] = content
        return context


class StudentBorrowedBookListView(LoginRequiredMixin, TemplateView):
    permission_required = 'finance.change_feemodel'
    template_name = 'student_portal/library/book/borrowed_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = BookBorrowModel.objects.filter(student=self.request.user.profile.student)[:50]
        return context
