from django.db import models
from django.contrib.auth.models import User
from school_setting.models import SchoolSettingModel


class DepartmentModel(models.Model):
    """"""
    name = models.CharField(max_length=100)
    DEPT_TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=DEPT_TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'type'],
                name='unique_dept_name_type_combo'
            )
        ]

    def __str__(self):
        return self.name.upper()

    def save(self, *args, **kwargs):
        setting = SchoolSettingModel.objects.first()
        self.subject_type = setting.general_info.school_type

        super(DepartmentModel, self).save(*args, **kwargs)


class PositionModel(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.upper() + ' (' + self.department.name.upper() + ')'

    def staff_count(self, *args, **kwargs):
        return StaffModel.objects.filter(department=self.department).count()


class StaffModel(models.Model):
    """"""
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True, default='')
    last_name = models.CharField(max_length=50)

    image = models.FileField(upload_to='images/staff_images', blank=True, null=True)
    residential_address = models.CharField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    GENDER = (
        ('MALE', 'MALE'), ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=10, choices=GENDER)

    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    position = models.ForeignKey(PositionModel, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=50, blank=True, null=True)
    employment_date = models.DateTimeField(blank=True, null=True)
    cv = models.FileField(upload_to='staff/cv', null=True, blank=True)

    salary = models.BigIntegerField(blank=True, null=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    account_name = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.CharField(max_length=50, null=True, blank=True)

    referral_fullname = models.CharField(max_length=200, null=True, blank=True)
    referral_mobile = models.CharField(max_length=20, null=True, blank=True)
    referral_email = models.EmailField(null=True, blank=True)
    referral_address = models.CharField(max_length=200, null=True, blank=True)
    referral_office = models.TextField(max_length=200, null=True, blank=True)
    referral_image = models.FileField(upload_to='staff/referral', null=True, blank=True)

    blood_group = models.CharField(max_length=20, null=True, blank=True)
    genotype = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    health_issues = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=15, blank=True, default='active')
    SECTION = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    section = models.CharField(max_length=10, choices=SECTION, blank=True)

    def __str__(self):
        if self.middle_name:
            return self.surname + ' ' + self.middle_name + ' ' + self.last_name
        else:
            return self.surname + ' ' + self.last_name

    def save(self, *args, **kwargs):
        setting = SchoolSettingModel.objects.first()
        if setting.school_type != 'mix':
            if setting.school_type == 'pri':
                self.section = 'pri'
            if setting.school_type == 'sec':
                self.section = 'sec'

        if not self.staff_id:
            setting = SchoolSettingModel.objects.first()
            if setting.general_info.school_type == 'mix':
                last_staff = StaffModel.objects.filter(section=self.section).last()
                if last_staff:
                    staff_id = str(int(last_staff.id) + 1)
                else:
                    staff_id = str(1)
                staff_id = self.section + '-' + staff_id.rjust(8, '0')
            else:
                last_staff = StaffModel.objects.last()
                if last_staff:
                    staff_id = str(int(last_staff.id) + 1)
                else:
                    staff_id = str(1)
                staff_id = staff_id.rjust(8, '0')

            self.staff_id = staff_id

        super(StaffModel, self).save(*args, **kwargs)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['staff_id'],
                name='unique_staff_id'
            )
        ]
