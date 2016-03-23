from django.conf.urls import url
from qa import views

urlpatterns = [
    url(r'^$', views.test, name='index'),
    url(r'^/popular/', views.test, name='pop'),
]
