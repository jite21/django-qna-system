from django import forms
from .models import Answer


class AskQuestionForm(forms.Form):
    question_text = forms.CharField(help_text='Enter your Question',
                                    widget = forms.Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'form-control'}))
    asked_by = forms.CharField(required=False)

class AnswerModelForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text', 'answered_by']
        widgets = {
            'answer_text': forms.Textarea(attrs={'cols': 80, 'rows': 5, 'class': 'form-control'}),
        }