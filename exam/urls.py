from django.urls import path
from exam.views import *

urlpatterns = [

    path('exam/create', ExamCreateView.as_view(), name='exam_create'),
    path('exam/index', ExamListView.as_view(), name='exam_index'),
    path('exam/<int:pk>/detail', ExamDetailView.as_view(), name='exam_detail'),
    path('exam/<int:pk>/edit', ExamUpdateView.as_view(), name='exam_edit'),
    path('exam/<int:pk>/delete', ExamDeleteView.as_view(), name='exam_delete'),

    path('exam/<int:exam_pk>/timetable/create', ExamTimeTableCreateView.as_view(), name='exam_timetable_create'),
    path('exam/timetable/index', ExamTimeTableListView.as_view(), name='exam_timetable_index'),
    path('exam/timetable/<int:pk>/detail', ExamTimeTableDetailView.as_view(), name='exam_timetable_detail'),
    path('exam/timetable/<int:pk>/edit', ExamTimeTableUpdateView.as_view(), name='exam_timetable_edit'),
    path('exam/timetable/<int:pk>/delete', ExamTimeTableDeleteView.as_view(), name='exam_timetable_delete'),

    path('exam/select-exam', select_exam_view, name='select_exam'),
    path('<int:timetable_pk>', set_exam_question_view, name='set_exam_question'),

    path('exam/question/add', ExamQuestionCreateView.as_view(), name='exam_question_create'),
    path('exam/question/<int:pk>/answer', ExamQuestionAnswerView.as_view(), name='exam_question_answer'),
    path('exam/question/<int:pk>/add-sub', add_sub_question_view, name='exam_add_sub_question'),


    path('exam/question/option/add', add_question_option_view, name='exam_question_option_create'),

]

