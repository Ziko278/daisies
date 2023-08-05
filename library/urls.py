from django.urls import path
from library.views import *

urlpatterns = [

    path('book-category/create', BookCategoryCreateView.as_view(), name='book_category_create'),
    path('book-category/index', BookCategoryListView.as_view(), name='book_category_index'),
    path('book-category/<int:pk>/edit', BookCategoryUpdateView.as_view(), name='book_category_edit'),
    path('book-category/<int:pk>/delete', BookCategoryDeleteView.as_view(), name='book_category_delete'),

    path('book-author/create', BookAuthorCreateView.as_view(), name='book_author_create'),
    path('book-author/index', BookAuthorListView.as_view(), name='book_author_index'),
    path('book-author/<int:pk>/edit', BookAuthorUpdateView.as_view(), name='book_author_edit'),
    path('book-author/<int:pk>/delete', BookAuthorDeleteView.as_view(), name='book_author_delete'),

    path('book/create', BookCreateView.as_view(), name='book_create'),
    path('book/index', BookListView.as_view(), name='book_index'),
    path('book/<int:pk>/detail', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:pk>/edit', BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book_delete'),

    path('book-copy/<int:pk>/generate', generate_book_copies, name='book_copy_create'),
    path('book-copy/<int:pk>/detail', BookCopyDetailView.as_view(), name='book_copy_detail'),
    path('book-copy/<int:pk>/delete', BookCopyDeleteView.as_view(), name='book_copy_delete'),

    path('book/borrow',  borrow_book, name='book_borrow'),
    path('book/borrowed-books', BorrowedBookListView.as_view(), name='borrowed_books'),
    path('book/borrowed-book/<int:pk>/return', return_borrowed_book, name='book_return'),

    path('e-book/create', EBookCreateView.as_view(), name='e_book_create'),
    path('e-book/index', EBookListView.as_view(), name='e_book_index'),
    path('e-book/<int:pk>/detail', EBookDetailView.as_view(), name='e_book_detail'),
    path('e-book/<int:pk>/edit', EBookUpdateView.as_view(), name='e_book_edit'),
    path('e-book/<int:pk>/delete', EBookDeleteView.as_view(), name='e_book_delete'),


    path('pdf/create', PDFBookCreateView.as_view(), name='pdf_book_create'),
    path('pdf/index', PDFBookListView.as_view(), name='pdf_book_index'),
    path('pdf/<int:pk>/detail', PDFBookDetailView.as_view(), name='pdf_book_detail'),
    path('pdf/<int:pk>/edit', PDFBookUpdateView.as_view(), name='pdf_book_edit'),
    path('pdf/<int:pk>/delete', PDFBookDeleteView.as_view(), name='pdf_book_delete'),

    path('library-info', LibrarySettingView.as_view(), name='library_info'),
    path('library-info/create', LibrarySettingCreateView.as_view(), name='library_info_create'),
    path('library-info/<int:pk>/update', LibrarySettingUpdateView.as_view(), name='library_info_update'),

    path('library-dashboard', LibraryDashboardView.as_view(), name='library_dashboard'),
]

