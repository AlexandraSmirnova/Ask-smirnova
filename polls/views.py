from django.shortcuts import render_to_response
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from .models import Question, Profile, Answer, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	context = {}
	limit = 5
	context['title'] = "Main Page"
	latest_question_list = Question.objects.annotate(num_answer=Count("answer")).order_by('-pub_date')
	pager = Paginator(latest_question_list, limit) 
	page = request.GET.get('page', 1)
	context['page'] = page
	try:
		context['quaryset'] = pager.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		context['quaryset'] = pager.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		context['quaryset'] = pager.page(pager.num_pages)
	context['questions'] = pager.page(page).object_list
	context['pager'] = pager
	context['minPageNum'] = int(page) - 3
	context['maxPageNum'] = int(page) + 3
	context['tags'] = Tag.objects.all()[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	context['authors'] = Profile.objects.order_by('-user_reiting')[:10]
	return render(request, 'index.html', context)


def reiting(request):
	context = {}
	context['title'] = "Best Questions"
	limit = 5
	latest_question_list = Question.objects.annotate(num_answer=Count("answer")).order_by('-question_reiting')[:100]
	pager = Paginator(latest_question_list, limit) 
	page = request.GET.get('page', 1)
	context['page'] = page
	try:
		context['quaryset'] = pager.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		context['quaryset'] = pager.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		context['quaryset'] = pager.page(pager.num_pages)
	context['questions'] = pager.page(page).object_list
	context['pager'] = pager
	context['minPageNum'] = int(page) - 3
	context['maxPageNum'] = int(page) + 3
	context['authors'] = Profile.objects.order_by('-user_reiting')[:10]
	context['popular_tags'] = Tag.objects.all().values('id','word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'index.html', context)
    #return render_to_response('index.html')

def tags(request, tag_id):
	context = {}
	limit = 5
	question_list = Question.objects.annotate(num_answer=Count("answer")).filter(tags = tag_id)
	latest_question_list = question_list.order_by('-question_reiting')[:5]
	pager = Paginator(latest_question_list, limit) 
	page = request.GET.get('page', 1)
	context['page'] = page
	context['title'] = "Search by tag: "
	try:
		context['quaryset'] = pager.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		context['quaryset'] = pager.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		context['quaryset'] = pager.page(pager.num_pages)
	context['questions'] = pager.page(page).object_list
	context['pager'] = pager
	context['latest_question_list'] = latest_question_list
	context['minPageNum'] = int(page) - 3
	context['maxPageNum'] = int(page) + 3
	context['tag'] = Tag.objects.get(pk = tag_id)
	context['authors'] = Profile.objects.order_by('-user_reiting')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'index.html', context)


def question(request, question_id):
	try:
		question = Question.objects.annotate(num_answer=Count("answer")).get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	context = {}
	context['question'] =  question
	context['tags'] = Tag.objects.all()[:10]
	context['authors'] = Profile.objects.order_by('-user_reiting')[:10]
	context['answers'] = Answer.objects.filter(question = question_id)
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'question.html', context)

def new_q(request):
	context = {}
	context['tags'] = Tag.objects.all()
	context['authors'] = Profile.objects.order_by('-user_reiting')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'new_q.html', context)

def login(request):
	context = {}
	context['tags'] = Tag.objects.all()[:10]
	context['authors'] = Profile.objects.order_by('-user_reiting')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'login.html', context)

def reg(request):
	context = {}
	context['tags'] = Tag.objects.all()[:10]
	context['authors'] = Profile.objects.order_by('-user_reiting')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'register.html', context)




