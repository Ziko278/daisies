from django.db import models
from django.contrib.auth.models import User


class FrontEndPages(models.Model):
    name = models.CharField(max_length=30)


class FrontEndSettingModel(models.Model):
    template = models.CharField(max_length=100)
    main_color = models.CharField(max_length=20, null=True)
    auxiliary_color = models.CharField(max_length=20, null=True)
    STATUS = (('active', 'ACTIVE'), ('maintenance', 'MAINTENANCE'))
    status = models.CharField(max_length=20, choices=STATUS)
    active_pages = models.ManyToManyField(FrontEndPages, blank=True)
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='frontend_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


class HomePageInfoModel(models.Model):
    pass


class FrontSliderModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='frontend/slider')
    second_image = models.FileField(upload_to='frontend/slider', null=True, blank=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    BUTTON_LINK = (
        ('homepage', 'HOME PAGE'), ('about', 'ABOUT'), ('contact_us', 'CONTACT'), ('gallery', 'GALLERY'),
        ('staff', 'OUR STAFF')
    )
    button_link = models.CharField(max_length=10, choices=BUTTON_LINK, null=True, blank=True)
    STATUS = (('active', 'ACTIVE'), ('inactive', 'INACTIVE'))
    status = models.CharField(max_length=20, choices=STATUS, default='active')
    TYPE = (
        ('pri', 'PRIMARY'), ('sec', 'SECONDARY'), ('mix', 'GENERAL')
    )
    type = models.CharField(max_length=10, choices=TYPE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='slider_updated_by')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
