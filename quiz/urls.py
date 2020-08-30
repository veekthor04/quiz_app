from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_start, name = 'quiz_start'),
    path('question/', views.quiz_question, name = 'quiz_question'),
    path('result/' ,views.quiz_result, name = 'quiz_result'),
]