from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from school_utility.models import *
from school_setting.models import SchoolGeneralInfoModel
from school_utility.forms import *
from student.models import StudentsModel


class HostelCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = HostelModel
    permission_required = 'school_utility.add_hostelmodel'
    form_class = HostelForm
    success_message = 'Hostel Added Successfully'
    template_name = 'school_utility/hostel/index.html'

    def get_success_url(self):
        return reverse('hostel_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['hostel_list'] = HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['class_list'] = ClassesModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['class_section_list'] = ClassSectionModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            context['hostel_list'] = HostelModel.objects.all().order_by('name')
            context['class_list'] = ClassesModel.objects.all().order_by('name')
            context['class_section_list'] = ClassSectionModel.objects.all().order_by('name')
        return context

    def get_form_kwargs(self):
        kwargs = super(HostelCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class HostelListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = HostelModel
    permission_required = 'school_utility.view_hostelmodel'
    fields = '__all__'
    template_name = 'school_utility/hostel/index.html'
    context_object_name = "hostel_list"

    def get_queryset(self):
        school_setting=SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return HostelModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            context['class_section_list'] = ClassSectionModel.objects.filter(type=self.request.user.profile.type)
            context['hostel_list'] = HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['class_list'] = ClassesModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            form_kwargs['type'] = self.request.user.profile.type
        else:
            context['class_section_list'] = ClassSectionModel.objects.all()
            context['hostel_list'] = HostelModel.objects.all().order_by('name')
            context['class_list'] = ClassesModel.objects.all().order_by('name')
        context['form'] = HostelForm(**form_kwargs)
        return context


class HostelDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = HostelModel
    permission_required = 'school_utility.add_hostelmodel'
    fields = '__all__'
    template_name = 'school_utility/hostel/detail.html'
    context_object_name = "hostel"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            context['class_section_list'] = ClassSectionModel.objects.filter(type=self.request.user.profile.type)
            context['hostel_list'] = HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['class_list'] = ClassesModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            form_kwargs['type'] = self.request.user.profile.type

        else:
            context['class_section_list'] = ClassSectionModel.objects.all()
            context['hostel_list'] = HostelModel.objects.all().order_by('name')
            context['class_list'] = ClassesModel.objects.all().order_by('name')
        context['student_list'] = StudentsModel.objects.filter(hostel=self.object).order_by(
            'surname')
        context['form'] = HostelForm(**form_kwargs)
        context['hostel_rep_form'] = HostelRepEditForm

        return context


class HostelUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = HostelModel
    permission_required = 'school_utility.change_hostelmodel'
    form_class = HostelEditForm
    success_message = 'Hostel Updated Successfully'
    template_name = 'school_utility/hostel/index.html'

    def get_success_url(self):
        return reverse('hostel_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hostel_list'] = HostelModel.objects.all()
        context['class_list'] = ClassesModel.objects.all()
        context['class_section_list'] = ClassSectionModel.objects.all()
        return context


class HostelRepUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = HostelModel
    permission_required = 'school_utility.change_hostelmodel'
    form_class = HostelRepEditForm
    success_message = 'Hostel Rep Updated Successfully'
    template_name = 'school_utility/hostel/detail.html'

    def get_success_url(self):
        return reverse('hostel_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hostel_rep_form'] = HostelRepEditForm
        context['hostel'] = self.object
        return context


class HostelDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = HostelModel
    permission_required = 'school_utility.delete_hostelmodel'
    success_message = 'Hostel Deleted Successfully'
    fields = '__all__'
    template_name = 'school_utility/hostel/delete.html'
    context_object_name = "hostel"

    def get_success_url(self):
        return reverse("hostel_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HostelRoomCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = HostelRoomModel
    permission_required = 'school_utility.add_hostelroommodel'
    form_class = HostelRoomForm
    success_message = 'Hostel Room Added Successfully'
    template_name = 'school_utility/hostel_room/index.html'

    def get_success_url(self):
        return reverse('hostel_room_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hostel_list'] = HostelModel.objects.all()
        context['hostel_room_list'] = HostelRoomModel.objects.all()
        context['class_list'] = ClassesModel.objects.all()
        context['class_section_list'] = ClassSectionModel.objects.all()
        return context


class HostelRoomListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = HostelRoomModel
    permission_required = 'school_utility.view_hostelroommodel'
    fields = '__all__'
    template_name = 'school_utility/hostel_room/index.html'
    context_object_name = "hostel_room_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return HostelRoomModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return HostelRoomModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            context['class_section_list'] = ClassSectionModel.objects.filter(type=self.request.user.profile.type)
            context['hostel_list'] = HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['hostel_room_list'] = HostelRoomModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['class_list'] = ClassesModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            form_kwargs['type'] = self.request.user.profile.type
        else:
            context['class_section_list'] = ClassSectionModel.objects.all()
            context['hostel_list'] = HostelModel.objects.all().order_by('name')
            context['hostel_room_list'] = HostelRoomModel.objects.all().order_by('name')
            context['class_list'] = ClassesModel.objects.all().order_by('name')
        context['form'] = HostelRoomForm(**form_kwargs)

        return context


class HostelRoomDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = HostelRoomModel
    permission_required = 'school_utility.view_hostelroommodel'
    fields = '__all__'
    template_name = 'school_utility/hostel_room/detail.html'
    context_object_name = "hostel_room"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            context['class_section_list'] = ClassSectionModel.objects.filter(type=self.request.user.profile.type)
            context['hostel_list'] = HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['hostel_room_list'] = HostelRoomModel.objects.filter(type=self.request.user.profile.type).order_by(
                'name')
            context['class_list'] = ClassesModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            form_kwargs['type'] = self.request.user.profile.type
        else:
            context['class_section_list'] = ClassSectionModel.objects.all()
            context['hostel_list'] = HostelModel.objects.all().order_by('name')
            context['hostel_room_list'] = HostelRoomModel.objects.all().order_by('name')
            context['class_list'] = ClassesModel.objects.all().order_by('name')
        context['form'] = HostelRoomForm(**form_kwargs)
        context['student_list'] = StudentsModel.objects.filter(hostel_room=self.object).order_by(
            'surname')
        return context


class HostelRoomUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = HostelRoomModel
    permission_required = 'school_utility.change_hostelroommodel'
    form_class = HostelRoomEditForm
    success_message = 'Hostel Room Updated Successfully'
    template_name = 'school_utility/hostel_room/index.html'

    def get_success_url(self):
        return reverse('hostel_room_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hostel_list'] = HostelModel.objects.all()
        context['hostel_room_list'] = HostelRoomModel.objects.all()
        context['class_list'] = ClassesModel.objects.all()
        context['class_section_list'] = ClassSectionModel.objects.all()
        return context


class HostelRoomRepUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = HostelRoomModel
    permission_required = 'school_utility.change_hostelroommodel'
    form_class = HostelRoomRepForm
    success_message = 'Hostel Room Rep Updated Successfully'
    template_name = 'school_utility/hostel_room/index.html'

    def get_success_url(self):
        return reverse('hostel_room_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hostel_list'] = HostelModel.objects.all()
        context['hostel_room_list'] = HostelRoomModel.objects.all()
        context['class_list'] = ClassesModel.objects.all()
        context['class_section_list'] = ClassSectionModel.objects.all()
        return context


class HostelRoomDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = HostelRoomModel
    permission_required = 'school_utility.delete_hostelroommodel'
    success_message = 'Hostel Room Deleted Successfully'
    fields = '__all__'
    template_name = 'school_utility/hostel_room/delete.html'
    context_object_name = "hostel_room"

    def get_success_url(self):
        return reverse("hostel_room_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HostelBedCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = HostelBedModel
    permission_required = 'school_utility.add_hostelbedmodel'
    form_class = HostelBedForm
    success_message = 'Hostel Bed Added Successfully'
    template_name = 'school_utility/hostel_bed/index.html'

    def get_success_url(self):
        return reverse('hostel_bed_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['hostel_list'] = HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['hostel_room_list'] = HostelRoomModel.objects.filter(type=self.request.user.profile.type).order_by(
                'name')
            context['hostel_bed_list'] = HostelBedModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            context['hostel_list'] = HostelModel.objects.all().order_by('name')
            context['hostel_room_list'] = HostelRoomModel.objects.all().order_by('name')
            context['hostel_bed_list'] = HostelBedModel.objects.all().order_by('name')

        return context


class HostelBedListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = HostelRoomModel
    permission_required = 'school_utility.view_hostelbedmodel'
    fields = '__all__'
    template_name = 'school_utility/hostel_bed/index.html'
    context_object_name = "hostel_bed_list"

    def get_queryset(self):
        return HostelBedModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['hostel_list'] = HostelModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            context['hostel_room_list'] = HostelRoomModel.objects.filter(type=self.request.user.profile.type).order_by(
                'name')
            context['hostel_bed_list'] = HostelBedModel.objects.filter(type=self.request.user.profile.type).order_by(
                'name')
        else:
            context['hostel_list'] = HostelModel.objects.all().order_by('name')
            context['hostel_room_list'] = HostelRoomModel.objects.all().order_by('name')
            context['hostel_bed_list'] = HostelBedModel.objects.all().order_by('name')
        context['form'] = HostelBedForm

        return context


class HostelBedDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'school_utility.view_hostelbedmodel'
    model = HostelBedModel
    fields = '__all__'
    template_name = 'school_utility/hostel_bed/detail.html'
    context_object_name = "hostel_bed"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hostel_list'] = HostelModel.objects.all()
        context['room_list'] = HostelRoomModel.objects.filter(hostel=self.object.hostel)
        context['hostel_bed_list'] = HostelBedModel.objects.all()
        return context


class HostelBedUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = HostelBedModel
    permission_required = 'school_utility.change_hostelbedmodel'
    form_class = HostelBedEditForm
    success_message = 'Hostel Bed Updated Successfully'
    template_name = 'school_utility/hostel_bed/index.html'

    def get_success_url(self):
        return reverse('hostel_bed_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hostel_list'] = HostelModel.objects.all()
        context['hostel_bed_list'] = HostelBedModel.objects.all()
        return context


class HostelBedDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = HostelBedModel
    permission_required = 'school_utility.update_hostelbedmodel'
    success_message = 'Hostel Bed Deleted Successfully'
    fields = '__all__'
    template_name = 'school_utility/hostel_bed/delete.html'
    context_object_name = "hostel_bed"

    def get_success_url(self):
        return reverse("hostel_bed_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TransportRouteCreateView(SuccessMessageMixin, CreateView):
    model = TransportRouteModel
    form_class = TransportRouteForm
    success_message = 'Transportation Route Added Successfully'
    template_name = 'school_utility/transport_route/index.html'

    def get_success_url(self):
        return reverse('transport_route_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transport_route_list'] = TransportRouteModel.objects.all()
        return context


class TransportRouteListView(ListView):
    model = TransportRouteModel
    fields = '__all__'
    template_name = 'school_utility/transport_route/index.html'
    context_object_name = "transport_route_list"

    def get_queryset(self):
        return TransportRouteModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transport_route_list'] = TransportRouteModel.objects.all()
        context['form'] = TransportRouteForm

        return context


class TransportRouteDetailView(DetailView):
    model = TransportRouteModel
    fields = '__all__'
    template_name = 'school_utility/transport_route/detail.html'
    context_object_name = "transport_route"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TransportPathForm
        context['path_list'] = TransportPathModel.objects.filter(route=self.object).order_by('order')
        return context


class TransportRouteUpdateView(SuccessMessageMixin, UpdateView):
    model = TransportRouteModel
    form_class = TransportRouteEditForm
    success_message = 'Transport Route Updated Successfully'
    template_name = 'school_utility/transport_route/index.html'

    def get_success_url(self):
        return reverse('transport_route_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transport_route_list'] = TransportRouteModel.objects.all()
        return context


class TransportRouteDeleteView(SuccessMessageMixin, DeleteView):
    model = TransportRouteModel
    success_message = 'Transport Route Deleted Successfully'
    fields = '__all__'
    template_name = 'school_utility/transport_route/delete.html'
    context_object_name = "transport_route"

    def get_success_url(self):
        return reverse("transport_route_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TransportPathCreateView(SuccessMessageMixin, CreateView):
    model = TransportPathModel
    form_class = TransportPathForm
    success_message = 'Transportation Path Added Successfully'
    template_name = 'school_utility/transport_path/index.html'

    def get_success_url(self):
        return reverse('transport_route_detail', kwargs={'pk': self.object.route.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transport_path_list'] = TransportPathModel.objects.all()
        return context


class TransportPathUpdateView(SuccessMessageMixin, UpdateView):
    model = TransportPathModel
    form_class = TransportPathEditForm
    success_message = 'Transport Path Updated Successfully'
    template_name = 'school_utility/transport_path/index.html'

    def get_success_url(self):
        return reverse('transport_route_detail', kwargs={'pk': self.object.route.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transport_path_list'] = TransportPathModel.objects.all()
        return context


class TransportPathDeleteView(SuccessMessageMixin, DeleteView):
    model = TransportPathModel
    success_message = 'Transport Path Deleted Successfully'
    fields = '__all__'
    template_name = 'school_utility/transport_path/delete.html'
    context_object_name = "transport_path"

    def get_success_url(self):
        return reverse("transport_route_detail", kwargs={'pk': self.get_object().route.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TransportVehicleCreateView(SuccessMessageMixin, CreateView):
    model = TransportVehicleModel
    form_class = TransportVehicleForm
    success_message = 'Transportation Vehicle Added Successfully'
    template_name = 'school_utility/transport_vehicle/index.html'

    def get_success_url(self):
        return reverse('transport_vehicle_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transport_vehicle_list'] = TransportVehicleModel.objects.all()
        return context


class TransportVehicleListView(ListView):
    model = TransportVehicleModel
    fields = '__all__'
    template_name = 'school_utility/transport_vehicle/index.html'
    context_object_name = "transport_vehicle_list"

    def get_queryset(self):
        return TransportVehicleModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transport_vehicle_list'] = TransportVehicleModel.objects.all()
        context['form'] = TransportVehicleForm

        return context


class TransportVehicleDetailView(DetailView):
    model = TransportVehicleModel
    fields = '__all__'
    template_name = 'school_utility/transport_vehicle/detail.html'
    context_object_name = "transport_vehicle"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TransportVehicleEditForm(instance=self.object)
        return context


class TransportVehicleUpdateView(SuccessMessageMixin, UpdateView):
    model = TransportVehicleModel
    form_class = TransportVehicleEditForm
    success_message = 'Transport Vehicle Updated Successfully'
    template_name = 'school_utility/transport_vehicle/index.html'

    def get_success_url(self):
        return reverse('transport_vehicle_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['transport_vehicle_list'] = TransportVehicleModel.objects.all()
        return context


class TransportVehicleDeleteView(SuccessMessageMixin, DeleteView):
    model = TransportVehicleModel
    success_message = 'Transport Vehicle Deleted Successfully'
    fields = '__all__'
    template_name = 'school_utility/transport_vehicle/delete.html'
    context_object_name = "transport_vehicle"

    def get_success_url(self):
        return reverse("transport_vehicle_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def get_hostel_rooms(request):
    pk = request.GET.get('hostel_pk')
    room_list = HostelRoomModel.objects.filter(hostel__id=pk)
    room_list_option = "<option value=''>------------</option>"
    for room in room_list:
        room_list_option += "<option value='{}'>{} ({})</option>".format(room.id, room.name.upper(), room.vacant_beds())

    if room_list_option == "<option value=''>------------</option>":
        room_list_option += "<option value=''>No Available Room in the Hostel</option>"
    return HttpResponse(room_list_option)


def get_room_beds(request):
    pk = request.GET.get('room_pk')
    room = HostelRoomModel.objects.get(pk=1)
    bed_list = HostelBedModel.objects.filter(bed_student__isnull=True, room__pk=pk)
    bed_list_option = "<option value=''>------------</option>"
    for bed in bed_list:
        bed_list_option += "<option value='{}'>{}</option>".format(bed.id, bed.name.upper())
    if bed_list_option == "<option value=''>------------</option>":
        bed_list_option = "<option value=''>No Empty Bed in the Room</option>"
    return HttpResponse(bed_list_option)


class SchoolUtilitySettingView(LoginRequiredMixin, TemplateView):
    template_name = 'school_utility/setting/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            utility_info = SchoolUtilitySettingModel.objects.filter(type=self.request.user.profile.type).first()
            form_kwargs['type'] = self.request.user.profile.type
        else:
            utility_info = SchoolUtilitySettingModel.objects.first()

        if not utility_info:
            form = SchoolUtilitySettingCreateForm(**form_kwargs)
            is_utility_info = False
        else:
            form = SchoolUtilitySettingEditForm(instance=utility_info, **form_kwargs)
            is_utility_info = True
        context['form'] = form
        context['is_utility_info'] = is_utility_info
        context['utility_info'] = utility_info
        return context


class SchoolUtilitySettingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SchoolUtilitySettingModel
    form_class = SchoolUtilitySettingCreateForm
    template_name = 'school_utility/setting/index.html'
    success_message = 'Utility Settings updated Successfully'

    def get_success_url(self):
        return reverse('utility_info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()

        return context

    def get_form_kwargs(self):
        kwargs = super(SchoolUtilitySettingCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class SchoolUtilitySettingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SchoolUtilitySettingModel
    form_class = SchoolUtilitySettingEditForm
    template_name = 'school_utility/setting/index.html'
    success_message = 'Utility Setting updated Successfully'

    def get_success_url(self):
        return reverse('utility_info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_form_kwargs(self):
        kwargs = super(SchoolUtilitySettingUpdateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class UtilityDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'school_utility/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_type = self.request.user.profile.type
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            boarding_student = StudentsModel.objects.filter(type=user_type, is_boarding=True).count()
            male_boarding_student = StudentsModel.objects.filter(type=user_type, is_boarding=True, gender='MALE').count()
            female_boarding_student = StudentsModel.objects.filter(type=user_type, is_boarding=True, gender='FEMALE').count()
            total_student = StudentsModel.objects.filter(type=user_type).count()
            transport_student = StudentsModel.objects.filter(type=user_type, use_transport=True).count()
            total_bed = HostelBedModel.objects.filter(type=user_type).count()
            vacant_bed = HostelBedModel.objects.filter(type=user_type, bed_student__isnull=True).count()
            occupied_bed = HostelBedModel.objects.filter(type=user_type, bed_student__isnull=False).count()

        else:
            boarding_student = StudentsModel.objects.filter(is_boarding=True).count()
            male_boarding_student = StudentsModel.objects.filter(is_boarding=True, gender='MALE').count()
            female_boarding_student = StudentsModel.objects.filter(is_boarding=True, gender='FEMALE').count()
            total_student = StudentsModel.objects.filter().count()
            transport_student = StudentsModel.objects.filter(use_transport=True).count()
            total_bed = HostelBedModel.objects.count()
            vacant_bed = HostelBedModel.objects.filter(bed_student__isnull=True).count()
            occupied_bed = HostelBedModel.objects.filter(bed_student__isnull=False).count()

        context['boarding_student'] = boarding_student
        context['male_boarding_student'] = male_boarding_student
        context['female_boarding_student'] = female_boarding_student
        context['percentage_boarding_student'] = round((boarding_student/total_student) * 100) if total_student else 0
        context['transport_student'] = transport_student
        context['total_bed'] = total_bed
        context['vacant_bed'] = vacant_bed
        context['occupied_bed'] = occupied_bed
        return context
