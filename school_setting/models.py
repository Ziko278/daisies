from django.db import models


class SessionModel(models.Model):
    start_year = models.FloatField()
    end_year = models.FloatField()
    DELIMETER = (('-', '-'), ('/', '/'))
    delimeter = models.CharField(max_length=1, choices=DELIMETER)
    SessionStatus = (
        ('a', 'ACTIVE'), ('p', 'PAST'), ('n', 'NEXT')
    )
    status = models.CharField(max_length=1, choices=SessionStatus)

    def __str__(self):
        return str(self.start_year) + self.delimeter + str(self.end_year)


class SchoolAcademicInfoModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE)
    TERM = (
        ('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')
    )
    term = models.CharField(max_length=10, choices=TERM)
    next_resumption_date = models.DateField(null=True, blank=True)


class TermRecordModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE)
    TERM = (
        ('1st term', '1st TERM'), ('2nd term', '2nd TERM'), ('3rd term', '3rd TERM')
    )
    term = models.CharField(max_length=10, choices=TERM)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    no_of_students = models.FloatField()
    no_of_staff = models.FloatField()
    no_of_parents = models.FloatField()


class SchoolGeneralInfoModel(models.Model):
    name = models.CharField(max_length=100)
    SCHOOL_TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'MIXED')
    )
    school_type = models.CharField(max_length=200, choices=SCHOOL_TYPE)
    logo = models.FileField(upload_to='images/logo')
    mobile_1 = models.CharField(max_length=20)
    mobile_2 = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)


class SchoolSettingModel(models.Model):
    general_info = models.ForeignKey(SchoolGeneralInfoModel, on_delete=models.CASCADE)
    academic_info = models.ForeignKey(SchoolAcademicInfoModel, on_delete=models.SET_NULL, null=True, blank=True)