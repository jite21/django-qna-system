from django.urls import path
from . import views

#app_name = 'qna'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question-detail'),
    path('answer/<int:pk>', views.AnswerDetailView.as_view(), name='answer-detail'),
    path('answer/<int:pk>/update', views.UpdateAnswerView.as_view(), name='update-answer'),
    path('answer/<int:pk>/delete', views.DeleteAnswerView.as_view(), name='delete-answer'),
    path('<int:question_pk>/answer', views.AnswerView.as_view(), name='answer'),
    path('ask/', views.AskQuestionView.as_view(), name='ask-question')
]