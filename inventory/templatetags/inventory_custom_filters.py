from django import template
from student.models import StudentsModel
from datetime import date, timedelta
from inventory.models import InventoryAssignModel, InventoryStockOutModel
from django.db.models import Sum
from school_setting.models import SchoolGeneralInfoModel, SchoolAcademicInfoModel
from finance.models import FeeModel, FeeMasterModel, FeePaymentModel

register = template.Library()


@register.filter
def inventory_is_collected(inventory_assign, student_id):
    student = StudentsModel.objects.get(pk=student_id)
    type = student.type
    school_setting = SchoolGeneralInfoModel.objects.first()
    if school_setting.separate_school_section:
        academic_info = SchoolAcademicInfoModel.objects.filter(type=type).first()
    else:
        academic_info = SchoolAcademicInfoModel.objects.first()
    item = inventory_assign.inventory
    quantity = inventory_assign.quantity

    item_collected = InventoryStockOutModel.objects.filter(item=item, student=student, term=academic_info.term,
                                                           session=academic_info.session, mode='assign')
    if not item_collected:
        return "not collected"
    quantity_collected = item_collected.aggregate(Sum('quantity'))['quantity__sum']

    if quantity_collected >= quantity:
        return "collected"
    return "part collected"


@register.filter
def inventory_left(inventory_assign, student_id):
    student = StudentsModel.objects.get(pk=student_id)
    type = student.type
    school_setting = SchoolGeneralInfoModel.objects.first()
    if school_setting.separate_school_section:
        academic_info = SchoolAcademicInfoModel.objects.filter(type=type).first()
    else:
        academic_info = SchoolAcademicInfoModel.objects.first()
    item = inventory_assign.inventory
    quantity = inventory_assign.quantity

    item_collected = InventoryStockOutModel.objects.filter(item=item, student=student, term=academic_info.term,
                                                           session=academic_info.session, mode='assign')
    if not item_collected:
        return quantity
    quantity_collected = item_collected.aggregate(Sum('quantity'))['quantity__sum']

    if quantity_collected >= quantity:
        return 0
    return quantity - quantity_collected


@register.filter
def inventory_verified(inventory_assign, student_id):
    student = StudentsModel.objects.get(pk=student_id)
    type = student.type
    school_setting = SchoolGeneralInfoModel.objects.first()
    if school_setting.separate_school_section:
        academic_info = SchoolAcademicInfoModel.objects.filter(type=type).first()
    else:
        academic_info = SchoolAcademicInfoModel.objects.first()
    session = academic_info.session
    term = academic_info.term
    item = inventory_assign.inventory
    fee_list = inventory_assign.fee.all()

    fee_paid = False
    if fee_list:
        for fee_master in fee_list:
            if fee_master.fee.fee_occurrence != 'termly':
                amount = fee_master.amount
            else:
                if fee_master.same_termly_price:
                    amount = fee_master.amount
                else:
                    if academic_info.term == '1st term':
                        amount = fee_master.first_term_amount
                    elif academic_info.term == '2nd term':
                        amount = fee_master.second_term_amount
                    elif academic_info.term == '3rd term':
                        amount = fee_master.third_term_amount

            fee_payment = FeePaymentModel.objects.filter(fee=fee_master, student=student, session=session, term=term)
            if not fee_payment:
                break
            amount_paid = fee_payment.aggregate(Sum('amount'))['amount__sum']
            if amount_paid < amount:
                break
        else:
            fee_paid = True
    else:
        fee_paid = True
    return fee_paid
