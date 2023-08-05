from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages
# from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from communication.models import RecentActivityModel
from student.models import StudentsModel
from school_setting.models import SchoolGeneralInfoModel, SchoolAcademicInfoModel
from attendance.models import StudentClassAttendanceRecordModel
from academic.models import ClassSectionInfoModel
from finance.models import FeeModel


def setup_test():
    info = SchoolGeneralInfoModel.objects.first()
    if info:
        return True
    return False


class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_dashboard/dashboard.html'

    def dispatch(self, *args, **kwargs):
        if setup_test():
            return super(AdminDashboardView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('maintenance_view'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        type = self.request.user.profile.type
        info = SchoolGeneralInfoModel.objects.first()
        if info.school_type == 'mix' and info.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=type).first()
            context['active_students'] = StudentsModel.objects.filter(status='active', type=type).count()
        else:
            context['active_students'] = StudentsModel.objects.filter(status='active').count()
            academic_info = SchoolAcademicInfoModel.objects.first()
        session = academic_info.session
        term = academic_info.term

        if info.school_type == 'mix' and info.separate_school_section:
            context['notification_list'] = RecentActivityModel.objects.filter(session=session, term=term,
                                           type=type).order_by('id').reverse()[:15]
            context['attendance_record_list'] = StudentClassAttendanceRecordModel.objects.filter(session=session,
                                          term=term, type=type).order_by('id')[:7]
            context['student_class_list'] = ClassSectionInfoModel.objects.filter(type=type)
            context['fee_list'] = FeeModel.objects.filter(type=type)
        else:
            context['notification_list'] = RecentActivityModel.objects.filter(session=session, term=term).order_by(
                'id').reverse()[:15]
            context['attendance_record_list'] = StudentClassAttendanceRecordModel.objects.filter(session=session,
                                                term=term).order_by('id')[:7]
            context['student_class_list'] = ClassSectionInfoModel.objects.all()
            context['fee_list'] = FeeModel.objects.all()
        return context


class AdminMaintenanceView(TemplateView):
    template_name = 'admin_dashboard/maintenance.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


