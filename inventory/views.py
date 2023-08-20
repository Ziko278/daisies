from django.db.models.aggregates import Sum
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import serializers
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from inventory.models import *
from inventory.forms import *
from student.models import StudentsModel
from school_setting.models import SchoolGeneralInfoModel


class InventorySupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = InventorySupplierModel
    permission_required = 'academic.add_classesmodel'
    form_class = InventorySupplierForm
    success_message = 'Inventory Supplier Added Successfully'
    template_name = 'inventory/supplier/index.html'

    def get_success_url(self):
        return reverse('inventory_supplier_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['inventory_supplier'] = InventorySupplierModel.objects.filter(
                type=self.request.user.profile.type).order_by(
                'name')
        else:
            context['inventory_supplier'] = InventorySupplierModel.objects.all().order_by('name')
        return context


class InventorySupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = InventorySupplierModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/supplier/index.html'
    context_object_name = "inventory_supplier_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return InventorySupplierModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return InventorySupplierModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InventorySupplierForm
        return context


class InventorySupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = InventorySupplierModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/supplier/detail.html'
    context_object_name = "inventory_supplier"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_list'] = InventoryStockModel.objects.filter(supplier=self.object)[:20]
        return context


class InventorySupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = InventorySupplierModel
    permission_required = 'academic.change_classsesmodel'
    form_class = InventorySupplierEditForm
    success_message = 'Inventory Supplier Updated Successfully'
    template_name = 'inventory/supplier/index.html'

    def get_success_url(self):
        return reverse('inventory_supplier_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['inventory_supplier'] = InventorySupplierModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['inventory_supplier'] = InventorySupplierModel.objects.all().order_by('name')
        return context


class InventorySupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = InventorySupplierModel
    permission_required = 'academic.delete_classesmodel'
    success_message = 'Inventory Supplier Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/supplier/delete.html'
    context_object_name = "inventory_supplier"

    def get_success_url(self):
        return reverse('inventory_supplier_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InventoryCategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = InventoryCategoryModel
    permission_required = 'academic.add_classesmodel'
    form_class = InventoryCategoryForm
    success_message = 'Inventory Category Added Successfully'
    template_name = 'inventory/category/index.html'

    def get_success_url(self):
        return reverse('inventory_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['inventory_category_list'] = InventoryCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['inventory_category_list'] = InventoryCategoryModel.objects.all().order_by('name')
        return context


class InventoryCategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = InventoryCategoryModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/category/index.html'
    context_object_name = "inventory_category_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return InventoryCategoryModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return InventoryCategoryModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InventoryCategoryForm
        return context


class InventoryCategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = InventoryCategoryModel
    permission_required = 'academic.change_classsesmodel'
    form_class = InventoryCategoryEditForm
    success_message = 'Inventory Category Updated Successfully'
    template_name = 'inventory/category/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['inventory_category'] = InventoryCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['inventory_category'] = InventoryCategoryModel.objects.all().order_by('name')
        return context

    def get_success_url(self):
        return reverse('inventory_category_index')


class InventoryCategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = InventoryCategoryModel
    permission_required = 'academic.delete_classesmodel'
    success_message = 'Inventory Category Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/category/delete.html'
    context_object_name = "inventory_category"

    def get_success_url(self):
        return reverse('inventory_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InventoryItemCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = InventoryItemModel
    permission_required = 'academic.add_classesmodel'
    form_class = InventoryItemForm
    success_message = 'Inventory Item Added Successfully'
    template_name = 'inventory/item/index.html'

    def get_success_url(self):
        return reverse('inventory_item_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['inventory_item_list'] = InventoryItemModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
            context['inventory_category_list'] = InventoryCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['inventory_item_list'] = InventoryItemModel.objects.all().order_by('name')
            context['inventory_category_list'] = InventoryCategoryModel.objects.all().order_by('name')
        return context

    def get_form_kwargs(self):
        kwargs = super(InventoryItemCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class InventoryItemListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = InventoryItemModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/item/index.html'
    context_object_name = "inventory_item_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return InventoryItemModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return InventoryItemModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            context['inventory_category_list'] = InventoryCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
            form_kwargs['type'] = self.request.user.profile.type
        else:
            context['inventory_category_list'] = InventoryCategoryModel.objects.all().order_by('name')

        context['form'] = InventoryItemForm(**form_kwargs)
        return context


class InventoryItemDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = InventoryItemModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/item/detail.html'
    context_object_name = "inventory_item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            context['inventory_category_list'] = InventoryCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
            form_kwargs['type'] = self.request.user.profile.type
        else:
            context['inventory_category_list'] = InventoryCategoryModel.objects.all().order_by('name')
        context['stock_form'] = InventoryStockForm(**form_kwargs)
        return context


class InventoryItemUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = InventoryItemModel
    permission_required = 'academic.change_classsesmodel'
    form_class = InventoryItemEditForm
    success_message = 'Inventory Item Updated Successfully'
    template_name = 'inventory/item/index.html'

    def get_success_url(self):
        return reverse('inventory_item_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['inventory_item_list'] = InventoryItemModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
            context['inventory_category_list'] = InventoryCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['inventory_item_list'] = InventoryItemModel.objects.all().order_by('name')
            context['inventory_category_list'] = InventoryCategoryModel.objects.all().order_by('name')
        return context


class InventoryItemDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = InventoryItemModel
    permission_required = 'academic.delete_classesmodel'
    success_message = 'Inventory Item Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/item/delete.html'
    context_object_name = "inventory_item"

    def get_success_url(self):
        return reverse('inventory_item_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InventoryStockCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = InventoryStockModel
    permission_required = 'academic.add_classesmodel'
    form_class = InventoryStockForm
    success_message = 'Inventory Stocked Successfully'
    template_name = 'inventory/item/detail.html'

    def get_success_url(self):
        return reverse('inventory_item_detail', kwargs={'pk': self.object.item.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['inventory_category_list'] = InventoryCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['inventory_category_list'] = InventoryCategoryModel.objects.all().order_by('name')

        return context

    def get_form_kwargs(self):
        kwargs = super(InventoryStockCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class InventoryStockListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = InventoryStockModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/stock/index.html'
    context_object_name = "inventory_stock_list"

    def get_queryset(self):
        session_id = self.request.GET.get('session')
        session = SessionModel.objects.get(pk=session_id)
        term = self.request.GET.get('term')
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return InventoryStockModel.objects.filter(type=self.request.user.profile.type, session=session,
                                                      term=term).order_by('id').reverse()
        else:
            return InventoryStockModel.objects.filter(session=session, term=term).order_by('id').reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_id = self.request.GET.get('session')
        session = SessionModel.objects.get(pk=session_id)
        term = self.request.GET.get('term')
        context['current_session'] = session
        context['session_list'] = SessionModel.objects.all()
        context['term'] = term
        return context


class InventoryStockDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = InventoryStockModel
    permission_required = 'academic.delete_classesmodel'
    success_message = 'Inventory Stock Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/stock/delete.html'
    context_object_name = "inventory_stock"

    def get_success_url(self):
        return reverse('inventory_item_detail', kwargs={'pk': self.get_object().item.pk})

    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.quantity != self.object.quantity_left:
            messages.error(self.request, 'Items in stock given out, stock can no longer be deleted')
            return redirect(reverse('inventory_item_detail', kwargs={'pk': self.object.item.id}))
        if self.request.method == 'POST':
            item = self.object.item
            item.quantity -= self.object.quantity
            item.save()
        return super(InventoryStockDeleteView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InventoryAssignCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = InventoryAssignModel
    permission_required = 'academic.add_classesmodel'
    form_class = InventoryAssignForm
    success_message = 'Inventory Item Assigned Successfully'
    template_name = 'inventory/assign/create.html'

    def get_success_url(self):
        return reverse('inventory_assign_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_form_kwargs(self):
        kwargs = super(InventoryAssignCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class InventoryAssignListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = InventoryAssignModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/assign/index.html'
    context_object_name = "inventory_assign_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return InventoryAssignModel.objects.filter(type=self.request.user.profile.type)
        else:
            return InventoryAssignModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InventoryAssignDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = InventoryAssignModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/assign/detail.html'
    context_object_name = "inventory_assign"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class InventoryAssignUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = InventoryAssignModel
    permission_required = 'academic.change_classsesmodel'
    form_class = InventoryAssignEditForm
    success_message = 'Inventory Item Assignment Updated Successfully'
    template_name = 'inventory/assign/edit.html'

    def get_success_url(self):
        return reverse('inventory_assign_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_form_kwargs(self):
        kwargs = super(InventoryAssignUpdateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class InventoryAssignDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = InventoryAssignModel
    permission_required = 'academic.delete_classesmodel'
    success_message = 'Inventory Item Assignment Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/assign/delete.html'
    context_object_name = "inventory_assign"

    def get_success_url(self):
        return reverse('inventory_assign_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InventorySelectStudentView(SuccessMessageMixin, TemplateView):
    template_name = 'inventory/stock_out/select_student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['class_list'] = ClassesModel.objects.filter(type=self.request.user.profile.type).order_by('name')
            student_list = StudentsModel.objects.filter(type=self.request.user.profile.type)
        else:
            context['class_list'] = ClassesModel.objects.all().order_by('name')
            student_list = StudentsModel.objects.all()
        context['student_list'] = serializers.serialize("json", student_list)
        return context


def stock_out_damaged_inventory(request, pk):
    stock = InventoryStockModel.objects.get(pk=pk)
    if stock.quantity_left <= 0:
        messages.error(request, 'Cannot Stock out of finished Stock')
        return redirect(reverse('inventory_item_detail', kwargs={'pk': stock.item.pk}))

    if request.method == 'POST':
        quantity = float(request.POST.get('quantity'))
        if stock.quantity_left < quantity:
            messages.error(request, 'Stock Out Quantity exceeds stock quantity left')
            return redirect(reverse('inventory_item_detail', kwargs={'pk': stock.item.pk}))

        reason = request.POST.get('reason')
        stock_out = InventoryStockOutModel.objects.create(item=stock.item, quantity=quantity, mode='damage',
                                                          reason=reason, type=request.user.profile.type,
                                                          user=request.user)
        stock_out.save()
        if stock_out.id:
            stock.quantity_left -= quantity
            stock.save()

            stock.item.quantity -= quantity
            stock.item.save()

            messages.success(request, '{} units stocked out successfully'.format(quantity))
        else:
            messages.success(request, 'An error occurred, Try Again')
        return redirect(reverse('inventory_item_detail', kwargs={'pk': stock.item.pk}))
    messages.error(request, 'Request Method not Supported')
    return redirect(reverse('inventory_item_detail', kwargs={'pk': stock.item.pk}))


def student_inventory_collect(request, pk):
    student = StudentsModel.objects.get(pk=pk)
    student_class = student.student_class
    class_section = student.class_section
    school_setting = SchoolGeneralInfoModel.objects.first()

    if school_setting.separate_school_section:
        academic_setting = SchoolAcademicInfoModel.objects.filter(type=request.user.profile.type).first()
    else:
        academic_setting = SchoolAcademicInfoModel.objects.first()

    if request.method == 'POST':
        form = InventoryStockOutForm(request.POST)
        if form.is_valid():
            stock_out = form.save()
            item = stock_out.item
            stock_out_quantity = stock_out.quantity
            stock_list = InventoryStockModel.objects.filter(item=item, quantity_left__gt=0)
            for stock in stock_list:
                if stock.quantity_left >= stock_out_quantity:
                    stock.quantity_left -= stock_out_quantity
                    stock.save()
                    item.quantity -= stock_out_quantity
                    item.save()
                    break
                else:
                    stock_out_quantity -= stock.quantity_left
                    item.quantity -= stock.quantity_left
                    item.save()
                    stock.quantity_left = 0
                    stock.save()

            if stock_out.mode == 'assign':
                messages.success(request, 'Items given to student successfully')
                return redirect(reverse('inventory_stock_out_detail', kwargs={'pk': stock_out.pk}))

    assigned_inventory_list = InventoryAssignModel.objects.filter(term=academic_setting.term,
                                                                  student_class__in=[student_class],
                                                                  class_section__in=[class_section]).filter(
                                                                  Q(gender='both') | Q(gender=student.gender))
    inventory_list = InventoryItemModel.objects.all()
    serialized_inventory_list = serializers.serialize("json", inventory_list)

    context = {
        'student': student,
        'assigned_inventory_list': assigned_inventory_list,
        'academic_setting': academic_setting,
        'form': InventoryStockOutForm,
        'inventory_list': inventory_list,
        'serialized_inventory_list': serialized_inventory_list
    }
    return render(request, 'inventory/stock_out/student_collect.html', context)


def student_inventory_bulk_collect(request, pk):
    student = StudentsModel.objects.get(pk=pk)
    student_class = student.student_class
    class_section = student.class_section
    school_setting = SchoolGeneralInfoModel.objects.first()

    if school_setting.separate_school_section:
        academic_setting = SchoolAcademicInfoModel.objects.filter(type=request.user.profile.type).first()
    else:
        academic_setting = SchoolAcademicInfoModel.objects.first()

    if request.method == 'POST':
        inventory_list = request.POST.getlist('product_id[]')
        quantity_bought_list = request.POST.getlist('quantity_input[]')

        grand_total = 0

        if len(inventory_list) == 0:
            messages.error(request, 'No Item was Selected')
            return redirect(reverse('inventory_student_collect', kwargs={'pk': student.id}))

        # form = InventoryStockOutForm(request.POST)
        summary = InventoryStockOutSummaryModel.objects.create(student=student, type=request.user.profile.type)
        summary.save()

        for num in range(len(inventory_list)):

            item = InventoryItemModel.objects.get(pk=inventory_list[num])
            stock_out_quantity = float(quantity_bought_list[num])
            unit_selling_price = item.selling_price
            total_price = unit_selling_price * stock_out_quantity

            grand_total += total_price
            stock_list = InventoryStockModel.objects.filter(item=item, quantity_left__gt=0)

            for stock in stock_list:
                stock_out = InventoryStockOutModel.objects.create(item=item, quantity=stock_out_quantity,
                                                                  student=student,
                                                                  mode='sale', type=request.user.profile.type,
                                                                  user=request.user)
                stock_out.save()
                summary.items.add(stock_out)
                summary.save()

                if stock.quantity_left >= stock_out_quantity:
                    stock.quantity_left -= stock_out_quantity
                    stock.save()
                    item.quantity -= stock_out_quantity
                    item.save()
                    break
                else:
                    stock_out_quantity -= stock.quantity_left
                    item.quantity -= stock.quantity_left
                    item.save()
                    stock.quantity_left = 0
                    stock.save()

        summary.total_price = grand_total
        summary.save()

        messages.success(request, 'Items given to student successfully')
        return redirect(reverse('inventory_stock_out_detail', kwargs={'pk': stock_out.pk}))

    assigned_inventory_list = InventoryAssignModel.objects.filter(term=academic_setting.term,
                                                                  student_class__in=[student_class],
                                                                  class_section__in=[class_section]).filter(
                                                                  Q(gender='both') | Q(gender=student.gender))
    inventory_list = InventoryItemModel.objects.all()
    serialized_inventory_list = serializers.serialize("json", inventory_list)

    context = {
        'student': student,
        'assigned_inventory_list': assigned_inventory_list,
        'academic_setting': academic_setting,
        'form': InventoryStockOutForm,
        'inventory_list': inventory_list,
        'serialized_inventory_list': serialized_inventory_list
    }
    return render(request, 'inventory/stock_out/student_collect.html', context)


def inventory_staff_select(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        school_setting = SchoolGeneralInfoModel.objects.first()

        if school_setting.separate_school_section:
            staff = StaffModel.objects.filter(staff_id=staff_id, type=request.user.profile.type).first()
        else:
            staff = StaffModel.objects.filter(staff_id=staff_id).first()
        if staff:
            return redirect(reverse('inventory_staff_bulk_collect', kwargs={'pk': staff.id}))
        else:
            messages.error(request, 'Staff with ID: {} not found'.format(staff_id))
            return redirect(reverse('inventory_select_staff'))

    return render(request, 'inventory/stock_out/select_staff.html')


def staff_inventory_bulk_collect(request, pk):
    staff = StaffModel.objects.get(pk=pk)
    school_setting = SchoolGeneralInfoModel.objects.first()

    if school_setting.separate_school_section:
        academic_setting = SchoolAcademicInfoModel.objects.filter(type=request.user.profile.type).first()
    else:
        academic_setting = SchoolAcademicInfoModel.objects.first()

    if request.method == 'POST':
        inventory_list = request.POST.getlist('product_id[]')
        quantity_bought_list = request.POST.getlist('quantity_input[]')

        grand_total = 0

        if len(inventory_list) == 0:
            messages.error(request, 'No Item was Selected')
            return redirect(reverse('inventory_staff_collect', kwargs={'pk': staff.id}))

        # form = InventoryStockOutForm(request.POST)
        summary = InventoryStockOutSummaryModel.objects.create(staff=staff, type=request.user.profile.type)
        summary.save()

        for num in range(len(inventory_list)):
            item = InventoryItemModel.objects.get(pk=inventory_list[num])
            stock_out_quantity = float(quantity_bought_list[num])
            unit_selling_price = item.selling_price
            total_price = unit_selling_price * stock_out_quantity

            grand_total += total_price
            stock_list = InventoryStockModel.objects.filter(item=item, quantity_left__gt=0)

            for stock in stock_list:
                stock_out = InventoryStockOutModel.objects.create(item=item, quantity=stock_out_quantity,
                                                                  staff=staff,
                                                                  mode='staff', type=request.user.profile.type,
                                                                  user=request.user)
                stock_out.save()

                if stock.quantity_left >= stock_out_quantity:
                    stock.quantity_left -= stock_out_quantity
                    stock.save()
                    item.quantity -= stock_out_quantity
                    item.save()
                    break
                else:
                    stock_out_quantity -= stock.quantity_left
                    item.quantity -= stock.quantity_left
                    item.save()
                    stock.quantity_left = 0
                    stock.save()

                summary.items.add(stock_out)
                summary.save()
        summary.total_price = grand_total
        summary.save()

        messages.success(request, 'Items given to staff successfully')
        return redirect(reverse('inventory_stock_out_detail', kwargs={'pk': stock_out.pk}))

    inventory_list = InventoryItemModel.objects.all()
    serialized_inventory_list = serializers.serialize("json", inventory_list)

    context = {
        'staff': staff,
        'academic_setting': academic_setting,
        'form': InventoryStockOutForm,
        'inventory_list': inventory_list,
        'serialized_inventory_list': serialized_inventory_list
    }
    return render(request, 'inventory/stock_out/staff_collect.html', context)


class InventoryStockOutListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = InventoryStockOutModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/stock_out/index.html'
    context_object_name = "inventory_stock_out_list"

    def get_queryset(self):
        session_id = self.request.GET.get('session')
        session = SessionModel.objects.get(pk=session_id)
        term = self.request.GET.get('term')
        mode = self.request.GET.get('mode')
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return InventoryStockOutModel.objects.filter(type=self.request.user.profile.type, session=session,
                                                         term=term, mode=mode).order_by('id').reverse()
        else:
            return InventoryStockOutModel.objects.filter(session=session, term=term, mode=mode).order_by('id').reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_id = self.request.GET.get('session')
        session = SessionModel.objects.get(pk=session_id)
        term = self.request.GET.get('term')
        mode = self.request.GET.get('mode')
        context['current_session'] = session
        context['session_list'] = SessionModel.objects.all()
        context['term'] = term
        context['mode'] = mode
        return context


class InventoryStockOutDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = InventoryStockOutModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/stock_out/detail.html'
    context_object_name = "inventory_stock_out"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class InventoryStockOutDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = InventoryStockOutModel
    permission_required = 'academic.delete_classesmodel'
    success_message = 'Inventory Stock Reversed Successfully'
    fields = '__all__'
    template_name = 'inventory/stock_out/delete.html'
    context_object_name = "inventory_stock"

    def get_success_url(self):
        return reverse('inventory_stock_out_list')

    def dispatch(self, *args, **kwargs):

        return super(InventoryStockOutDeleteView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AssetCategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = AssetCategoryModel
    permission_required = 'academic.add_classesmodel'
    form_class = AssetCategoryForm
    success_message = 'Asset Category Added Successfully'
    template_name = 'inventory/asset_category/index.html'

    def get_success_url(self):
        return reverse('asset_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['asset_category_list'] = AssetCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['asset_category_list'] = AssetCategoryModel.objects.all().order_by('name')
        return context


class AssetCategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = AssetCategoryModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/asset_category/index.html'
    context_object_name = "asset_category_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return AssetCategoryModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return AssetCategoryModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AssetCategoryForm
        return context


class AssetCategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AssetCategoryModel
    permission_required = 'academic.change_classsesmodel'
    form_class = AssetCategoryEditForm
    success_message = 'Asset Category Updated Successfully'
    template_name = 'inventory/asset_category/index.html'

    def get_success_url(self):
        return reverse('asset_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['asset_category_list'] = AssetCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['asset_category_list'] = AssetCategoryModel.objects.all().order_by('name')
        return context


class AssetCategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = AssetCategoryModel
    permission_required = 'academic.delete_classesmodel'
    success_message = 'Asset Category Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/asset_category/delete.html'
    context_object_name = "asset_category"

    def get_success_url(self):
        return reverse('asset_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AssetCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = AssetModel
    permission_required = 'academic.add_classesmodel'
    form_class = AssetForm
    success_message = 'Asset Added Successfully'
    template_name = 'inventory/asset/index.html'

    def get_success_url(self):
        return reverse('asset_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['asset_list'] = AssetModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
            context['asset_category_list'] = AssetCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['asset_list'] = AssetModel.objects.all().order_by('name')
            context['asset_category_list'] = AssetCategoryModel.objects.all().order_by('name')
        return context

    def get_form_kwargs(self):
        kwargs = super(AssetCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class AssetListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = AssetModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/asset/index.html'
    context_object_name = "asset_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return AssetModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return AssetModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            context['asset_category_list'] = AssetCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
            form_kwargs['type'] = self.request.user.profile.type
        else:
            context['asset_category_list'] = AssetCategoryModel.objects.all().order_by('name')

        context['form'] = AssetForm(**form_kwargs)
        return context


class AssetDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = AssetModel
    permission_required = 'academic.view_classesmodel'
    fields = '__all__'
    template_name = 'inventory/asset/detail.html'
    context_object_name = "asset"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            context['asset_category_list'] = AssetCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
            form_kwargs['type'] = self.request.user.profile.type
        else:
            context['asset_category_list'] = AssetCategoryModel.objects.all().order_by('name')
        # context['stock_form'] = InventoryStockForm(**form_kwargs)
        return context


class AssetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = AssetModel
    permission_required = 'academic.change_classsesmodel'
    form_class = AssetEditForm
    success_message = 'Asset Updated Successfully'
    template_name = 'inventory/asset/index.html'

    def get_success_url(self):
        return reverse('asset_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['asset_list'] = AssetModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
            context['asset_category_list'] = AssetCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['asset_list'] = AssetModel.objects.all().order_by('name')
            context['asset_category_list'] = AssetCategoryModel.objects.all().order_by('name')
        return context


class AssetDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = AssetModel
    permission_required = 'academic.delete_classesmodel'
    success_message = 'Asset Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/asset/delete.html'
    context_object_name = "asset"

    def get_success_url(self):
        return reverse('asset_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class InventoryDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'inventory/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_type = self.request.user.profile.type
        school_setting = SchoolGeneralInfoModel.objects.first()
        session_id = self.request.GET.get('session')
        session = SessionModel.objects.get(pk=session_id)
        term = self.request.GET.get('term')
        if school_setting.separate_school_section:
            inventory_list = InventoryItemModel.objects.filter(type=user_type)
            current_inventory_list = InventoryStockModel.objects.filter(type=user_type, session=session, term=term)
            damage_inventory_list = InventoryStockOutModel.objects.filter(type=user_type, mode='damage', session=session, term=term)
            asset_worth = AssetModel.objects.filter(type=self.request.user.profile.type).aggregate(Sum('worth'))['worth__sum']
        else:
            inventory_list = InventoryItemModel.objects.filter()
            current_inventory_list = InventoryStockModel.objects.filter(session=session, term=term)
            damage_inventory_list = InventoryStockOutModel.objects.filter(mode='damage', session=session, term=term)
            asset_worth = AssetModel.objects.filter(type=self.request.user.profile.type).aggregate(Sum('worth'))[
                'worth__sum']

        total_inventory_worth = 0
        for inventory in inventory_list:
            total_inventory_worth += inventory.quantity * inventory.selling_price

        current_inventory_worth = 0
        for inventory in current_inventory_list:
            current_inventory_worth += inventory.quantity * inventory.unit_cost

        context['current_session'] = session
        context['session_list'] = SessionModel.objects.all()
        context['term'] = term
        context['asset_worth'] = asset_worth if asset_worth else 0
        context['total_inventory_worth'] = total_inventory_worth
        context['current_inventory_worth'] = current_inventory_worth

        return context
