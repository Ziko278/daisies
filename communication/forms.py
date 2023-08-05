from django.forms import ModelForm, Select, TextInput, DateInput, CheckboxSelectMultiple
from communication.models import *


class SMTPConfigurationForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SMTPConfigurationModel
        fields = '__all__'
        widgets = {
            'password': TextInput(attrs={
                'type': 'password'
            })
        }


class SMTPConfigurationEditForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SMTPConfigurationModel
        exclude = ['type', 'user']
        widgets = {
            'password': TextInput(attrs={
                'type': 'password'
            })
        }


class SMSConfigurationForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SMSConfigurationModel
        fields = '__all__'
        widgets = {

        }


class SMSConfigurationEditForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SMSConfigurationModel
        exclude = ['type', 'user']
        widgets = {

        }


class MessageForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = MessageModel
        fields = '__all__'
        widgets = {

        }


class MessageEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = MessageModel
        exclude = ['type', 'user']
        widgets = {

        }


class SentMessageForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SentMessageModel
        fields = '__all__'
        widgets = {

        }


class SentMessageEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SentMessageModel
        exclude = ['type', 'user']
        widgets = {

        }


