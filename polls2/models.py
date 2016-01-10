from django.db import models
from django.contrib.auth.models import User
#from djangosphinx.models import SphinxSearch

class Tag(models.Model):
	word = 	models.CharField(max_length=50)
	def __str__(self):             
		return self.word

class Profile(models.Model):
	user_id = models.OneToOneField(User, default = 1)
	user_name = models.CharField(max_length=100)
	user_rating = models.IntegerField(default=0)
	avatar = models.ImageField()
	def __str__(self):             
		return self.user_name

class VoteForPosts(models.Model):
	value = models.IntegerField()
	voter = models.ForeignKey(User, related_name = 'VoteForPost')
	post = models.IntegerField(default = 0)
	p_type = models.IntegerField(default = 0) #0 - Question, 1 - Answer

class Question(models.Model):
	question_title = models.CharField(max_length=100)
	question_text = models.TextField(max_length=400)
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey(Profile, default = 1)
	rating = models.IntegerField(default=0)
	tags = models.ManyToManyField(Tag)
	#likes = models.ManyToManyField(Like)
	#search = SphinxSearch(
	#	index = 'pr_question_index',
	#	weights = {	'header': 100, 'question_text': 50}
	#)
	def __str__(self):             
		return self.question_title

class Answer(models.Model):
	answer_text = models.TextField(max_length=400)
	pub_date = models.DateTimeField()
	author = models.ForeignKey(Profile)
	rating = models.IntegerField(default=0)
	flag = models.NullBooleanField(default = 0)
	question = models.ForeignKey(Question) 
	def __str__(self):             
		return self.answer_text







