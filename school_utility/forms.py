from django.forms import ModelForm, Select, TextInput, DateInput, CheckboxSelectMultiple
from school_utility.models import *


class HostelForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['student_class'].queryset = ClassesModel.objects.filter(type=division)
            self.fields['class_section'].queryset = ClassSectionModel.objects.filter(type=division)

        for field in self.fields:
            if field != 'student_class' and field != 'class_section':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = HostelModel
        fields = '__all__'
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            })
        }


class HostelEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['student_class'].queryset = ClassesModel.objects.filter(type=division)
            self.fields['class_section'].queryset = ClassSectionModel.objects.filter(type=division)

        for field in self.fields:
            if field != 'student_class' and field != 'class_section':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = HostelModel
        exclude = ['type', 'user', 'hostel_rep', 'assistant_hostel_rep']
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            })
        }


class HostelRepEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'student_class' and field != 'class_section':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = HostelModel
        fields = ['hostel_rep', 'assistant_hostel_rep', 'updated_by']
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            })
        }


class HostelRoomForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['student_class'].queryset = ClassesModel.objects.filter(type=division)
            self.fields['class_section'].queryset = ClassSectionModel.objects.filter(type=division)
            self.fields['hostel'].queryset = HostelModel.objects.filter(type=division)
        for field in self.fields:
            if field != 'student_class' and field != 'class_section':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = HostelRoomModel
        fields = '__all__'
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            })
        }


class HostelRoomEditForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['student_class'].queryset = ClassesModel.objects.filter(type=division)
            self.fields['class_section'].queryset = ClassSectionModel.objects.filter(type=division)
            self.fields['hostel'].queryset = HostelModel.objects.filter(type=division)

        for field in self.fields:
            if field != 'student_class' and field != 'class_section':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = HostelRoomModel
        exclude = ['type', 'room_rep', 'assistant_room_rep', 'user']
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            })
        }


class HostelRoomRepForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = HostelRoomModel
        fields = ['room_rep', 'assistant_room_rep', 'updated_by']
        widgets = {

        }


class HostelBedForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = HostelBedModel
        fields = '__all__'
        widgets = {

        }


class HostelBedEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = HostelBedModel
        exclude = ['type', 'user']
        widgets = {

        }


class TransportRouteForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = TransportRouteModel
        fields = '__all__'
        widgets = {

        }


class TransportRouteEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = TransportRouteModel
        exclude = ['type', 'user']
        widgets = {

        }


class TransportPathForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = TransportPathModel
        fields = '__all__'
        widgets = {

        }


class TransportPathEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = TransportPathModel
        exclude = ['route', 'type', 'user']
        widgets = {

        }


class TransportVehicleForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['driver'].queryset = SchoolUtilitySettingModel.objects.filter(
                type=division).first().drivers.all()
        else:
            self.fields['driver'].queryset = SchoolUtilitySettingModel.objects.first().drivers.all()
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = TransportVehicleModel
        fields = '__all__'
        widgets = {

        }


class TransportVehicleEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['driver'].queryset = SchoolUtilitySettingModel.objects.filter(
                type=division).first().drivers.all()
        else:
            self.fields['driver'].queryset = SchoolUtilitySettingModel.objects.first().drivers.all()

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = TransportVehicleModel
        exclude = ['type', 'user', 'state']
        widgets = {

        }


class SchoolUtilitySettingCreateForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['drivers'].queryset = StaffModel.objects.filter(type=division)
        for field in self.fields:
            if field != 'drivers':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = SchoolUtilitySettingModel
        fields = '__all__'

        widgets = {
            'drivers': CheckboxSelectMultiple(attrs={

            }),
        }


class SchoolUtilitySettingEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['drivers'].queryset = StaffModel.objects.filter(type=division)
        for field in self.fields:
            if field != 'drivers':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = SchoolUtilitySettingModel
        exclude = ['type', 'user']

        widgets = {
            'drivers': CheckboxSelectMultiple(attrs={

            }),
        }

