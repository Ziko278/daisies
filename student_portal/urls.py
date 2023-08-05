from django.urls import path
from student_portal.views import *


urlpatterns = [
    path('dashboard', StudentDashboardView.as_view(), name='student_dashboard'),

    path('fee/dashboard', StudentFeeView.as_view(), name='student_fee'),
    path('fee/select-method', select_fee_method, name='select_fee_method'),

    path('library/book/index', StudentBookListView.as_view(), name='student_book_index'),
    path('library/borrowed-book/index', StudentBorrowedBookListView.as_view(),
         name='student_borrowed_book_index'),

    path('library/pdf/index', StudentPDFListView.as_view(), name='student_pdf_index'),
    path('library/pdf/<int:pk>/detail', StudentPDFDetailView.as_view(), name='student_pdf_detail'),

    path('library/e-book/index', StudentEBookListView.as_view(), name='student_ebook_index'),
    path('library/e-book/<int:pk>/detail', StudentEBookDetailView.as_view(), name='student_ebook_detail'),

    path('result/<int:pk>/current-result', current_term_result, name='student_current_result'),



]

