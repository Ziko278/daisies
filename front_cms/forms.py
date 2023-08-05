from django.forms import ModelForm, Select, TextInput, DateInput, CheckboxSelectMultiple
from front_cms.models import *


class FrontSliderForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = FrontSliderModel
        fields = '__all__'
        widgets = {

        }


class FrontSliderEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = FrontSliderModel
        exclude = ['type', 'user']
        widgets = {

        }


