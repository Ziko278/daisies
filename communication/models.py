from django.db import models
from django.contrib.auth.models import User
from human_resource.models import StaffModel
from student.models import StudentsModel, ParentsModel
from school_setting.models import SchoolGeneralInfoModel, SessionModel, SchoolAcademicInfoModel


class RecentActivityModel(models.Model):
    category = models.CharField(max_length=100)
    subject = models.CharField(max_length=250)
    reference_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE, blank=True)
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2nd Term'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)

    def save(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=self.type).first()
        else:
            academic_info = SchoolAcademicInfoModel.objects.first()
        self.session = academic_info.session
        self.term = academic_info.term
        super(RecentActivityModel, self).save(*args, **kwargs)


class SMTPConfigurationModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    host = models.CharField(max_length=200)
    port = models.PositiveIntegerField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='smtp_config_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    STATUS = (
        ('active', 'ACTIVE'), ('inactive', 'INACTIVE')
    )
    status = models.CharField(max_length=20, choices=STATUS, default='active', blank=True)

    def __str__(self):
        return self.name.upper()


class SMSConfigurationModel(models.Model):
    name = models.CharField(max_length=200)
    PROVIDER = (('africastalking', 'AFRICASTALKING'), ('nexmo', 'NEXMO'))
    provider = models.CharField(max_length=200, choices=PROVIDER)
    api_key = models.CharField(max_length=200)
    secret_key = models.CharField(max_length=200)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='sms_config_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    STATUS = (
        ('active', 'ACTIVE'), ('inactive', 'INACTIVE')
    )
    status = models.CharField(max_length=20, choices=STATUS, default='active', blank=True)

    def __str__(self):
        return "{} - {}".format(self.name.upper(), self.provider.upper())


class CommunicationSettingModel(models.Model):
    default_smtp = models.ForeignKey(SMTPConfigurationModel, on_delete=models.SET_NULL, null=True, blank=True)
    default_sms = models.ForeignKey(SMSConfigurationModel, on_delete=models.SET_NULL, null=True, blank=True)
    auto_save_sent_message = models.BooleanField(default=False)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)


class MessageModel(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    SMS_TYPE = (
        ('plain', 'PLAIN'), ('multimedia', 'MULTIMEDIA')
    )
    sms_type = models.CharField(max_length=20, choices=SMS_TYPE, default='active', blank=True)
    attachment = models.FileField(upload_to='communication/message', null=True, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='message_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class SentMessageModel(models.Model):
    message = models.ForeignKey(MessageModel, on_delete=models.CASCADE)
    MEDIUM = (
        ('sms', 'SMS'), ('email', 'EMAIL')
    )
    medium = models.CharField(max_length=50, choices=MEDIUM)
    recipients = models.TextField(null=True, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class QueryModel(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    QUERY_TYPE = (
        ('plain', 'PLAIN'), ('multimedia', 'MULTIMEDIA')
    )
    query_type = models.CharField(max_length=20, choices=QUERY_TYPE, default='active', blank=True)
    FLOW = (
        ('incoming', 'INCOMING'), ('outgoing', 'OUTGOING')
    )
    flow = models.CharField(max_length=20, choices=FLOW, blank=True)
    RECIPIENT = (
        ('student', 'STUDENT'), ('staff', 'STAFF'), ('parent', 'PARENT')
    )
    recipient = models.CharField(max_length=10, choices=RECIPIENT, blank=True)
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(StudentsModel, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey(ParentsModel, on_delete=models.CASCADE, null=True, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class QueryFollowUpModel(models.Model):
    query = models.ForeignKey(QueryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    QUERY_TYPE = (
        ('plain', 'PLAIN'), ('multimedia', 'MULTIMEDIA')
    )
    query_type = models.CharField(max_length=20, choices=QUERY_TYPE, default='active', blank=True)
    FLOW = (
        ('incoming', 'INCOMING'), ('outgoing', 'OUTGOING')
    )
    flow = models.CharField(max_length=20, choices=FLOW, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class FrontDeskInfoModel(models.Model):
    opening_days = models.CharField(max_length=255, null=True, blank=True)
    opening_hours = models.CharField(max_length=255, null=True, blank=True)


class VisitorRecordModel(models.Model):
    parent = models.ForeignKey(ParentsModel, on_delete=models.SET_NULL, null=True, blank=True)
    visitor_name = models.CharField(max_length=200, blank=True)
    visitor_mobile = models.CharField(max_length=50, blank=True)
    purpose = models.CharField(max_length=50, blank=True)
    staff_to_see = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True)
    student_to_see = models.ForeignKey(StudentsModel, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True, blank=True)
    sign_in_time = models.TimeField(auto_now_add=True, blank=True)
    sign_out_time = models.TimeField(blank=True, null=True)
    STATUS = (
        ('signed in', 'SIGNED IN'), ('signed out', 'SIGNED OUT')
    )
    status = models.CharField(max_length=20, choices=STATUS, default='signed in', blank=True)


