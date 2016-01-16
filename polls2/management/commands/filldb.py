from django.core.management.base import BaseCommand, CommandError
from polls2.models import *
from django.utils import timezone
import random 

class Command(BaseCommand):
	
	def handle(self, *args, **options):
		text = ['How to build a lunapark???', 'To be or not to be?', 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor']
		i = 1
		while i < 20:
			num = random.randint(0, 2)
			u = Profile.objects.get(pk = i%6+1)
			t = Tag.objects.all()
			q = Question(author = u, question_title = text[num], question_text = "Please Help me", pub_date=timezone.now(), rating = 0)
			q.save()
			u = Profile.objects.get(pk = (i+1)%3+1)			
			
			a = Answer(author = u, question = q, answer_text = "hmm..it's difficult question", pub_date=timezone.now()) 
			a.save()

			self.stdout.write('Successfully created question"%s"' % q.id)
			i+=1
