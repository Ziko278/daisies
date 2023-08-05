from django.db import models
from django.contrib.auth.models import User
from school_setting.models import SchoolSettingModel, SessionModel
from student.models import StudentsModel
from academic.models import *
from school_setting.models import SchoolAcademicInfoModel


class ExamModel(models.Model):
    """"""
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=100, null=True, blank=True)
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE, blank=True)
    TERM = (
        ('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')
    )
    term = models.CharField(max_length=10, choices=TERM, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    EXAM_TYPE = (
        ('exam', 'EXAM'), ('assessment', 'ASSESSMENT'), ('assignment', 'ASSIGNMENT')
    )
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPE, blank=True, null=True)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    student_class = models.ManyToManyField(ClassSectionInfoModel, blank=True)

    def __str__(self):
        return self.name.upper()

    def duration(self):
        if self.start_date and self.end_date:
            return "{} - {}".format(self.start_date, self.end_date)
        return '----------'

    def save(self, *args, **kwargs):
        academic_info = SchoolAcademicInfoModel.objects.first()
        self.session = academic_info.session
        self.term = academic_info.term
        super(ExamModel, self).save(*args, **kwargs)


class ExamHallModel(models.Model):
    name = models.CharField(max_length=200)


class ExamTimeTableModel(models.Model):
    """"""
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE, related_name='timetable')
    student_class = models.ManyToManyField(ClassesModel, blank=True)
    class_section = models.ManyToManyField(ClassSectionModel, blank=True)
    subject = models.ForeignKey(SubjectsModel, on_delete=models.CASCADE)
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE, blank=True)
    TERM = (
        ('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')
    )
    term = models.CharField(max_length=10, choices=TERM, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    EXAM_TYPE = (
        ('objective', 'OBJECTIVE'), ('theory', 'THEORY'), ('practical', 'PRACTICAL'), ('combined', 'COMBINED')
    )
    exam_type = models.CharField(max_length=10, choices=EXAM_TYPE, blank=True, null=True)
    EXAM_MODE = (
        ('online', 'ONLINE'), ('paper/pen', 'PAPER/PEN'), ('combined', 'COMBINED')
    )
    exam_mode = models.CharField(max_length=10, choices=EXAM_MODE, default='paper/pen', blank=True, null=True)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)

    def __str__(self):
        return self.subject.name.upper()

    def save(self, *args, **kwargs):
        self.session = self.exam.session
        self.term = self.exam.term
        super(ExamTimeTableModel, self).save(*args, **kwargs)


class ExamQuestionOptionModel(models.Model):
    numbering = models.CharField(max_length=10)
    option = models.TextField()
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)


class ExamQuestionModel(models.Model):
    timetable = models.ForeignKey(ExamTimeTableModel, on_delete=models.CASCADE)
    numbering = models.CharField(max_length=10)
    question = models.TextField()
    sub_questions = models.ManyToManyField('self', blank=True)
    options = models.ManyToManyField(ExamQuestionOptionModel, blank=True)
    correct_option = models.ForeignKey(ExamQuestionOptionModel, on_delete=models.SET_NULL, null=True, blank=True,
                                       related_name='correct_answer')
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    mark = models.FloatField()
    QUESTION_TYPE = (
        ('objective', 'OBJECTIVE'), ('subjective', 'SUBJECTIVE'), ('theory', 'THEORY'), ('practical', 'PRACTICAL'))
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPE)
    subjective_answer = models.CharField(max_length=200, null=True, blank=True)
    theory_answer = models.TextField(null=True, blank=True)
    is_sub = models.BooleanField(default=False)


class ExamSittingModel(models.Model):
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectsModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentsModel, on_delete=models.CASCADE)
    sit_number = models.CharField(max_length=100)


class ExamResultModel(models.Model):
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(SubjectsModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentsModel, on_delete=models.CASCADE)
    question = models.ForeignKey(ExamQuestionModel, on_delete=models.CASCADE)
    theory_answer = models.TextField(blank=True, null=True)
    subjective_answer = models.CharField(max_length=200, blank=True, null=True)
    objective_answer = models.ForeignKey(ExamQuestionOptionModel, on_delete=models.SET_NULL, blank=True, null=True)
    score = models.FloatField(null=True, blank=True)
    correct_answer = models.BooleanField(null=True, blank=True)
    marked = models.BooleanField(blank=True, default=False)






     














