from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from library.models import *
from django.contrib.auth.models import User
from user_management.models import UserProfileModel
from school_setting.models import SchoolAcademicInfoModel


def generate_book_id(type):
    setting = SchoolSettingModel.objects.first()
    if setting.general_info.school_type == 'mix' and setting.general_info.separate_school_section:
        last_book = BookIDGeneratorModel.objects.filter(type=type).last()
    else:
        last_book = BookIDGeneratorModel.objects.filter().last()
    if last_book:
        book_id = str(int(last_book.last_id) + 1)
    else:
        book_id = str(1)
    while True:
        gen_id = book_id
        if setting.general_info.school_type == 'mix':
            book_id = type[0] + 'buc' + '-' + book_id.rjust(8, '0')
        else:
            book_id = 'buc' + '-' + book_id.rjust(8, '0')
        book_exist = BookCopyModel.objects.filter(copy_id=book_id).first()
        if not book_exist:
            break
        else:
            book_id = str(int(gen_id) + 1)

    generate_id = BookIDGeneratorModel.objects.create(last_id=gen_id, last_book_id=book_id, type=type)
    generate_id.save()

    return book_id


@receiver(post_save, sender=BookModel)
def create_book_copies(sender, instance, created, **kwargs):
    if created:
        book = instance
        type = book.type
        number_of_instance = book.initial_copies
        for num in range(number_of_instance):
            copy_id = generate_book_id(type)
            book_copy = BookCopyModel.objects.create(book=book, copy_id=copy_id, status='available', type=type,
                                                     user=book.user)
            book_copy.save()
