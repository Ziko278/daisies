from django.db import models
from django.contrib.auth.models import User
from school_setting.models import SchoolSettingModel, SessionModel, SchoolGeneralInfoModel
from student.models import StudentsModel
from finance.models import FeeMasterModel
from academic.models import *
from datetime import date
from school_setting.models import SchoolAcademicInfoModel


class InventorySupplierModel(models.Model):
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    contact_name = models.CharField(max_length=250, null=True, blank=True)
    contact_phone_number = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)

    STATUS = (
        ('active', 'ACTIVE'), ('inactive', 'INACTIVE')
    )
    status = models.CharField(max_length=10, choices=STATUS)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='supplier_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()


class InventoryCategoryModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='inventory_category_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()


class InventoryItemModel(models.Model):
    category = models.ForeignKey(InventoryCategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    quantity = models.FloatField(null=True, blank=True, default=0)
    selling_price = models.FloatField(null=True, blank=True, default=0)
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='inventory_item_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()


class InventoryStockModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE, blank=True)
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2ndTerm'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM, blank=True)
    item = models.ForeignKey(InventoryItemModel, on_delete=models.CASCADE, related_name='stock_list')
    supplier = models.ForeignKey(InventorySupplierModel, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.FloatField()
    quantity_left = models.FloatField(blank=True)
    unit_cost = models.FloatField()
    unit_selling = models.FloatField()
    date = models.DateField(blank=True, default=date.today())
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='inventory_stock_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=self.type).first()
        else:
            academic_info = SchoolAcademicInfoModel.objects.first()
        self.session = academic_info.session
        self.term = academic_info.term
        self.item.selling_price = self.unit_selling
        self.item.save()
        if not self.quantity_left:
            self.quantity_left = self.quantity
        super(InventoryStockModel, self).save(*args, **kwargs)


class InventoryAssignModel(models.Model):
    student_class = models.ManyToManyField(ClassesModel, blank=True)
    class_section = models.ManyToManyField(ClassSectionModel, blank=True)
    inventory = models.ForeignKey(InventoryItemModel, on_delete=models.CASCADE)
    quantity = models.FloatField()
    fee = models.ManyToManyField(FeeMasterModel, blank=True)
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2nd Term'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM, blank=True)
    is_mandatory = models.BooleanField(default=False)
    GENDER = (('male', 'MALE'), ('female', 'FEMALE'), ('both', 'BOTH'))
    gender = models.CharField(max_length=15, default='both', choices=GENDER)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='inventory_assign_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.inventory.name.title()

    def quantity_left(self):
        return self.inventory.quantity


class InventoryStockOutModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE, blank=True)
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2nd Term'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM, blank=True)
    item = models.ForeignKey(InventoryItemModel, on_delete=models.CASCADE)
    quantity = models.FloatField()
    student = models.ForeignKey(StudentsModel, on_delete=models.SET_NULL, null=True, blank=True)
    staff = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    date = models.DateTimeField(blank=True, default=date.today())
    MODE = (
        ('damage', 'DAMAGE'), ('assign', 'ASSIGN'), ('sale', 'SALE'), ('staff', 'STAFF')
    )
    mode = models.CharField(max_length=10, choices=MODE, blank=True, null=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='inventory_stock_out_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=self.type).first()
        else:
            academic_info = SchoolAcademicInfoModel.objects.first()
        self.session = academic_info.session
        self.term = academic_info.term

        super(InventoryStockOutModel, self).save(*args, **kwargs)


class InventoryStockOutSummaryModel(models.Model):
    items = models.ManyToManyField(InventoryStockOutModel, related_name='stock_out_summary')
    total_price = models.FloatField(null=True)
    session = models.ForeignKey(SessionModel, on_delete=models.CASCADE, blank=True)
    TERM = (
        ('1st term', '1st Term'), ('2nd term', '2nd Term'), ('3rd term', '3rd Term')
    )
    term = models.CharField(max_length=20, choices=TERM, blank=True)
    student = models.ForeignKey(StudentsModel, on_delete=models.SET_NULL, null=True, blank=True)
    staff = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(blank=True, default=date.today())
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='inventory_stock_out_summary_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            academic_info = SchoolAcademicInfoModel.objects.filter(type=self.type).first()
        else:
            academic_info = SchoolAcademicInfoModel.objects.first()
        self.session = academic_info.session
        self.term = academic_info.term

        super(InventoryStockOutSummaryModel, self).save(*args, **kwargs)


class AssetCategoryModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='asset_category_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()


class AssetModel(models.Model):
    category = models.ForeignKey(AssetCategoryModel, on_delete=models.CASCADE)
    ASSET_TYPE = (
        ('fixed', 'FIXED'), ('movable', 'MOVABLE')
    )
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPE)
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    quantity = models.FloatField()
    worth = models.FloatField()
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='asset_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()



