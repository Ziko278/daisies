from django.db import models
from academic.models import ClassesModel
from school_setting.models import SchoolSettingModel, SessionModel
import random


class ParentsModel(models.Model):
    """"""
    TITLE = (
        ('MR', 'MR'), ('MRS', 'MRS'), ('MISS', 'MISS'), ('MS', 'MS'), ('MAL', 'MAL'), ('DOC', 'DOC'),
        ('BARR', 'BARR'), ('PST', 'PST'), ('PROF', 'PROF'),  ('ENGR', 'ENGR'),
    )
    title = models.CharField(max_length=10, choices=TITLE)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)

    image = models.FileField(blank=True, null=True, upload_to='images/parent_images')
    residential_address = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    occupation = models.CharField(max_length=100, null=True, blank=True)
    office_address = models.CharField(max_length=200, null=True, blank=True)
    office_mobile = models.CharField(max_length=20, null=True, blank=True)

    registration_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=15, blank=True, default='active')

    def __str__(self):
        if self.middle_name:
            return self.title + ' ' + self.surname + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.title + ' ' + self.surname + ' ' + self.last_name

    def number_of_ward(self):
        return StudentsModel.objects.filter(parent=self).count()


class StudentsModel(models.Model):
    """"""
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    GENDER = (
        ('MALE', 'MALE'), ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=10, choices=GENDER)

    image = models.FileField(blank=True, null=True, upload_to='images/student_images')
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    blood_group = models.CharField(max_length=20, null=True, blank=True)
    genotype = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    health_issues = models.TextField(null=True, blank=True)
    student_class = models.ForeignKey(ClassesModel, null=True, on_delete=models.CASCADE)
    parent = models.ForeignKey(ParentsModel, on_delete=models.CASCADE, blank=True, null=True)
    RELATIONSHIP_WITH_PARENT = (
        ('father', 'FATHER'), ('mother', 'MOTHER'), ('sister', 'SISTER'), ('brother', 'BROTHER'), ('uncle', 'UNCLE'),
        ('aunty', 'AUNTY'), ('pastor', 'PASTOR'), ('others', 'OTHERS')
    )
    relationship_with_parent = models.CharField(max_length=20, choices=RELATIONSHIP_WITH_PARENT)

    registration_date = models.DateField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, default='active')

    def __str__(self):
        if self.middle_name:
            return self.surname + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.surname + ' ' + self.last_name


class StudentAcademicRecordModel(models.Model):
    student = models.ForeignKey(StudentsModel, on_delete=models.CASCADE)
    entry_class = models.ForeignKey(ClassesModel, on_delete=models.SET_NULL, null=True)
    entry_session = models.ForeignKey(SessionModel, on_delete=models.SET_NULL, null=True)
    entry_term = models.CharField(max_length=20)
    current_class = models.ForeignKey(ClassesModel, related_name='student_current_class', on_delete=models.SET_NULL, null=True)
    previous_classes = models.JSONField(null=True, blank=True)
