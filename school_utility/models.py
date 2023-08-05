from django.db import models
from django.contrib.auth.models import User
from human_resource.models import StaffModel
from academic.models import *
from school_setting.models import SchoolSettingModel
from django.apps import apps


class HostelModel(models.Model):
    name = models.CharField(max_length=200)
    GENDER = (('male', 'MALE'), ('female', 'FEMALE'), ('combined', 'COMBINED'))
    hostel_gender = models.CharField(max_length=100, choices=GENDER)
    HOSTEL_TYPE = (('student', 'STUDENT'), ('staff', 'STAFF'), ('combined', 'COMBINED'))
    hostel_type = models.CharField(max_length=100, choices=HOSTEL_TYPE)
    student_class = models.ManyToManyField(ClassesModel, blank=True)
    class_section = models.ManyToManyField(ClassSectionModel, blank=True)
    hostel_rep = models.ForeignKey('student.StudentsModel', related_name='hostel_rep', null=True, blank=True,
                                   on_delete=models.SET_NULL)
    assistant_hostel_rep = models.ForeignKey('student.StudentsModel', related_name='assistant_hostel_rep', null=True,
                                             blank=True, on_delete=models.SET_NULL)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='hostel_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'type'],
                name='unique_hostel_name_combo'
            )
        ]

    def __str__(self):
        return self.name.upper()

    def vacant_beds(self):
        return HostelBedModel.objects.filter(hostel=self).count() - HostelBedModel.objects.filter(hostel=self,
                                                                                                  bed_student__isnull=False).count()

    def students(self):
        StudentsModel = apps.get_model('student', 'StudentsModel')
        return StudentsModel.objects.filter(hostel=self)


class HostelRoomModel(models.Model):
    name = models.CharField(max_length=200)
    hostel = models.ForeignKey(HostelModel, on_delete=models.CASCADE, related_name='room_hostel')
    GENDER = (('male', 'MALE'), ('female', 'FEMALE'), ('combined', 'COMBINED'))
    room_gender = models.CharField(max_length=100, choices=GENDER)
    ROOM_TYPE = (('student', 'STUDENT'), ('staff', 'STAFF'), ('combined', 'COMBINED'))
    room_type = models.CharField(max_length=100, choices=ROOM_TYPE)
    student_class = models.ManyToManyField(ClassesModel, blank=True)
    class_section = models.ManyToManyField(ClassSectionModel, blank=True)
    room_rep = models.ForeignKey('student.StudentsModel', related_name='room_rep', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    assistant_room_rep = models.ForeignKey('student.StudentsModel', related_name='assistant_room_rep', null=True,
                                           blank=True, on_delete=models.SET_NULL)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='hostel_room_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'hostel', 'type'],
                name='unique_hostel_room_combo'
            )
        ]

    def __str__(self):
        return self.name.upper()

    def vacant_beds(self):
        total_bed = HostelBedModel.objects.filter(room=self).count()
        occupied_bed = HostelBedModel.objects.filter(room=self,  bed_student__isnull=False).count()

        return total_bed - occupied_bed


class HostelBedModel(models.Model):
    name = models.CharField(max_length=200)
    hostel = models.ForeignKey(HostelModel, on_delete=models.CASCADE, blank=True, related_name='bed_hostel')
    room = models.ForeignKey(HostelRoomModel, on_delete=models.CASCADE, related_name='bed_room')

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='hostel_bed_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'room', 'hostel', 'type'],
                name='unique_hostel_bed_combo'
            )
        ]

    def __str__(self):
        return self.name.upper()


class TransportRouteModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='transport_route_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'type'],
                name='unique_transport_route_combo'
            )
        ]

    def __str__(self):
        return self.name.upper()


class TransportPathModel(models.Model):
    name = models.CharField(max_length=200)
    route = models.ForeignKey(TransportRouteModel, on_delete=models.CASCADE, related_name='route_paths')
    order = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='transport_path_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'type'],
                name='unique_transport_path_combo'
            )
        ]

    def __str__(self):
        return self.name.upper()
    

class TransportVehicleModel(models.Model):
    vehicle_id = models.CharField(max_length=200)
    plate_number = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, unique=True, null=True, blank=True)
    route = models.ForeignKey(TransportRouteModel, on_delete=models.CASCADE, blank=True, null=True,
                              related_name='route_vehicle')
    driver = models.ForeignKey(StaffModel, on_delete=models.CASCADE, blank=True, null=True,
                               related_name='driver_vehicle')
    attendant = models.ForeignKey(StaffModel, on_delete=models.CASCADE, blank=True, null=True,
                                  related_name='attendant_vehicle')
    STATUS = (
        ('available', 'AVAILABLE'), ('maintenance', 'MAINTENANCE')
    )
    status = models.CharField(max_length=20, choices=STATUS, default='available', blank=True)

    STATE = (
        ('in school', 'IN SCHOOL'), ('driving student home', 'DRIVING STUDENT HOME'),
        ('bringing student to school', 'BRINGING STUDENT TO SCHOOL')
    )
    state = models.CharField(max_length=100, choices=STATE, default='in school', blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='transport_vehicle_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['vehicle_id', 'type'],
                name='unique_vehicle_combo'
            )
        ]

    def __str__(self):
        return self.vehicle_id.upper()


class SchoolUtilitySettingModel(models.Model):
    drivers = models.ManyToManyField(StaffModel, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='utility_setting_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
