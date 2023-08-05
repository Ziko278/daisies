from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TimeInput, TextInput, CheckboxInput, CheckboxSelectMultiple, DateInput
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from academic.models import *


class ClassSectionForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = ClassSectionModel
        fields = '__all__'

        widgets = {

        }


class ClassSectionEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'section':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = ClassSectionModel
        fields = ['name', 'updated_by']

        widgets = {

        }


class ClassCreateForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['section'].queryset = ClassSectionModel.objects.filter(type=division)
            self.fields['promotion_class'].queryset = ClassesModel.objects.filter(type=division)
        for field in self.fields:
            if field != 'section' and field != 'is_graduation_class':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = ClassesModel
        fields = '__all__'

        widgets = {
            'section': CheckboxSelectMultiple(attrs={

            })
        }


class ClassEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['section'].queryset = ClassSectionModel.objects.filter(type=division)
            self.fields['promotion_class'].queryset = ClassesModel.objects.filter(type=division)
        for field in self.fields:
            if field != 'section' and field != 'is_graduation_class':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = ClassesModel
        fields = ['name', 'code', 'result_type', 'section', 'is_graduation_class', 'promotion_class', 'updated_by']

        widgets = {
            'section': CheckboxSelectMultiple(attrs={

            })
        }


class SubjectCreateForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SubjectsModel
        fields = '__all__'

        widgets = {

        }


class SubjectEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = SubjectsModel
        fields = ['name', 'code', 'subject_type', 'updated_by']

        widgets = {

        }


class ClassSectionInfoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['subjects'].queryset = SubjectsModel.objects.filter(type=division).order_by('name')
        else:
            self.fields['subjects'].queryset = SubjectsModel.objects.all().order_by('name')
        for field in self.fields:
            if field != 'section' and field != 'subjects':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = ClassSectionInfoModel
        fields = '__all__'
        widgets = {
            'subjects': CheckboxSelectMultiple(attrs={

            })
        }


class ClassSectionInfoEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['subjects'].queryset = SubjectsModel.objects.filter(type=division).order_by('name')
        else:
            self.fields['subjects'].queryset = SubjectsModel.objects.all().order_by('name')
        for field in self.fields:
            if field != 'section' and field != 'subjects':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = ClassSectionInfoModel
        exclude = ['user', 'type', 'student_class', 'section']
        widgets = {
            'subjects': CheckboxSelectMultiple(attrs={

            })
        }


class ClassSectionSubjectTeacherForm(ModelForm):
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            # self.fields['subjects'].queryset = SubjectsModel.objects.filter(type=division).order_by('name')
            pass
        else:
            pass
            # self.fields['subjects'].queryset = SubjectsModel.objects.all().order_by('name')
        for field in self.fields:
            if field != 'class_section' and field != 'student_class' and field != 'teachers':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = ClassSectionSubjectTeacherModel
        fields = '__all__'
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            }),
            'teachers': CheckboxSelectMultiple(attrs={

            })
        }


class ClassSectionSubjectTeacherEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            # self.fields['subjects'].queryset = SubjectsModel.objects.filter(type=division).order_by('name')
            pass
        else:
            pass
            # self.fields['subjects'].queryset = SubjectsModel.objects.all().order_by('name')
        for field in self.fields:
            if field != 'class_section' and field != 'student_class':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = ClassSectionSubjectTeacherModel
        exclude = ['user', 'type', 'student_class', 'class_section']
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            }),
            'teachers': CheckboxSelectMultiple(attrs={

            })
        }


class ClassTimeTableForm(ModelForm):
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['subject'].queryset = SubjectsModel.objects.filter(type=division).order_by('name')
        else:
            self.fields['subject'].queryset = SubjectsModel.objects.all().order_by('name')
        for field in self.fields:
            if 1:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = ClassTimeTableModel
        fields = '__all__'
        widgets = {
            'start_time': TimeInput(attrs={
                'type': 'time'
            }),
            'stop_time': TimeInput(attrs={
                'type': 'time'
            })
        }


class ClassTimeTableEditForm(ModelForm):
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['subject'].queryset = SubjectsModel.objects.filter(type=division).order_by('name')
        else:
            self.fields['subject'].queryset = SubjectsModel.objects.all().order_by('name')
        for field in self.fields:
            if 1:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = ClassTimeTableModel
        exclude = ['user', 'type']
        widgets = {
            'start_time': TimeInput(attrs={
                'type': 'time'
            }),
            'stop_time': TimeInput(attrs={
                'type': 'time'
            })
        }


class AcademicSettingCreateForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['head_teacher'].queryset = StaffModel.objects.filter(type=division).order_by('surname')
        for field in self.fields:
            if field != 'active_days' and field != 'use_promotion_cutoff':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = AcademicSettingModel
        fields = '__all__'

        widgets = {
            'active_days': CheckboxSelectMultiple(attrs={

            })
        }


class AcademicSettingEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['head_teacher'].queryset = StaffModel.objects.filter(type=division).order_by('surname')
        for field in self.fields:
            if field != 'active_days' and field != 'use_promotion_cutoff':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = AcademicSettingModel
        exclude = ['type', 'user']

        widgets = {
            'active_days': CheckboxSelectMultiple(attrs={

            })
        }


class LessonNoteForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            if field != 'student_class' and field != 'class_section' and field != 'mid_term':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = LessonNoteModel
        fields = '__all__'
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            })
        }


class LessonNoteEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            if field != 'student_class' and field != 'class_section' and field != 'mid_term':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = LessonNoteModel
        exclude = ['type', 'user']
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            })
        }


class LessonDocumentForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            if field != 'student_class' and field != 'class_section' and field != 'mid_term':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = LessonDocumentModel
        fields = '__all__'
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            })
        }


class LessonDocumentEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            if field != 'student_class' and field != 'class_section' and field != 'mid_term':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = LessonDocumentModel
        exclude = ['type', 'user']
        widgets = {
            'student_class': CheckboxSelectMultiple(attrs={

            }),
            'class_section': CheckboxSelectMultiple(attrs={

            })
        }
