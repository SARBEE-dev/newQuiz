from django import forms
from .models import Quiz, Question, Answer
from django.contrib import admin
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ('name', 'topic', 'number_of_questions', 'time', 'required_score_to_pass','difficulty')

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('text', 'quiz')
