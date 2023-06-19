from django.urls import path
from . import views
from .views import QuizListView
from django.contrib.auth import views as auth_views
app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<int:pk>/', views.quiz_view, name='quiz-view'),
    path('<int:pk>/save/', views.save_quiz_view, name='save-view'),
    path('<int:pk>/data/', views.quiz_data_view, name='quiz-data-view'),
path('register/', views.register, name='register'),
path('login/', auth_views.LoginView.as_view(template_name="quizes/login.html"), name='login'),
path('logout/', auth_views.LogoutView.as_view(template_name="quizes/logout.html"), name='logout'),
]
