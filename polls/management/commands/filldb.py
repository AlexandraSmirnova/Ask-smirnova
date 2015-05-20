from django.core.management.base import BaseCommand, CommandError
from polls.models import *
from django.utils import timezone
import random 

class Command(BaseCommand):
	
	def handle(self, *args, **options):
		i = 1
		while i < 20:
			u = Profile.objects.get(pk = i%3+1)
			t = Tag.objects.all()
			q = Question(author = u, question_title = "How to build a lunapark???", question_text = "Please Help me", pub_date=timezone.now(), question_reiting = random.randint(0, 50))
			q.save()
			u = Profile.objects.get(pk = (i+1)%3+1)
			
			
			a = Answer(author = u, question = q, answer_text = "hmm..it's difficult question", pub_date=timezone.now()) 
			a.save()

			self.stdout.write('Successfully created question"%s"' % q.id)
			i+=1
