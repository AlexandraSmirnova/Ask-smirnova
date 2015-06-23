from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	word = 	models.CharField(max_length=50)
	def __str__(self):             
		return self.word

class Profile(models.Model):
	user_id = models.OneToOneField(User, default = 1)
	user_name = models.CharField(max_length=100)
	#user_password = models.CharField(max_length=100, default=123)
	#user_mail = models.EmailField(max_length=100)
	user_reiting = models.IntegerField(default=0)
	avatar = models.ImageField()
	#registration_date= models.DateTimeField()
	def __str__(self):             
		return self.user_name

class Like(models.Model):
	user = models.ForeignKey(Profile)
	state = models.IntegerField(default=0)

class Question(models.Model):
	question_title = models.CharField(max_length=100)
	question_text = models.TextField(max_length=400)
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey(Profile, default = 1)
	question_reiting = models.IntegerField(default=0)
	tags = models.ManyToManyField(Tag)
	likes = models.ManyToManyField(Like)
	def __str__(self):             
		return self.question_title

class Answer(models.Model):
	answer_text = models.TextField(max_length=400)
	pub_date = models.DateTimeField()
	author = models.ForeignKey(Profile)
	reiting_a = models.IntegerField(default=0)
	flag = models.NullBooleanField(default = 0)
	question = models.ForeignKey(Question) 
	likes = models.ManyToManyField(Like)
	def __str__(self):             
		return self.answer_text






