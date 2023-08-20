from django.shortcuts import render, redirect
from django.urls import reverse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import resolve
from django.core import serializers
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from admin_dashboard.utility import state_list
from school_setting.models import *
from django.apps import apps
from student.models import *
from student.forms import *
from finance.templatetags.fee_custom_filters import *


class ParentCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = ParentsModel
    permission_required = 'student.add_parentsmodel'
    form_class = ParentForm
    template_name = 'student/parent/create.html'
    success_message = 'Parent Registration Successful'

    def get_success_url(self):
        if 'student-registration' in self.request.path:
            return reverse('student_create', kwargs={'parent_pk': self.object.pk})
        return reverse('parent_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['parent_setting'] = StudentSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            context['parent_setting'] = StudentSettingModel.objects.filter().first()
        context['state_list'] = state_list
        return context


class ParentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ParentsModel
    permission_required = 'student.view_parentsmodel'
    fields = '__all__'
    template_name = 'student/parent/index.html'
    context_object_name = "parent_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return ParentsModel.objects.filter(type=self.request.user.profile.type).order_by('surname')
        else:
            return ParentsModel.objects.all().order_by('surname')


class ParentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = ParentsModel
    permission_required = 'student.view_parentsmodel'
    fields = '__all__'
    template_name = 'student/parent/detail.html'
    context_object_name = "parent"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent = self.object
        student_list = StudentsModel.objects.filter(parent=parent)
        context['student_list'] = student_list
        return context


class ParentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ParentsModel
    permission_required = 'student.change_parentsmodel'
    form_class = ParentEditForm
    template_name = 'student/parent/edit.html'
    success_message = 'Parent Information Successfully Updated'

    def get_success_url(self):
        return reverse('parent_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent'] = self.object
        context['state_list'] = state_list
        return context


class ParentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ParentsModel
    permission_required = 'student.delete_parentsmodel'
    fields = '__all__'
    template_name = 'student/parent/delete.html'
    success_message = 'Parent Successfully Deleted'
    context_object_name = "parent"

    def get_success_url(self):
        return reverse('parent_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentsModel
    permission_required = 'student.add_studentsmodel'
    form_class = StudentForm
    template_name = 'student/student/create.html'
    success_message = 'Student Successfully Registered'

    def get_success_url(self):
        return reverse('student_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, *args, **kwargs):
        return super(StudentCreateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(StudentCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        parent_pk = self.kwargs.get('parent_pk')
        student_parent = ParentsModel.objects.get(pk=parent_pk)
        context['student_parent'] = student_parent
        context['state_list'] = state_list
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['class_list'] = ClassesModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['hostel_list'] = HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['student_setting'] = StudentSettingModel.objects.filter(
                type=self.request.user.profile.type).first()
        else:
            context['hostel_list'] = HostelModel.objects.all().order_by('name')
            context['student_setting'] = StudentSettingModel.objects.filter().first()
            context['class_list'] = ClassesModel.objects.all().order_by('name')

        return context


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = StudentsModel
    permission_required = 'student.view_studentsmodel'
    fields = '__all__'
    template_name = 'student/student/index.html'
    context_object_name = "student_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return StudentsModel.objects.filter(type=self.request.user.profile.type).exclude(
                status='graduated').order_by('surname')
        else:
            return StudentsModel.objects.filter().exclude(status='graduated').order_by('surname')


class StudentAlumniListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = StudentsModel
    permission_required = 'student.view_studentsmodel'
    fields = '__all__'
    template_name = 'student/student/alumni.html'
    context_object_name = "student_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return StudentsModel.objects.filter(type=self.request.user.profile.type).filter(
                status='graduated').order_by('surname')
        else:
            return StudentsModel.objects.filter().filter(status='graduated').order_by('surname')


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = StudentsModel
    permission_required = 'student.view_studentsmodel'
    fields = '__all__'
    template_name = 'student/student/detail.html'
    context_object_name = "student"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ResultModel = apps.get_model('result', 'ResultModel')
        session_list = ResultModel.objects.filter(student=self.object)
        student_session_list = []
        for session_result in session_list:
            if session_result.session not in student_session_list:
                student_session_list.append(session_result.session)
        context['student_session_list'] = student_session_list
        student = self.object
        student_class = student.student_class
        class_section = student.class_section
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            academic_setting = SchoolAcademicInfoModel.objects.filter(type=self.request.user.profile.type).first()
            fee_setting = FinanceSettingModel.objects.filter(type=self.request.user.profile.type).first()
            if student_class and class_section:
                termly_fee_list = FeeMasterModel.objects.filter(type=self.request.user.profile.type,
                                                                fee__fee_occurrence='termly',
                                                                student_class__in=[student_class.id],
                                                                class_section__in=[class_section.id])

                one_time_fee_list = FeeMasterModel.objects.filter(type=self.request.user.profile.type,
                                                                  student_class__in=[student_class.id],
                                                                  class_section__in=[class_section.id]).exclude(
                    fee__fee_occurrence='termly')
            else:
                termly_fee_list = []
                one_time_fee_list = []
        else:
            academic_setting = SchoolAcademicInfoModel.objects.first()
            fee_setting = FinanceSettingModel.objects.first()
            if student_class and class_section:
                termly_fee_list = FeeMasterModel.objects.filter(fee__fee_occurrence='termly',
                                                                student_class__in=[student_class.id],
                                                                class_section__in=[class_section.id])
                one_time_fee_list = FeeMasterModel.objects.exclude(fee__fee_occurrence='termly',
                                                                   student_class__in=[student_class.id],
                                                                   class_section__in=[class_section.id])
            else:
                termly_fee_list = []
                one_time_fee_list = []
        current_payment_list = FeePaymentModel.objects.filter(student=student, session=academic_setting.session)
        all_payment_list = FeePaymentModel.objects.filter(student=student)
        outstanding_payment_list = OutstandingFeeModel.objects.filter(student=student, status='active')
        current_fee, fee_paid, fee_discount, fee_penalty, fee_balance, outstanding_fee = 0, 0, 0, 0, 0, 0
        for fee_master in termly_fee_list:
            if fee_master.same_termly_price:
                amount = fee_master.amount
            else:
                if academic_setting.term == '1st term':
                    amount = fee_master.first_term_amount
                elif academic_setting.term == '2nd term':
                    amount = fee_master.second_term_amount
                elif academic_setting.term == '3rd term':
                    amount = fee_master.third_term_amount
            current_fee += amount
            fee_paid += get_amount_paid(fee_master, student.id)
            fee_discount += get_fee_discount(fee_master, student.id)
            fee_penalty += get_fee_penalty(fee_master, student.id)
            fee_balance += get_fee_balance(fee_master, student.id)

        for fee_master in one_time_fee_list:
            if fee_master.fee.payment_term == 'any term':
                amount = fee_master.amount
            elif fee_master.fee.payment_term == academic_setting.term:
                amount = fee_master.amount
            else:
                amount = 0

            current_fee += amount
            fee_paid += get_amount_paid(fee_master, student.id)
            fee_discount += get_fee_discount(fee_master, student.id)
            fee_penalty += get_fee_penalty(fee_master, student.id)
            fee_balance += get_fee_balance(fee_master, student.id)

        for fee in outstanding_payment_list:
            if fee.balance:
                outstanding_fee += fee.balance

        ClassAttendanceModel = apps.get_model('attendance', 'StudentClassAttendanceModel')
        class_attendance = ClassAttendanceModel.objects.filter(student=student, session=academic_setting.session,
                                                               term=academic_setting.term).first()

        context['academic_setting'] = academic_setting
        context['fee_setting'] = fee_setting
        context['student'] = student
        context['termly_fee_list'] = termly_fee_list
        context['one_time_fee_list'] = one_time_fee_list
        context['current_payment_list'] = current_payment_list
        context['all_payment_list'] = all_payment_list
        context['outstanding_payment_list'] = outstanding_payment_list
        context['current_fee'] = current_fee
        context['fee_paid'] = fee_paid
        context['fee_discount'] = fee_discount
        context['fee_penalty'] = fee_penalty
        context['fee_balance'] = fee_balance
        context['outstanding_fee'] = outstanding_fee
        context['total_fee'] = outstanding_fee + fee_balance
        if current_fee:
            context['percentage_paid'] = round(((current_fee - fee_balance) / current_fee) * 100)
        else:
            context['percentage_paid'] = 0
        context['class_attendance'] = class_attendance
        return context


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = StudentsModel
    permission_required = 'student.change_studentsmodel'
    form_class = StudentForm
    template_name = 'student/student/edit.html'
    success_message = 'Student Information Successfully Updated'

    def get_success_url(self):
        return reverse('student_detail', kwargs={'pk': self.object.pk})

    def dispatch(self, *args, **kwargs):
        return super(StudentUpdateView, self).dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(StudentUpdateView, self).get_form_kwargs()
        # kwargs.update({'division': self.request.session['division']})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['student_parent'] = self.object.parent
        context['student'] = self.object
        context['state_list'] = state_list
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['hostel_list'] = HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['room_list'] = HostelRoomModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['bed_list'] = HostelBedModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['student_setting'] = StudentSettingModel.objects.filter(
                type=self.request.user.profile.type).first()
            context['class_list'] = ClassesModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            context['hostel_list'] = HostelModel.objects.all().order_by('name')
            context['room_list'] = HostelRoomModel.objects.all().order_by('name')
            context['bed_list'] = HostelBedModel.objects.all().order_by('name')
            context['student_setting'] = StudentSettingModel.objects.filter().first()
            context['class_list'] = ClassesModel.objects.all().order_by('name')
        return context


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = StudentsModel
    permission_required = 'student.delete_studentsmodel'
    fields = '__all__'
    template_name = 'student/student/delete.html'
    context_object_name = "student"
    success_message = 'Student Successfully Deleted'

    def get_success_url(self):
        return reverse('student_index')


@login_required
def student_check_parent_view(request):
    school_setting = SchoolGeneralInfoModel.objects.first()
    if school_setting.separate_school_section:
        parent_list = ParentsModel.objects.filter(type=request.user.profile.type)
    else:
        parent_list = ParentsModel.objects.filter()
    parent_list = serializers.serialize("json", parent_list)

    context = {
        'parent_list': parent_list,
    }
    return render(request, 'student/student/check_parent.html', context=context)


class StudentSettingView(LoginRequiredMixin, TemplateView):
    template_name = 'student/setting/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            student_info = StudentSettingModel.objects.filter(type=self.request.user.profile.type).first()
            form_kwargs['type'] = self.request.user.profile.type
        else:
            student_info = StudentSettingModel.objects.first()

        if not student_info:
            form = StudentSettingCreateForm(**form_kwargs)
            is_student_info = False
        else:
            form = StudentSettingEditForm(instance=student_info, **form_kwargs)
            is_student_info = True
        context['form'] = form
        context['is_student_info'] = is_student_info
        context['student_info'] = student_info
        return context


class StudentSettingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = StudentSettingModel
    form_class = StudentSettingCreateForm
    template_name = 'student/setting/index.html'
    success_message = 'Admission Settings updated Successfully'

    def get_success_url(self):
        return reverse('student_info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()

        return context

    def get_form_kwargs(self):
        kwargs = super(StudentSettingCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class StudentSettingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = StudentSettingModel
    form_class = StudentSettingEditForm
    template_name = 'student/setting/index.html'
    success_message = 'Admission Setting updated Successfully'

    def get_success_url(self):
        return reverse('student_info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_form_kwargs(self):
        kwargs = super(StudentSettingUpdateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs
