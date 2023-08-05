from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Select, TextInput, RadioSelect, CheckboxInput, CheckboxSelectMultiple, DateInput
from django.contrib.auth.models import User
from academic.models import ClassesModel, ClassSectionModel
from django import forms
from django.core.exceptions import ValidationError
from inventory.models import *


class InventorySupplierForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventorySupplierModel
        fields = '__all__'

        widgets = {

        }


class InventorySupplierEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventorySupplierModel
        exclude = ['user', 'type']

        widgets = {

        }


class InventoryCategoryForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventoryCategoryModel
        fields = '__all__'

        widgets = {

        }


class InventoryCategoryEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventoryCategoryModel
        exclude = ['user', 'type']

        widgets = {

        }


class InventoryItemForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['category'].queryset = InventoryCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventoryItemModel
        fields = '__all__'

        widgets = {

        }


class InventoryItemEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['category'].queryset = InventoryCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventoryItemModel
        exclude = ['user', 'type']

        widgets = {

        }


class InventoryStockForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['supplier'].queryset = InventorySupplierModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventoryStockModel
        fields = '__all__'

        widgets = {
            'date': DateInput(attrs={
                'type': 'date'
            })
        }


class InventoryStockEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['supplier'].queryset = InventorySupplierModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventoryStockModel
        exclude = ['user', 'type']

        widgets = {
            'date': DateInput(attrs={
                'type': 'date'
            })
        }


class InventoryAssignForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['class_section'].queryset = ClassSectionModel.objects.filter(type=division).order_by('name')
            self.fields['student_class'].queryset = ClassesModel.objects.filter(type=division).order_by('name')
            self.fields['inventory'].queryset = InventoryItemModel.objects.filter(type=division).order_by('name')
            self.fields['fee'].queryset = FeeMasterModel.objects.filter(type=division).order_by('fee__name')

        for field in self.fields:
            if field != 'is_mandatory' and field != 'fee' and field != 'class_section' and field != 'student_class':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = InventoryAssignModel
        fields = '__all__'

        widgets = {
            'is_mandatory': CheckboxInput(attrs={

            }),
            'fee': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            }),

            'student_class': CheckboxSelectMultiple(attrs={

            })
        }


class InventoryAssignEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['class_section'].queryset = ClassSectionModel.objects.filter(type=division).order_by('name')
            self.fields['student_class'].queryset = ClassesModel.objects.filter(type=division).order_by('name')
            self.fields['inventory'].queryset = InventoryItemModel.objects.filter(type=division).order_by('name')
            self.fields['fee'].queryset = FeeMasterModel.objects.filter(type=division).order_by('fee__name')

        for field in self.fields:
            if field != 'is_mandatory' and field != 'fee' and field != 'class_section' and field != 'student_class':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = InventoryAssignModel
        exclude = ['user', 'type']

        widgets = {
            'fee': CheckboxSelectMultiple(attrs={

            }),
            'is_mandatory': CheckboxInput(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            }),

            'student_class': CheckboxSelectMultiple(attrs={

            })
        }


class InventoryStockOutForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventoryStockOutModel
        fields = '__all__'

        widgets = {
            'date': DateInput(attrs={
                'type': 'date'
            })
        }


class InventoryStockOutEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = InventoryStockOutModel
        exclude = ['user', 'type']

        widgets = {
            'date': DateInput(attrs={
                'type': 'date'
            })
        }


class AssetCategoryForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = AssetCategoryModel
        fields = '__all__'

        widgets = {

        }


class AssetCategoryEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = AssetCategoryModel
        exclude = ['user', 'type']

        widgets = {

        }


class AssetForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['category'].queryset = AssetCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = AssetModel
        fields = '__all__'

        widgets = {

        }


class AssetEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['category'].queryset = AssetCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = AssetModel
        exclude = ['user', 'type']

        widgets = {

        }
