from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^new/.*$', views.test, name='test'),
        url(r'^$', views.newQuestions, name='newQuestions'),
        url(r'^login/.*$', views.login, name='login'),
        url(r'^signup/.*$', views.signUp, name='signUp'),
        url(r'^ask/.*$', views.askQuestion, name='askQuestion'),
        url(r'^answer/.*$', views.answerQuestion, name='answerQuestion'),
        url(r'^popular/.*$', views.popularQuestions, name='popularQuestions'),
        url(r'^question/(?P<qId>\d+)/.*$', views.questionById, name='questionById'),
]
