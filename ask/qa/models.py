from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True)
    likes = models.ManyToManyField(User, related_name='likes_set',)
    def __unicode__(self):
        return self.title
    def get_url(self):
        return reverse('questionById',
                       kwargs={'qId': self.id})
    class Meta:
        db_table = 'qa_question'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True)
    def __unicode__(self):
        return self.text
    class Meta:
        db_table = 'qa_answer'
