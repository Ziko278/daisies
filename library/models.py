import datetime
from django.db import models
from django.contrib.auth.models import User
from school_setting.models import SchoolSettingModel, SessionModel
from student.models import StudentsModel
from academic.models import *
from datetime import datetime, timedelta, date
from school_setting.models import SchoolAcademicInfoModel
from student.models import StudentsModel
from human_resource.models import StaffModel
from school_setting.models import SchoolGeneralInfoModel


class BookCategoryModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='book_category_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'type'],
                name='unique_book_category_name_type_combo',
                violation_error_message='Book Category Already Exists'
            )
        ]


class BookAuthorModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='book_author_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()


class BookModel(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(BookCategoryModel, on_delete=models.CASCADE)
    author = models.ForeignKey(BookAuthorModel, on_delete=models.SET_NULL, null=True, blank=True)
    isbn = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cover_page = models.FileField(upload_to='library/book', blank=True, null=True)
    initial_copies = models.IntegerField()
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='book_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'isbn', 'type'],
                name='unique_book_name_type_combo',
                violation_error_message='Book Already Exists'
            )
        ]

    def total_copies(self):
        return BookCopyModel.objects.filter(book=self).count()

    def available_copies(self):
        return BookCopyModel.objects.filter(book=self, status='available').count()

    def borrowed_copies(self):
        return BookCopyModel.objects.filter(book=self, status='borrowed').count()

    def damaged_copies(self):
        return BookCopyModel.objects.filter(book=self, status='damaged').count()


class BookCopyModel(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, blank=True, null=True, related_name='copies')
    copy_id = models.CharField(max_length=100)
    STATUS = (
        ('available', 'AVAILABLE'), ('borrowed', 'BORROWED'), ('damaged', 'DAMAGED'), ('maintenance', 'MAINTENANCE'))
    status = models.CharField(max_length=100, choices=STATUS)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.book.name.upper()

    def borrower(self):
        borrow = BookBorrowModel.objects.filter(book=self, status='active').last()
        if borrow:
            return borrow.student


class PDFBookModel(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(BookCategoryModel, on_delete=models.CASCADE)
    author = models.ForeignKey(BookAuthorModel, on_delete=models.SET_NULL, null=True, blank=True)
    pdf_file = models.FileField(upload_to='library/pdf')
    description = models.TextField(null=True, blank=True)
    cover_page = models.FileField(upload_to='library/pdf', blank=True, null=True)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='pdf_book_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()


class EBookModel(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(BookCategoryModel, on_delete=models.CASCADE)
    author = models.ForeignKey(BookAuthorModel, on_delete=models.SET_NULL, blank=True, null=True)
    e_file = models.FileField(upload_to='library/e-book')
    description = models.TextField(null=True, blank=True)
    cover_page = models.FileField(upload_to='library/e-book', blank=True, null=True)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='e_book_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name.upper()


class BookBorrowModel(models.Model):
    book = models.ForeignKey(BookCopyModel, on_delete=models.CASCADE, blank=True, null=True, related_name='borrowed_book')
    student = models.ForeignKey(StudentsModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='student_borrowed_book')
    staff = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True)
    date_returned = models.DateTimeField(blank=True, null=True)
    STATUS = (('active', 'ACTIVE'), ('returned', 'RETURNED'), ('overdue', 'OVERDUE'))
    charge = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)

    def book_fine(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            library_setting = LibrarySettingModel.objects.filter(type=self.type).first()
        else:
            library_setting = LibrarySettingModel.objects.first()
        if self.due_date < date.today():
            return (date.today() - self.due_date).days * library_setting.charges_per_overdue_day
        return 0.0

    def is_due(self):
        if self.due_date < date.today():
            return True
        return False

    def due_days(self):
        if self.due_date < date.today():
            return (date.today() - self.due_date).days
        return 0


class DamagedBookModel(models.Model):
    book = models.ForeignKey(BookCopyModel, on_delete=models.CASCADE)
    reason = models.TextField()
    student = models.ForeignKey(StudentsModel, on_delete=models.SET_NULL, null=True, blank=True)
    staff = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class BookIDGeneratorModel(models.Model):
    last_id = models.IntegerField()
    last_book_id = models.CharField(max_length=100, null=True, blank=True)

    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True)


class LibrarySettingModel(models.Model):
    max_book_return_days = models.IntegerField(default=5)
    max_book = models.IntegerField(default=2)
    charges_per_overdue_day = models.FloatField(default=0)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='library_setting_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
