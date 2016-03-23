import datetime
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError('Title is empty!')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError('Text is empty!')
        return text

    def save(self):
        self.cleaned_data['added_at'] = datetime.datetime.now()
        if self._user is not None:
            self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError('Text is empty!')
        return text

    def clean_question(self):
        try:
            question = int(self.cleaned_data['question'])
        except:
            raise forms.ValidationError('Question should be an int')
        try:
            answeredQuestion = Question.objects.get(id=question)
        except ObjectDoesNotExist:
            raise forms.ValidationError('There is not such question!')
        return answeredQuestion

    def save(self):
        self.cleaned_data['added_at'] = datetime.datetime.now()
        if self._user is not None:
            self.cleaned_data['author'] = self._user
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError('Empty username!')
        return username

    def save(self):
        User.objects.create_user(**self.cleaned_data)
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("The username and password were incorrect")
        self.cleaned_data['user'] = user

    def save(self):
        return self.cleaned_data['user']

