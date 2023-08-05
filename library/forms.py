from django.forms import ModelForm, Select, TextInput, DateInput, CheckboxSelectMultiple
from library.models import *


class BookCategoryForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = BookCategoryModel
        fields = '__all__'
        widgets = {

        }


class BookCategoryEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = BookCategoryModel
        exclude = ['type', 'user']
        widgets = {

        }


class BookAuthorForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = BookAuthorModel
        fields = '__all__'
        widgets = {

        }


class BookAuthorEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = BookAuthorModel
        exclude = ['type', 'user']
        widgets = {

        }


class BookForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['author'].queryset = BookAuthorModel.objects.filter(type=division).order_by('name')
            self.fields['category'].queryset = BookCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = BookModel
        fields = '__all__'
        widgets = {

        }


class BookEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['author'].queryset = BookAuthorModel.objects.filter(type=division).order_by('name')
            self.fields['category'].queryset = BookCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = BookModel
        exclude = ['initial_copies', 'type', 'user']
        widgets = {

        }


class EBookForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['author'].queryset = BookAuthorModel.objects.filter(type=division).order_by('name')
            self.fields['category'].queryset = BookCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = EBookModel
        fields = '__all__'
        widgets = {

        }


class EBookEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['author'].queryset = BookAuthorModel.objects.filter(type=division).order_by('name')
            self.fields['category'].queryset = BookCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = EBookModel
        exclude = ['type', 'user']
        widgets = {

        }


class PDFBookForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['author'].queryset = BookAuthorModel.objects.filter(type=division).order_by('name')
            self.fields['category'].queryset = BookCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = PDFBookModel
        fields = '__all__'
        widgets = {

        }


class PDFBookEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            self.fields['author'].queryset = BookAuthorModel.objects.filter(type=division).order_by('name')
            self.fields['category'].queryset = BookCategoryModel.objects.filter(type=division).order_by('name')
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    class Meta:
        model = PDFBookModel
        exclude = ['initial_copies', 'type', 'user']
        widgets = {

        }


class LibrarySettingCreateForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            if 1:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = LibrarySettingModel
        fields = '__all__'

        widgets = {

        }


class LibrarySettingEditForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        division = False
        if 'type' in kwargs.keys():
            division = kwargs.pop('type')

        super().__init__(*args, **kwargs)
        if division:
            pass
        for field in self.fields:
            if 1:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = LibrarySettingModel
        exclude = ['type', 'user']

        widgets = {

        }
