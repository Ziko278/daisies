import ebooklib
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.db.models import Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from school_setting.models import SchoolGeneralInfoModel
from ebooklib import epub
import ebooklib
from library.models import *
from library.forms import *


def generate_book_id(type):
    setting = SchoolSettingModel.objects.first()
    if setting.general_info.school_type == 'mix' and setting.general_info.separate_school_section:
        last_book = BookIDGeneratorModel.objects.filter(type=type).last()
    else:
        last_book = BookIDGeneratorModel.objects.filter().last()
    if last_book:
        book_id = str(int(last_book.last_id) + 1)
    else:
        book_id = str(1)
    while True:
        gen_id = book_id
        if setting.general_info.school_type == 'mix':
            book_id = type[0] + 'buc' + '-' + book_id.rjust(8, '0')
        else:
            book_id = 'buc' + '-' + book_id.rjust(8, '0')
        book_exist = BookCopyModel.objects.filter(copy_id=book_id).first()
        if not book_exist:
            break
        else:
            book_id = str(int(gen_id) + 1)

    generate_id = BookIDGeneratorModel.objects.create(last_id=gen_id, last_book_id=book_id, type=type)
    generate_id.save()

    return book_id


class BookCategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = BookCategoryModel
    permission_required = 'finance.add_feemodel'
    form_class = BookCategoryForm
    success_message = 'Book Category Added Successfully'
    template_name = 'library/book_category/index.html'

    def get_success_url(self):
        return reverse('book_category_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['book_category_list'] = BookCategoryModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['book_category_list'] = BookCategoryModel.objects.all().order_by('name')
        context['form'] = BookCategoryForm
        return context


class BookCategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = BookCategoryModel
    permission_required = 'finance.view_feemodel'
    fields = '__all__'
    template_name = 'library/book_category/index.html'
    context_object_name = "book_category_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return BookCategoryModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return BookCategoryModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookCategoryForm
        return context


class BookCategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BookCategoryModel
    permission_required = 'finance.change_feemodel'
    form_class = BookCategoryEditForm
    success_message = 'Book Category Updated Successfully'
    template_name = 'library/book_category/index.html'

    def get_success_url(self):
        return reverse('book_category_index')
        # return reverse('fee_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_category'] = self.object

        return context


class BookCategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = BookCategoryModel
    permission_required = 'finance.delete_feemodel'
    success_message = 'Book Category Deleted Successfully'
    fields = '__all__'
    template_name = 'library/book_category/delete.html'
    context_object_name = "book_category"

    def get_success_url(self):
        return reverse("book_category_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookAuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = BookAuthorModel
    permission_required = 'finance.add_feemodel'
    form_class = BookAuthorForm
    success_message = 'Book Author Added Successfully'
    template_name = 'library/book_author/index.html'

    def get_success_url(self):
        return reverse('book_author_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['book_author_list'] = BookAuthorModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['book_author_list'] = BookAuthorModel.objects.all().order_by('name')
        context['form'] = BookAuthorForm
        return context


class BookAuthorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = BookAuthorModel
    permission_required = 'finance.view_feemodel'
    fields = '__all__'
    template_name = 'library/book_author/index.html'
    context_object_name = "book_author_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return BookAuthorModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return BookAuthorModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookAuthorForm
        return context


class BookAuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BookAuthorModel
    permission_required = 'finance.change_feemodel'
    form_class = BookAuthorEditForm
    success_message = 'Book Author Updated Successfully'
    template_name = 'library/book_author/index.html'

    def get_success_url(self):
        return reverse('book_author_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_author'] = self.object

        return context


class BookAuthorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = BookAuthorModel
    permission_required = 'finance.delete_feemodel'
    success_message = 'Book Author Deleted Successfully'
    fields = '__all__'
    template_name = 'library/book_author/delete.html'
    context_object_name = "book_author"

    def get_success_url(self):
        return reverse("book_author_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = BookModel
    permission_required = 'finance.add_feemodel'
    form_class = BookForm
    success_message = 'Book Added Successfully'
    template_name = 'library/book/index.html'

    def get_success_url(self):
        return reverse('book_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['book_list'] = BookModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['book_list'] = BookModel.objects.all().order_by('name')
        context['form'] = BookForm
        return context

    def get_form_kwargs(self):
        kwargs = super(BookCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = BookModel
    permission_required = 'finance.view_feemodel'
    fields = '__all__'
    template_name = 'library/book/index.html'
    context_object_name = "book_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return BookModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return BookModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            form_kwargs['type'] = self.request.user.profile.type

        context['form'] = BookForm(**form_kwargs)
        return context


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DetailView):
    model = BookModel
    permission_required = 'finance.delete_feemodel'
    fields = '__all__'
    template_name = 'library/book/detail.html'
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = BookModel
    permission_required = 'finance.change_feemodel'
    form_class = BookEditForm
    success_message = 'Book Updated Successfully'
    template_name = 'library/book/edit.html'

    def get_success_url(self):
        return reverse('book_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = self.object

        return context

    def get_form_kwargs(self):
        kwargs = super(BookUpdateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = BookModel
    permission_required = 'finance.delete_feemodel'
    success_message = 'Book Deleted Successfully'
    fields = '__all__'
    template_name = 'library/book/delete.html'
    context_object_name = "book"

    def get_success_url(self):
        return reverse("book_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def generate_book_copies(request, pk):
    if request.method == 'POST':
        book = BookModel.objects.get(pk=pk)
        number_of_copies = int(request.POST.get('copies'))
        if number_of_copies > 100:
            messages.warning(request, 'Maximum of 100 book copies can be generated at a time')
            return redirect(reverse('book_detail', kwargs={'pk': pk}))
        for num in range(number_of_copies):
            copy_id = generate_book_id(book.type)
            book_copy = BookCopyModel.objects.create(book=book, copy_id=copy_id, status='available', type=book.type,
                                                     user=book.user)
            book_copy.save()
        messages.success(request, '{} book copies of {} generated successfully'.format(number_of_copies,
                                                                                       book.name.title()))
        return redirect(reverse('book_detail', kwargs={'pk': pk}))

    messages.error(request, 'Method not supported, Try again')
    return redirect(reverse('book_detail', kwargs={'pk': pk}))


class BookCopyDetailView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DetailView):
    model = BookCopyModel
    permission_required = 'finance.delete_feemodel'
    fields = '__all__'
    template_name = 'library/book_copy/detail.html'
    context_object_name = "book_copy"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookCopyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = BookCopyModel
    permission_required = 'finance.delete_feemodel'
    success_message = 'Book Copy Deleted Successfully'
    fields = '__all__'
    template_name = 'library/book_copy/delete.html'
    context_object_name = "book_copy"

    def dispatch(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.status == 'borrowed':
            messages.error(self.request, 'Book is currently borrowed, mark book as returned to delete it')
            return redirect(reverse('book_copy_detail', kwargs={'pk': self.object.id}))
        return super(BookCopyDeleteView, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse("book_detail", kwargs={'pk': self.object.book.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def borrow_book(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        type = request.user.profile.type
        book_id = request.POST.get('book_id')
        book_copy = BookCopyModel.objects.filter(copy_id=book_id, type=type).first()
        student_id = request.POST.get('student_id')
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            library_setting = LibrarySettingModel.objects.filter(type=request.user.profile.type).first()
        else:
            library_setting = LibrarySettingModel.objects.filter().first()
        student = StudentsModel.objects.filter(registration_number=student_id, type=type).first()
        if not book_copy:
            messages.error(request, 'Book with ID {} not found, please check ID and try again'.format(book_id))
            return redirect(reverse('book_borrow'))

        if book_copy.status != 'available':
            messages.error(request, 'This book is not currently available')
            return redirect(reverse('book_borrow'))

        if not student:
            messages.error(request, 'Student with ID {} not found, please check ID and try again'.format(student_id))
            return redirect(reverse('book_borrow'))

        if action == 'confirm':
            context = {
                'student': student,
                'copy': book_copy
            }
            return render(request, 'library/book/confirm_borrow.html', context)
        elif action == 'confirmed':
            due_date = datetime.now().date() + timedelta(days=library_setting.max_book_return_days)
            borrow = BookBorrowModel.objects.create(book=book_copy, student=student, due_date=due_date, status='active',
                                                    user=request.user, type=student.type)
            borrow.save()
            if borrow.id:
                book_copy.status = 'borrowed'
                book_copy.save()
                messages.success(request, 'Book successfully borrowed, due on {}'.format(due_date))
                return redirect(reverse('book_borrow'))
            else:
                messages.error(request, 'Error Occurred, Try Later')
                return redirect(reverse('book_borrow'))
        else:
            messages.error(request, 'Unauthorized Action, please Retry')
            return redirect(reverse('book_borrow'))
    return render(request, 'library/book/borrow.html')


class BorrowedBookListView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = 'finance.change_feemodel'
    template_name = 'library/book/borrowed_books.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list'] = BookBorrowModel.objects.filter(type=self.request.user.profile.type).order_by('id').reverse()[:100]
        return context


def return_borrowed_book(request, pk):
    if request.method == 'POST':
        book_borrow = BookBorrowModel.objects.get(pk=pk)
        if book_borrow.status != 'active':
            messages.warning(request, 'Book Already Returned')
            return redirect(reverse('borrowed_books'))
        book_borrow.book.status = 'available'
        book_borrow.book.save()
        book_borrow.status = 'returned'
        book_borrow.charge = book_borrow.book_fine()
        book_borrow.date_returned = datetime.now()
        book_borrow.save()

        messages.success(request, 'Book Returned Successfully')
        return redirect(reverse('borrowed_books'))
    messages.error(request, 'method not allowed')
    return redirect(reverse('borrowed_books'))


class EBookCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = EBookModel
    permission_required = 'finance.add_feemodel'
    form_class = EBookForm
    success_message = 'E-Book Added Successfully'
    template_name = 'library/e_book/index.html'

    def get_success_url(self):
        return reverse('e_book_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['e_book_list'] = EBookModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['e_book_list'] = EBookModel.objects.all().order_by('name')
        context['form'] = EBookForm
        return context

    def get_form_kwargs(self):
        kwargs = super(EBookCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class EBookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = EBookModel
    permission_required = 'finance.view_feemodel'
    fields = '__all__'
    template_name = 'library/e_book/index.html'
    context_object_name = "e_book_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return EBookModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return EBookModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            form_kwargs['type'] = self.request.user.profile.type

        context['form'] = EBookForm(**form_kwargs)
        return context


class EBookDetailView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DetailView):
    model = EBookModel
    permission_required = 'finance.delete_feemodel'
    fields = '__all__'
    template_name = 'library/e_book/detail.html'
    context_object_name = "e_book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = epub.read_epub(self.object.e_file.path)
        content = ""

        for item in book.get_items():
            if item.get_type() == ebooklib.ITEM_DOCUMENT:
                item_content = item.get_content().decode('utf-8')
                content += item_content

        context['e_book_content'] = content
        return context


class EBookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = EBookModel
    permission_required = 'finance.change_feemodel'
    form_class = EBookEditForm
    success_message = 'E-Book Updated Successfully'
    template_name = 'library/e_book/edit.html'

    def get_success_url(self):
        return reverse('e_book_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['e_book'] = self.object

        return context

    def get_form_kwargs(self):
        kwargs = super(EBookUpdateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class EBookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = EBookModel
    permission_required = 'finance.delete_feemodel'
    success_message = 'E-Book Deleted Successfully'
    fields = '__all__'
    template_name = 'library/e_book/delete.html'
    context_object_name = "e_book"

    def get_success_url(self):
        return reverse("e_book_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PDFBookCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = PDFBookModel
    permission_required = 'finance.add_feemodel'
    form_class = PDFBookForm
    success_message = 'PDF Added Successfully'
    template_name = 'library/pdf_book/index.html'

    def get_success_url(self):
        return reverse('pdf_book_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            context['pdf_book_list'] = PDFBookModel.objects.filter(
                type=self.request.user.profile.type).order_by('name')
        else:
            context['pdf_book_list'] = PDFBookModel.objects.all().order_by('name')
        context['form'] = PDFBookForm
        return context

    def get_form_kwargs(self):
        kwargs = super(PDFBookCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class PDFBookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = PDFBookModel
    permission_required = 'finance.view_feemodel'
    fields = '__all__'
    template_name = 'library/pdf_book/index.html'
    context_object_name = "pdf_book_list"

    def get_queryset(self):
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            return PDFBookModel.objects.filter(type=self.request.user.profile.type).order_by('name')
        else:
            return PDFBookModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            form_kwargs['type'] = self.request.user.profile.type

        context['form'] = PDFBookForm(**form_kwargs)
        return context


class PDFBookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = PDFBookModel
    permission_required = 'finance.delete_feemodel'
    fields = '__all__'
    template_name = 'library/pdf_book/detail.html'
    context_object_name = "pdf_book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PDFBookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PDFBookModel
    permission_required = 'finance.change_feemodel'
    form_class = PDFBookEditForm
    success_message = 'PDF Updated Successfully'
    template_name = 'library/pdf_book/edit.html'

    def get_success_url(self):
        return reverse('pdf_book_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pdf_book'] = self.object

        return context

    def get_form_kwargs(self):
        kwargs = super(PDFBookUpdateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class PDFBookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = PDFBookModel
    permission_required = 'finance.delete_feemodel'
    success_message = 'PDF Deleted Successfully'
    fields = '__all__'
    template_name = 'library/pdf_book/delete.html'
    context_object_name = "pdf_book"

    def get_success_url(self):
        return reverse("pdf_book_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LibrarySettingView(LoginRequiredMixin, TemplateView):
    template_name = 'library/setting/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()
        form_kwargs = {}
        if school_setting.separate_school_section:
            library_info = LibrarySettingModel.objects.filter(type=self.request.user.profile.type).first()
            form_kwargs['type'] = self.request.user.profile.type
        else:
            library_info = LibrarySettingModel.objects.first()

        if not library_info:
            form = LibrarySettingCreateForm(**form_kwargs)
            is_library_info = False
        else:
            form = LibrarySettingEditForm(instance=library_info, **form_kwargs)
            is_library_info = True
        context['form'] = form
        context['is_library_info'] = is_library_info
        context['library_info'] = library_info
        return context


class LibrarySettingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = LibrarySettingModel
    form_class = LibrarySettingCreateForm
    template_name = 'library/setting/index.html'
    success_message = 'Library Settings updated Successfully'

    def get_success_url(self):
        return reverse('library_info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school_setting = SchoolGeneralInfoModel.objects.first()

        return context

    def get_form_kwargs(self):
        kwargs = super(LibrarySettingCreateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class LibrarySettingUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = LibrarySettingModel
    form_class = LibrarySettingEditForm
    template_name = 'library/setting/index.html'
    success_message = 'Library Setting updated Successfully'

    def get_success_url(self):
        return reverse('library_info')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_form_kwargs(self):
        kwargs = super(LibrarySettingUpdateView, self).get_form_kwargs()
        school_setting = SchoolGeneralInfoModel.objects.first()
        if school_setting.separate_school_section:
            kwargs.update({'type': self.request.user.profile.type})
        kwargs.update({'type': self.request.user.profile.type})
        return kwargs


class LibraryDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'library/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['distinct_books'] = BookModel.objects.filter(type=self.request.user.profile.type).count()
        context['distinct_copy'] = BookCopyModel.objects.filter(type=self.request.user.profile.type).count()
        context['pdf_book'] = PDFBookModel.objects.filter(type=self.request.user.profile.type).count()
        context['e_book'] = EBookModel.objects.filter(type=self.request.user.profile.type).count()
        context['borrowed_book'] = BookBorrowModel.objects.filter(type=self.request.user.profile.type,
                                                                  status='active').count()
        context['available_book'] = BookCopyModel.objects.filter(type=self.request.user.profile.type,
                                                                 status='available').count()

        context['most_borrowed_book'] = BookModel.objects.annotate(num_borrows=Count('copies__borrowed_book')).order_by(
            '-num_borrows').first()

        context['most_borrowing_student'] = StudentsModel.objects.annotate(num_borrows=Count('student_borrowed_book')).order_by(
            '-num_borrows').first()

        return context
