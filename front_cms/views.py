from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from school_setting.models import SchoolGeneralInfoModel, SchoolAcademicInfoModel
from front_cms.models import *
from front_cms.forms import *


def select_frontend_template_view(request):
    school_setting = SchoolGeneralInfoModel.objects.first()
    if school_setting.separate_school_section:
        frontend_setting = FrontEndSettingModel.objects.filter(type=request.user.profile.type).first()
    else:
        frontend_setting = FrontEndSettingModel.objects.first()

    if request.method == 'POST':
        template = request.POST.get('template', None)
        if frontend_setting:
            frontend_setting.template = template
            frontend_setting.save()

            if frontend_setting.template == template:
                messages.success(request, 'USER SITE TEMPLATE UPDATED SUCCESSFULLY')
        else:
            frontend_setting = FrontEndSettingModel.objects.create(template=template, status='active', user=request.user, type=request.user.profile.type)
            frontend_setting.save()
    context = {
        'frontend_setting': frontend_setting
    }
    return render(request, 'front_cms/select_template.html', context)


class HomePageView(LoginRequiredMixin, TemplateView):

    def dispatch(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()
        if frontend_setting:
            return super(HomePageView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('maintenance_view'))

    def get_template_names(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()

        template_variable = frontend_setting.template

        if template_variable == '1':
            return ['front_cms/template1/homepage.html']
        elif template_variable == '2':
            return ['front_cms/template2/homepage.html']
        else:
            return ['front_cms/template1/homepage.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_type = self.request.user.profile.type
        info = SchoolGeneralInfoModel.objects.first()
        if info.school_type == 'mix' and info.separate_school_section:
            slider_list = FrontSliderModel.objects.filter(type=user_type)[:3]
        else:
            slider_list = FrontSliderModel.objects.all()[:3]
        context['slider_list'] = slider_list
        return context


class AboutPageView(LoginRequiredMixin, TemplateView):

    def dispatch(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()
        if frontend_setting:
            return super(AboutPageView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('maintenance_view'))

    def get_template_names(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()

        template_variable = frontend_setting.template

        if template_variable == '1':
            return ['front_cms/template1/about.html']
        elif template_variable == '2':
            return ['front_cms/template2/about.html']
        else:
            return ['front_cms/template1/about.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_type = self.request.user.profile.type
        info = SchoolGeneralInfoModel.objects.first()
        if info.school_type == 'mix' and info.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=user_type).first()
        else:
            academic_info = SchoolAcademicInfoModel.objects.first()

        return context


class StaffPageView(LoginRequiredMixin, TemplateView):

    def dispatch(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()
        if frontend_setting:
            return super(StaffPageView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('maintenance_view'))

    def get_template_names(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()

        template_variable = frontend_setting.template

        if template_variable == '1':
            return ['front_cms/template1/staff.html']
        elif template_variable == '2':
            return ['front_cms/template2/staff.html']
        else:
            return ['front_cms/template1/staff.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_type = self.request.user.profile.type
        info = SchoolGeneralInfoModel.objects.first()
        if info.school_type == 'mix' and info.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=user_type).first()
        else:
            academic_info = SchoolAcademicInfoModel.objects.first()

        return context


class ContactPageView(LoginRequiredMixin, TemplateView):

    def dispatch(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()
        if frontend_setting:
            return super(ContactPageView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('maintenance_view'))

    def get_template_names(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()

        template_variable = frontend_setting.template

        if template_variable == '1':
            return ['front_cms/template1/contact_us.html']
        elif template_variable == '2':
            return ['front_cms/template2/contact_us.html']
        else:
            return ['front_cms/template1/contact_us.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_type = self.request.user.profile.type
        info = SchoolGeneralInfoModel.objects.first()
        if info.school_type == 'mix' and info.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=user_type).first()
        else:
            academic_info = SchoolAcademicInfoModel.objects.first()

        return context


class GalleryPageView(LoginRequiredMixin, TemplateView):

    def dispatch(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()
        if frontend_setting:
            return super(HomePageView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('maintenance_view'))

    def get_template_names(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()

        template_variable = frontend_setting.template

        if template_variable == '1':
            return ['front_cms/template1/homepage.html']
        elif template_variable == '2':
            return ['front_cms/template2/homepage.html']
        else:
            return ['front_cms/template1/homepage.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_type = self.request.user.profile.type
        info = SchoolGeneralInfoModel.objects.first()
        if info.school_type == 'mix' and info.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=user_type).first()
        else:
            academic_info = SchoolAcademicInfoModel.objects.first()

        return context


class EventPageView(LoginRequiredMixin, TemplateView):

    def dispatch(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()
        if frontend_setting:
            return super(HomePageView, self).dispatch(*args, **kwargs)
        else:
            return redirect(reverse('maintenance_view'))

    def get_template_names(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            frontend_setting = FrontEndSettingModel.objects.filter(type=self.request.user.profile.type).first()
        else:
            frontend_setting = FrontEndSettingModel.objects.first()

        template_variable = frontend_setting.template

        if template_variable == '1':
            return ['front_cms/template1/homepage.html']
        elif template_variable == '2':
            return ['front_cms/template2/homepage.html']
        else:
            return ['front_cms/template1/homepage.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_type = self.request.user.profile.type
        info = SchoolGeneralInfoModel.objects.first()
        if info.school_type == 'mix' and info.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=user_type).first()
        else:
            academic_info = SchoolAcademicInfoModel.objects.first()

        return context


class FrontSliderCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = FrontSliderModel
    permission_required = 'finance.add_feemodel'
    form_class = FrontSliderForm
    success_message = 'Home Page Slider Added Successfully'
    template_name = 'front_cms/slider/index.html'

    def get_success_url(self):
        return reverse('frontend_slider_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['slider_list'] = FrontSliderModel.objects.filter(type=self.request.user.profile.type)
        else:
            context['slider_list'] = FrontSliderModel.objects.all()
        return context


class FrontSliderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = FrontSliderModel
    permission_required = 'finance.view_feemodel'
    fields = '__all__'
    template_name = 'front_cms/slider/index.html'
    context_object_name = "slider_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return FrontSliderModel.objects.filter(type=self.request.user.profile.type)
        else:
            return FrontSliderModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FrontSliderForm

        return context


class FrontSliderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = FrontSliderModel
    permission_required = 'finance.change_feemodel'
    form_class = FrontSliderEditForm
    success_message = 'Home Page slider Updated Successfully'
    template_name = 'front_cms/slider/edit.html'

    def get_success_url(self):
        return reverse('frontend_slider_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = self.object

        return context


class FrontSliderDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = FrontSliderModel
    permission_required = 'finance.delete_feemodel'
    success_message = 'Home Page Slider Deleted Successfully'
    fields = '__all__'
    template_name = 'front_cms/slider/delete.html'
    context_object_name = "slider"

    def get_success_url(self):
        return reverse("frontend_slider_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
