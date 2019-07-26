from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('about/', views.about, name = 'about'),
    path('forget/', views.forget, name = 'forget'),
    path('instruction/', views.instruction, name = 'instruction'),
    path('login/', views.login, name = 'login'),
    path('ques/', views.ques, name = 'ques'),
    path('result/', views.result, name = 'result'),
    path('thank/', views.thank, name = 'thank'),
    path('review/', views.Review, name = 'Review'),
]