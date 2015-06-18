from django.shortcuts import render_to_response
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.contrib import auth
from .models import Question, Profile, Answer, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProfileUser
from django.utils import timezone
from django.contrib.auth.models import User

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
		page = 1
		context['page'] = 1
		context['quaryset'] = pager.page(page)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		page = pager.num_pages	
		context['page'] = page
		context['queryset'] = pager.page(page)
	context['profile'] = get_user_data(request)
	context['questions'] = pager.page(page).object_list
	context['pager'] = pager
	context['minPageNum'] = int(page) - 3
	context['maxPageNum'] = int(page) + 3
	context['tags'] = Tag.objects.all().values('word').filter(id=3)
	#num = Question.objects.annotate()
	#return HttpResponse(tags)
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
		page = 1
		context['page'] = 1
		context['quaryset'] = pager.page(page)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		page = pager.num_pages	
		context['page'] = page
		context['queryset'] = pager.page(page)
	context['profile'] = get_user_data(request)
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
	try:
		context['tag'] = Tag.objects.get(pk = tag_id)
	except Tag.DoesNotExist:
		raise Http404("Tag does not exist")
	question_list = Question.objects.annotate(num_answer=Count("answer")).filter(tags = tag_id)	
	limit = 5
	latest_question_list = question_list.order_by('-question_reiting')[:5]
	pager = Paginator(latest_question_list, limit) 
	page = request.GET.get('page', 1)
	context['page'] = page
	context['title'] = "Search by tag: "
	try:
		context['quaryset'] = pager.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		page = 1
		context['page'] = 1
		context['quaryset'] = pager.page(page)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		page = pager.num_pages	
		context['page'] = page
		context['queryset'] = pager.page(page)
	context['profile'] = get_user_data(request)
	context['questions'] = pager.page(page).object_list
	context['pager'] = pager
	context['latest_question_list'] = latest_question_list
	context['minPageNum'] = int(page) - 3
	context['maxPageNum'] = int(page) + 3
	context['authors'] = Profile.objects.order_by('-user_reiting')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'index.html', context)


def question(request, question_id):
	try:
		question = Question.objects.annotate(num_answer=Count("answer")).get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	context = {}
	context['profile'] = get_user_data(request)
	
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
	if request.POST:
		name = request.POST['username']
		password =  request.POST['password']
		#return HttpResponse(password)
		user  = auth.authenticate(username=name, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			return render(request, 'login.html', {"login_error": True} )
	return render(request, 'login.html', context)


def logout_view(request):
	auth.logout(request)
	return redirect('/')

def reg(request):
	context = {}
	form = ProfileUser()		
	if request.POST:
		form = ProfileUser(request.POST)
		if form.is_valid():
			password =  form.cleaned_data.get('password')
			password2 =  form.cleaned_data.get('passwordSecond')
			if password2 != password:
				return HttpResponse("Mistake1")
			#name = form.cleaned_data.get('username')
			#mail = form.cleaned_data.get('mail')
			nick = form.cleaned_data.get('nick')
			
			try:
				u = User.objects.create(username = name, email = mail )
				u.set_password(password)
				u.save()
			except:
				return HttpResponse("Mistake2")
			context['message']='Congratiolations'
			return redirect('/', context)
		else:
			return HttpResponse("Mistake3")
	else:
		context['form'] = form
	context['authors'] = Profile.objects.order_by('-user_reiting')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'register.html', context)

def get_user_data(request):
	if request.user.is_authenticated():
		context = {}
		prop = Profile.objects.get(user_id=request.user.id)
		context["id"] = request.user.id
		context["nickname"] = prop.user_name
		context["avatar"] = prop.avatar
		return context


