from django.forms import ModelForm, Select, TextInput, DateInput, CheckboxSelectMultiple
from exam.models import *


class ExamForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ExamModel
        fields = '__all__'
        widgets = {
            'start_date': TextInput(attrs={
                'type': 'date'
            }),
            'end_date': TextInput(attrs={
                'type': 'date'
            }),
        }


class ExamEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ExamModel
        exclude = ['type', 'session', 'term']
        widgets = {
            'start_date': TextInput(attrs={
                'type': 'date'
            }),
            'end_date': TextInput(attrs={
                'type': 'date'
            }),

        }


class ExamTimeTableForm(ModelForm):
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
        model = ExamTimeTableModel
        fields = '__all__'
        widgets = {
            'start_date': TextInput(attrs={
                'type': 'date'
            }),
            'end_date': TextInput(attrs={
                'type': 'date'
            }),
            'student_class': CheckboxSelectMultiple(attrs={
                'checked': 'checked'
            }),

            'class_section': CheckboxSelectMultiple(attrs={
                'checked': 'checked'
            }),

            'date': TextInput(attrs={
                'type': 'date'
            }),
            'start_time': TextInput(attrs={
                'type': 'time'
            }),
            'end_time': TextInput(attrs={
                'type': 'time'
            })
        }


class ExamTimeTableEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ExamTimeTableModel
        exclude = ['type', 'session', 'term']
        widgets = {
            'start_date': TextInput(attrs={
                'type': 'date'
            }),
            'end_date': TextInput(attrs={
                'type': 'date'
            }),
            'student_class': CheckboxSelectMultiple(attrs={
                'checked': 'checked'
            }),

            'class_section': CheckboxSelectMultiple(attrs={
                'checked': 'checked'
            }),

            'date': TextInput(attrs={
                'type': 'date'
            }),
            'start_time': TextInput(attrs={
                'type': 'time'
            }),
            'end_time': TextInput(attrs={
                'type': 'time'
            })

        }


class ExamQuestionForm(ModelForm):
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
        model = ExamQuestionModel
        fields = '__all__'
        widgets = {
            'start_date': TextInput(attrs={
                'type': 'date'
            }),
        }


class ExamQuestionEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ExamQuestionModel
        exclude = ['type', 'session', 'term']
        widgets = {
            'start_date': TextInput(attrs={
                'type': 'date'
            }),

        }


class ExamQuestionAnswerForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ExamQuestionModel
        fields = ['correct_option']
        widgets = {

        }


class ExamQuestionOptionForm(ModelForm):
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
        model = ExamQuestionOptionModel
        fields = '__all__'
        widgets = {
            'start_date': TextInput(attrs={
                'type': 'date'
            }),
        }