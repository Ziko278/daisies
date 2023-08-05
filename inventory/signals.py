from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from inventory.models import *
from django.contrib.auth.models import User
from school_setting.models import SchoolAcademicInfoModel
from communication.models import RecentActivityModel


@receiver(post_save, sender=InventoryStockModel)
def update_inventory_quantity(sender, instance, created, **kwargs):
    if created:
        stock = instance
        item = stock.item
        item.quantity += stock.quantity
        item.save()

        category = 'inventory_stock'
        subject = "<b>{} unit of {}</b> stocked just stocked in".format(stock.quantity,
                                                                        item.name.title())
        activity = RecentActivityModel.objects.create(category=category, subject=subject, reference_id=instance.id)
        activity.save()
