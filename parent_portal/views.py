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


class ParentDashboardView(TemplateView):
    template_name = 'parent_portal/dashboard.html'

    def dispatch(self, *args, **kwargs):
        if setup_test():
            return super(ParentDashboardView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('maintenance_view'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

