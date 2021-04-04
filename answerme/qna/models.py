from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Question(models.Model):
    question_text = models.CharField(max_length=200, help_text='Enter your question')
    asked_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    posted_on = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-posted_on']

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('question-detail', args=[str(self.id)])

    def total_answers(self):
        return self.answer_set.count()

    def total_comments(self):
        return self.comment_set.count()
    
    total_answers.short_description = 'Total Answers'
    total_comments.short_description = 'Total Comments'

class Answer(models.Model):
    answer_text = models.CharField(max_length=200, help_text='Enter the answer')
    stars = models.IntegerField(default=0)
    question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    answered_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    posted_on = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-star','-posted_on']

    def __str__(self):
        return self.answer_text

    def get_absolute_url(self):
        return reverse('answer-detail', args=[str(self.id)])

    def get_update_url(self):
        return reverse('update-answer', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('delete-answer', args=[str(self.id)])

    def total_comments(self):
        return self.comment_set.count()
    
    total_comments.short_description = 'Total Comments'

class Comment(models.Model):
    comment_text = models.CharField(max_length=200, help_text='Enter your comment')
    answer = models.ForeignKey('Answer', on_delete=models.SET_NULL, null=True, blank=True)
    commented_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    posted_on = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-star','-posted_on']

    def __str__(self):
        return self.comment_text

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.id)])