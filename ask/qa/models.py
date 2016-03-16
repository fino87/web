from django.contrib.auth.models import User,UserManager
from django.db import models

class Local_User(User):
	#questions=models.ManyToManyField(Question)
	objects = UserManager()

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(blank=True)
	rating = models.IntegerField()
	author = models.ForeignKey(Local_User,related_name='author')
	likes = models.ManyToManyField(Local_User,related_name='likes')

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.ForeignKey(Question)
	author = models.ForeignKey(Local_User)
