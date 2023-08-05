from django.forms import ModelForm, Select, TextInput, DateInput
from student.models import ParentsModel, StudentsModel, StudentSettingModel
from school_utility.models import *


class ParentForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ParentsModel
        fields = '__all__'
        exclude = []
        widgets = {
            'date_of_birth': DateInput(attrs={
                'type': 'date'
            }),
        }


class ParentEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ParentsModel
        fields = '__all__'
        exclude = ['type', 'user', 'parent_id']
        widgets = {
            'date_of_birth': DateInput(attrs={
                'type': 'date'
            }),
        }


class StudentForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['transport_route'].queryset = TransportRouteModel.objects.filter(type=division).order_by('name')
            self.fields['transport_vehicle'].queryset = TransportVehicleModel.objects.filter(type=division).order_by(
                'vehicle_id')

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = StudentsModel
        fields = '__all__'
        exclude = []
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            }),
            'date_of_birth': TextInput(attrs={
                'type': 'date',
                'class': 'form-control',
            })
        }


class StudentEditForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['transport_route'].queryset = TransportRouteModel.objects.filter(type=division).order_by('name')
            self.fields['transport_vehicle'].queryset = TransportVehicleModel.objects.filter(type=division).order_by(
                'vehicle_id')

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = StudentsModel
        exclude = ['type', 'user', 'status', 'parent', 'registration_number']
        widgets = {
            'school': TextInput(attrs={
                'class': 'form-control',
            }),
            'date_of_birth': TextInput(attrs={
                'type': 'date',
                'class': 'form-control',
            })
        }


class StudentSettingCreateForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            if 0:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = StudentSettingModel
        fields = '__all__'

        widgets = {

        }


class StudentSettingEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            if 0:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = StudentSettingModel
        exclude = ['type', 'user']

        widgets = {

        }

