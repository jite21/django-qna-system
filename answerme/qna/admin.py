from django.contrib import admin
from .models import Question, Answer, Comment

# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer

class CommentInline(admin.StackedInline):
    model = Comment

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=('question_text', 'asked_by', 'posted_on', 'total_answers', 'total_comments')
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display=('answer_text', 'stars', 'answered_by', 'posted_on', 'total_comments')
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass