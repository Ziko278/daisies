from django.urls import path
from academic.views import *

urlpatterns = [
    path('class/section/create', ClassSectionCreateView.as_view(), name='class_section_create'),
    path('class/section/index', ClassSectionListView.as_view(), name='class_section_index'),
    path('class/section/<int:pk>/edit', ClassSectionUpdateView.as_view(), name='class_section_edit'),
    path('class/section/<int:pk>/delete', ClassSectionDeleteView.as_view(), name='class_section_delete'),

    path('class/create', ClassCreateView.as_view(), name='class_create'),
    path('class/index', ClassListView.as_view(), name='class_index'),
    path('class/<int:pk>/detail', ClassDetailView.as_view(), name='class_detail'),
    path('class/<int:pk>/edit', ClassUpdateView.as_view(), name='class_edit'),
    path('class/<int:pk>/delete', ClassDeleteView.as_view(), name='class_delete'),

    path('subject/create', SubjectCreateView.as_view(), name='subject_create'),
    path('subject/index', SubjectListView.as_view(), name='subject_index'),
    path('subject/<int:pk>/detail', SubjectDetailView.as_view(), name='subject_detail'),
    path('subject/<int:pk>/edit', SubjectUpdateView.as_view(), name='subject_edit'),
    path('subject/<int:pk>/delete', SubjectDeleteView.as_view(), name='subject_delete'),

    path('timetable/create', TimeTableCreateView.as_view(), name='timetable_create'),
    path('timetable/index', TimeTableListView.as_view(), name='timetable_index'),
    path('timetable/<int:pk>/edit', TimeTableUpdateView.as_view(), name='timetable_edit'),
    path('timetable/<int:pk>/delete', TimeTableDeleteView.as_view(), name='timetable_delete'),

    path('lesson-document/create', LessonDocumentCreateView.as_view(), name='lesson_document_create'),
    path('lesson-document/index', LessonDocumentListView.as_view(), name='lesson_document_index'),
    path('lesson-document/<int:pk>/detail', LessonDocumentDetailView.as_view(), name='lesson_document_detail'),
    path('lesson-document/<int:pk>/edit', LessonDocumentUpdateView.as_view(), name='lesson_document_edit'),
    path('lesson-document/<int:pk>/delete', LessonDocumentDeleteView.as_view(), name='lesson_document_delete'),

    path('lesson-note/create', LessonNoteCreateView.as_view(), name='lesson_note_create'),
    path('lesson-note/index', LessonNoteListView.as_view(), name='lesson_note_index'),
    path('lesson-note/<int:pk>/detail', LessonNoteDetailView.as_view(), name='lesson_note_detail'),
    path('lesson-note/<int:pk>/edit', LessonNoteUpdateView.as_view(), name='lesson_note_edit'),
    path('lesson-note/<int:pk>/delete', LessonNoteDeleteView.as_view(), name='lesson_note_delete'),

    path('class/section/info/create', ClassSectionInfoCreateView.as_view(), name='class_section_info_create'),
    path('class/section/info/<int:class_pk>/<int:section_pk>/detail', ClassSectionInfoDetailView.as_view(),
         name='class_section_info_detail'),
    path('class/section/info/<int:pk>/edit', ClassSectionInfoUpdateView.as_view(), name='class_section_info_edit'),

    path('class/subject/info/create', ClassSectionSubjectTeacherCreateView.as_view(), name='class_subject_info_create'),
    path('class/subject/info/<int:pk>/edit', ClassSectionSubjectTeacherUpdateView.as_view(), name='class_subject_info_edit'),
    path('class/subject/info/<int:pk>/delete', ClassSectionSubjectTeacherDeleteView.as_view(), name='class_subject_info_delete'),

    path('academic-info', AcademicSettingView.as_view(), name='academic_info'),
    path('academic-info/create', AcademicSettingCreateView.as_view(), name='academic_info_create'),
    path('academic-info/<int:pk>/update', AcademicSettingUpdateView.as_view(), name='academic_info_update'),


    path('proceed-to-next-term', proceed_to_next_term, name='proceed_to_next_term'),
    path('proceed-to-next-term-confirmed', proceed_to_next_term_confirmed, name='proceed_to_next_term_confirmed'),
    path('confirm-admin-password', confirm_admin_password, name='confirm_admin_password'),
    path('confirm-setting-okay', check_setting_is_okay, name='check_setting_is_okay'),
    path('save-student-attendance-record', save_student_attendance_record, name='save_student_attendance_record'),
    path('save-student-academic-record', save_student_academic_record, name='save_student_academic_record'),
    path('save-student-fee-record', save_student_fee_record, name='save_student_fee_record'),
    path('update-student-class', update_student_class, name='update_student_class'),
    path('update-and-clean-up', update_and_clean_up, name='update_and_clean_up'),
]

