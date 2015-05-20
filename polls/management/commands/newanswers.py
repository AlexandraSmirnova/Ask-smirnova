from django.core.management.base import BaseCommand, CommandError
from polls.models import *
from django.utils import timezone
import random 

class Command(BaseCommand):
	
	def handle(self, *args, **options):
		i = 1
		while i < 9:
			u = Profile.objects.get(pk = i%3+1)
			t = Tag.objects.all()
			q = Question.objects.get(pk = 10)
			text ='i am number %i ' 
			a = Answer(author = u, question = q, answer_text = text, pub_date=timezone.now()) 
			a.save()

			self.stdout.write('Successfully created question"%s"' % q.id)
			i+=1
