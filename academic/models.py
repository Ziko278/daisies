from django.db import models
from django.contrib.auth.models import User
from human_resource.models import StaffModel
from school_setting.models import SchoolSettingModel


class SubjectsModel(models.Model):
    """"""
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    teachers = models.ManyToManyField(StaffModel, blank=True)

    SUBJECT_TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    subject_type = models.CharField(max_length=10, choices=SUBJECT_TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return self.name.upper()

    def save(self, *args, **kwargs):
        setting = SchoolSettingModel.objects.first()
        if setting.general_info.school_type != 'mix':
            self.subject_type = setting.general_info.school_type

        super(SubjectsModel, self).save(*args, **kwargs)

    def number_of_class(self):
        return ClassesModel.objects.filter(subjects__in=[self]).count()


class ClassSectionModel(models.Model):
    """"""
    name = models.CharField(max_length=100)


class ClassesModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=25, null=True, blank=True)
    section = models.ForeignKey(ClassSectionModel, on_delete=models.CASCADE, null=True, blank=True)
    subjects = models.ManyToManyField(SubjectsModel, blank=True)
    form_teacher = models.ForeignKey(StaffModel, null=True, blank=True, on_delete=models.SET_NULL)
    assistant_form_teacher = models.ForeignKey(StaffModel, related_name='assistant_form_teacher', null=True, blank=True, on_delete=models.SET_NULL)
    class_rep = models.ForeignKey('student.StudentsModel', related_name='class_rep', null=True, blank=True, on_delete=models.SET_NULL)
    assistant_class_rep = models.ForeignKey('student.StudentsModel', related_name='assistant_class_rep', null=True, blank=True, on_delete=models.SET_NULL)
    CLASS_TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    class_type = models.CharField(max_length=10, choices=CLASS_TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'section', 'class_type'],
                name='unique_name_class_type_combo'
            )
        ]

    def __str__(self):
        return self.name.upper()

    def save(self, *args, **kwargs):
        setting = SchoolSettingModel.objects.first()
        if setting.general_info.school_type != 'mix':
            if setting.general_info.school_type == 'pri':
                self.class_type = 'pri'
            if setting.general_info.school_type == 'sec':
                self.class_type = 'sec'

        super(ClassesModel, self).save(*args, **kwargs)



