from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from exam.models import *
from exam.forms import *


class ExamCreateView(SuccessMessageMixin, CreateView):
    model = ExamModel
    form_class = ExamForm
    success_message = 'Exam Added Successfully'
    template_name = 'exam/exam/index.html'

    def get_success_url(self):
        return reverse('exam_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_list'] = ExamModel.objects.all()
        return context


class ExamListView(ListView):
    model = ExamModel
    fields = '__all__'
    template_name = 'exam/exam/index.html'
    context_object_name = "exam_list"

    def get_queryset(self):
        return ExamModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_list'] = ExamModel.objects.all()
        context['form'] = ExamForm

        return context


class ExamDetailView(DetailView):
    model = ExamModel
    fields = '__all__'
    template_name = 'exam/exam/detail.html'
    context_object_name = "exam"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ExamTimeTableForm
        return context


class ExamUpdateView(SuccessMessageMixin, UpdateView):
    model = ExamModel
    form_class = ExamEditForm
    success_message = 'Exam Updated Successfully'
    template_name = 'exam/exam/index.html'

    def get_success_url(self):
        return reverse('exam_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_list'] = ExamModel.objects.all()
        return context


class ExamDeleteView(SuccessMessageMixin, DeleteView):
    model = ExamModel
    success_message = 'Exam Deleted Successfully'
    fields = '__all__'
    template_name = 'exam/exam/delete.html'
    context_object_name = "exam"

    def get_success_url(self):
        return reverse("exam_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ExamTimeTableCreateView(SuccessMessageMixin, CreateView):
    model = ExamTimeTableModel
    form_class = ExamTimeTableForm
    success_message = 'Exam Time Table Added Successfully'
    template_name = 'exam/exam/detail.html'

    def get_success_url(self):
        return reverse('exam_detail', kwargs={'pk': self.object.exam.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exam_pk = self.kwargs.get('exam_pk')
        exam = ExamModel.objects.get(pk=exam_pk)
        context['exam'] = exam
        return context


class ExamTimeTableListView(ListView):
    model = ExamTimeTableModel
    fields = '__all__'
    template_name = 'exam/exam/index.html'
    context_object_name = "exam_list"

    def get_queryset(self):
        return ExamTimeTableModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_list'] = ExamTimeTableModel.objects.all()
        context['form'] = ExamForm

        return context


class ExamTimeTableDetailView(DetailView):
    model = ExamTimeTableModel
    fields = '__all__'
    template_name = 'exam/exam/detail.html'
    context_object_name = "exam"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ExamTimeTableUpdateView(SuccessMessageMixin, UpdateView):
    model = ExamTimeTableModel
    form_class = ExamTimeTableEditForm
    success_message = 'Exam Updated Successfully'
    template_name = 'exam/exam/index.html'

    def get_success_url(self):
        return reverse('exam_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_list'] = ExamModel.objects.all()
        return context


class ExamTimeTableDeleteView(SuccessMessageMixin, DeleteView):
    model = ExamTimeTableModel
    success_message = 'Exam Deleted Successfully'
    fields = '__all__'
    template_name = 'exam/exam/delete.html'
    context_object_name = "exam"

    def get_success_url(self):
        return reverse("exam_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def select_exam_view(request):
    academic_info = SchoolAcademicInfoModel.objects.first()
    if request.method == 'POST':
        timetable = request.POST['timetable']

        return redirect(reverse('set_exam_question', kwargs={'timetable_pk': timetable}))

    context = {
        'timetable_list': ExamTimeTableModel.objects.filter(term=academic_info.term, session=academic_info.session,
                                                            exam__exam_type='exam')
    }
    return render(request, 'exam/exam/select_exam.html', context)


def set_exam_question_view(request, timetable_pk):
    if request.method == 'POST':
        pass

    timetable = ExamTimeTableModel.objects.get(pk=timetable_pk)

    context = {
        'timetable': timetable,
        'question_list': ExamQuestionModel.objects.filter(timetable=timetable, is_sub=False),
        'question_form': ExamQuestionForm,
        'option_form': ExamQuestionOptionForm
    }
    return render(request, 'exam/exam/exam_question.html', context)


class ExamQuestionCreateView(SuccessMessageMixin, CreateView):
    model = ExamQuestionModel
    form_class = ExamQuestionForm
    success_message = 'Question Added Successfully'
    template_name = 'exam/exam/exam_question.html'

    def get_success_url(self):
        return reverse('set_exam_question', kwargs={'timetable_pk': self.object.timetable.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['option_form'] = ExamQuestionOptionForm
        return context


class ExamQuestionUpdateView(SuccessMessageMixin, UpdateView):
    model = ExamQuestionModel
    form_class = ExamQuestionEditForm
    success_message = 'Question Updated Successfully'
    template_name = 'exam/exam/exam_question.html'

    def get_success_url(self):
        return reverse('set_exam_question', kwargs={'timetable_pk': self.object.timetable.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_list'] = ExamModel.objects.all()
        return context


class ExamQuestionDeleteView(SuccessMessageMixin, DeleteView):
    model = ExamQuestionModel
    success_message = 'Question Deleted Successfully'
    fields = '__all__'
    template_name = 'exam/exam/exam_question.html'
    context_object_name = "exam_question"

    def get_success_url(self):
        return redirect(reverse('set_exam_question', kwargs={'timetable_pk': self.object.timetable.id}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class ExamQuestionOptionCreateView(SuccessMessageMixin, CreateView):
#     model = ExamQuestionModel
#     form_class = ExamQuestionForm
#     success_message = 'Option Added Successfully'
#     template_name = 'exam/exam/exam_question.html'
#
#     def get_success_url(self):
#         return reverse('set_exam_question',
#                        kwargs={'exam_pk': self.object.question.exam.id,
#                                'class_pk': self.object.question.student_class.id,
#                                'section_pk': self.object.question.class_section.id,
#                                'subject_pk': self.object.question.subject.id})
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context


def add_question_option_view(request):
    if request.method == 'POST':
        question_pk = request.POST.get('question')
        question = ExamQuestionModel.objects.get(pk=question_pk)
        form = ExamQuestionOptionForm(request.POST)
        if form.is_valid():
            option = form.save()
            question.options.add(option)
            return redirect(reverse('set_exam_question', kwargs={'timetable_pk': question.timetable.id}))


class ExamQuestionAnswerView(SuccessMessageMixin, UpdateView):
    model = ExamQuestionModel
    form_class = ExamQuestionAnswerForm
    success_message = 'Correct Answer Chosen Successfully'
    template_name = 'exam/exam/exam_question.html'

    def get_success_url(self):
        return reverse('set_exam_question', kwargs={'timetable_pk': self.object.timetable.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exam_list'] = ExamModel.objects.all()
        return context


def add_sub_question_view(request, pk):
    if request.method == 'POST':
        timetable_pk = request.POST.get('timetable')
        numbering = request.POST.get('numbering')
        question = request.POST.get('question')
        mark = request.POST.get('mark')
        theory_answer = request.POST.get('theory_answer')
        timetable = ExamTimeTableModel.objects.get(pk=timetable_pk)
        is_sub = True

        sub_question = ExamQuestionModel.objects.create(timetable=timetable, numbering=numbering, question=question,
                                                        mark=mark, is_sub=is_sub,
                                                        theory_answer=theory_answer, question_type='theory')
        sub_question.save()
        main_question = ExamQuestionModel.objects.get(pk=pk)
        main_question.sub_questions.add(sub_question)
        messages.success(request, 'sub question added successfully')

        return redirect(reverse('set_exam_question', kwargs={'timetable_pk': timetable.id}))

