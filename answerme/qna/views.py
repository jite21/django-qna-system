from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm, Textarea
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from .models import Question, Answer, Comment
from .forms import AskQuestionForm, AnswerModelForm


class IndexView(generic.ListView):
    template_name = 'qna/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-posted_on')[:5]

class QuestionDetailView(generic.DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        return context

class AnswerDetailView(generic.DetailView):
    model = Answer

class AskQuestionView(FormView):
    template_name = 'qna/ask_question.html'
    form_class = AskQuestionForm

    def form_valid(self, form, *args, **kwargs):
        form.cleaned_data['asked_by'] = self.request.user if self.request.user.is_authenticated else None
        Question.objects.create(**form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('index')


class AnswerView(CreateView):
    model = Answer
    template_name = 'qna/answer.html'
    form_class = AnswerModelForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.question = Question.objects.get(pk = self.kwargs.get('question_pk'))
        form.instance.answered_by = self.request.user if self.request.user.is_authenticated else None
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AnswerView, self).get_context_data(**kwargs)
        context['question'] = Question.objects.get(pk=self.kwargs.get('question_pk'))
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse('question-detail', args=(self.kwargs.get('question_pk'),))

class UpdateAnswerView(UpdateView):
    model = Answer
    template_name = 'qna/update_answer.html'
    form_class = AnswerModelForm

    def get_success_url(self, *args, **kwargs):
        return reverse('answer-detail', args=(self.kwargs.get('pk'),))

class DeleteAnswerView(DeleteView):
    model = Answer
    template_name = 'qna/answer_delete.html'
    form_class = AnswerModelForm

    def get_success_url(self, *args, **kwargs):
        return reverse('index')

'''
def ask_question(request):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            question = Question(question_text=form.cleaned_data['question_text'])
            question.save()
            return HttpResponseRedirect(reverse('index') )

    else:
        form = AskQuestionForm()
    
    context = {
        'form': form,
    }

    return render(request, 'qna/ask_question.html', context)

def answer(request, question_pk):
    if request.method == 'POST':
        form = AnswerModelForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('question-detail', args=(question_pk,)))
        
    else:
        form = AnswerModelForm()

    context = {
        'form': form,
        'question': Question.objects.get(pk=question_pk),
    }

    return render(request, 'qna/answer.html', context)
'''