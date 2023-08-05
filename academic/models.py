from django.db import models
from django.contrib.auth.models import User
from human_resource.models import StaffModel
from school_setting.models import SchoolSettingModel
from django.apps import apps


class SubjectsModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    SUBJECT_TYPE = (
        ('theory', 'THEORY'), ('practical', 'PRACTICAL'), ('combined', 'COMBINED')
    )
    subject_type = models.CharField(max_length=10, choices=SUBJECT_TYPE, default='theory')

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='subject_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'type'],
                name='unique_subject_name_type_combo',
                violation_error_message='Subject Already Exists'
            )
        ]

    def __str__(self):
        return self.name.upper()

    def number_of_class(self):
        return ClassesModel.objects.filter(subjects__in=[self]).count()


class ClassSectionModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'MIXED')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='class_section_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'type'],
                name='unique_class_name_type_combo',
                violation_error_message='Class Section Already Exists'
            )
        ]

    def __str__(self):
        return self.name.upper()

    def no_of_students(self):
        StudentsModel = apps.get_model('student', 'StudentsModel')
        return StudentsModel.objects.filter(class_section=self).count()

    def save(self, *args, **kwargs):

        super(ClassSectionModel, self).save(*args, **kwargs)


class ClassesModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    section = models.ManyToManyField(ClassSectionModel, blank=True)
    RESULT_TYPE = (
        ('score', 'SCORE BASED'), ('text', 'TEXT BASED')
    )
    result_type = models.CharField(max_length=20, choices=RESULT_TYPE)
    is_graduation_class = models.BooleanField(default=False)
    promotion_class = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='class_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'type'],
                name='unique_name_class_type_combo'
            )
        ]

    def __str__(self):
        return self.name.upper()

    def no_of_students(self):
        StudentsModel = apps.get_model('student', 'StudentsModel')
        return StudentsModel.objects.filter(student_class=self).count()

    def save(self, *args, **kwargs):

        super(ClassesModel, self).save(*args, **kwargs)


class ClassSectionInfoModel(models.Model):
    """"""
    student_class = models.ForeignKey(ClassesModel, on_delete=models.CASCADE)
    section = models.ForeignKey(ClassSectionModel, blank=True, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(SubjectsModel, blank=True, related_name='subject_class_info')
    form_teacher = models.ForeignKey(StaffModel, null=True, blank=True, on_delete=models.SET_NULL)
    assistant_form_teacher = models.ForeignKey(StaffModel, related_name='assistant_form_teacher', null=True, blank=True,
                                               on_delete=models.SET_NULL)
    class_rep = models.ForeignKey('student.StudentsModel', related_name='class_rep', null=True, blank=True,
                                  on_delete=models.SET_NULL)
    assistant_class_rep = models.ForeignKey('student.StudentsModel', related_name='assistant_class_rep', null=True,
                                            blank=True, on_delete=models.SET_NULL)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='class_section_info_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = []
        constraints = [
            models.UniqueConstraint(
                fields=['student_class', 'section', 'type'],
                name='unique_student_class_section_combo'
            )
        ]

    def __str__(self):
        return "{} {}".format(self.student_class.name.upper(), self.section.name.upper())

    def number_of_students(self):
        StudentsModel = apps.get_model('student', 'StudentsModel')
        return StudentsModel.objects.filter(student_class=self.student_class, class_section=self.section).count()


class ClassSectionSubjectTeacherModel(models.Model):
    """"""
    subject = models.ForeignKey(SubjectsModel, blank=True, on_delete=models.CASCADE,
                                related_name='subject_class_section_info')
    student_class = models.ManyToManyField(ClassesModel, blank=True)
    class_section = models.ManyToManyField(ClassSectionModel, blank=True)
    teachers = models.ManyToManyField(StaffModel, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='class_section_subject_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class DaysModel(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name.upper()


class AcademicSettingModel(models.Model):
    """"""
    active_days = models.ManyToManyField(DaysModel, blank=True, related_name='active_days')
    week_start_day = models.ForeignKey(DaysModel, on_delete=models.SET_NULL, null=True, blank=True)
    head_teacher = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, blank=True, null=True)
    promotion_cutoff_score = models.FloatField(default=30)
    use_promotion_cutoff = models.BooleanField(default=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)

    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def week_active_days(self):
        return self.active_days.count()

    def termly_active_days(self):
        return 0


class ClassTimeTableModel(models.Model):
    student_class = models.ForeignKey(ClassesModel, on_delete=models.CASCADE)
    class_section = models.ForeignKey(ClassSectionModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectsModel, blank=True, null=True, on_delete=models.CASCADE)
    CLASS_BREAK = (('short break', 'SHORT BREAK'), ('long break', 'LONG BREAK'), ('closing time', 'CLOSING TIME'))
    class_break = models.CharField(max_length=50, choices=CLASS_BREAK, blank=True, null=True)
    day = models.ForeignKey(DaysModel, on_delete=models.CASCADE)
    start_time = models.TimeField()
    stop_time = models.TimeField()
    teacher = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True)
    class_room = models.CharField(max_length=200, blank=True, null=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='class_timetable_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def start_time_str(self):
        hours = self.start_time.hour
        minutes = self.start_time.minute

        return f"{hours:02d}:{minutes:02d}"

    def stop_time_str(self):
        hours = self.stop_time.hour
        minutes = self.stop_time.minute

        return f"{hours:02d}:{minutes:02d}"


class LessonNoteModel(models.Model):
    student_class = models.ManyToManyField(ClassSectionInfoModel, blank=True)
    subject = models.ForeignKey(SubjectsModel, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    grant_access = models.BooleanField(default=False)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='lesson_note_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class LessonDocumentModel(models.Model):
    student_class = models.ManyToManyField(ClassSectionInfoModel, blank=True)
    subject = models.ForeignKey(SubjectsModel, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    grant_access = models.BooleanField(default=False)
    document = models.FileField()
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='lesson_document_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


