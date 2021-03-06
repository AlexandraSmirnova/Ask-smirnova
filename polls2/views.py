#TODO: 1.use manager
#2. Add search
#3. Add checkboxes
from django.shortcuts import render_to_response
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpRequest, Http404
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from django.contrib import auth
from polls2.models import Question, Profile, Answer, Tag, VoteForPosts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
	context = {}
	context['title'] = "Main Page"
	latest_question_list = Question.objects.annotate(num_answer=Count("answer")).order_by('-pub_date')
	pages = pagination(request, latest_question_list)
	context.update(pages)
	context['profile'] = get_user_data(request)
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	context['authors'] = Profile.objects.order_by('-user_rating')[:10]
	return render(request, 'index.html', context)

#sort by rating
def rating(request):
	context = {}
	context['title'] = "Best Questions"
	latest_question_list = Question.objects.annotate(num_answer=Count("answer")).order_by('-rating')[:100]
	pages = pagination(request, latest_question_list)
	context.update(pages)
	context['profile'] = get_user_data(request)
	context['authors'] = Profile.objects.order_by('-user_rating')[:10]
	context['popular_tags'] = Tag.objects.all().values('id','word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'index.html', context)

#filter questions by tag
def tags(request, tag_id):
	context = {}	
	try:
		context['tag'] = Tag.objects.get(pk = tag_id)
	except Tag.DoesNotExist:
		raise Http404("Tag does not exist")
	question_list = Question.objects.annotate(num_answer=Count("answer")).filter(tags = tag_id)	
	latest_question_list = question_list.order_by('-rating')
	pages = pagination(request, latest_question_list)
	context.update(pages)
	context['title'] = "Search by tag: "
	context['profile'] = get_user_data(request)
	context['authors'] = Profile.objects.order_by('-user_rating')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'index.html', context)

#filter questions by author
def authors(request, author_id):
	context = {}	
	try:
		context['author'] = Profile.objects.get(pk = author_id)
	except Tag.DoesNotExist:
		raise Http404("Tag does not exist")
	question_list = Question.objects.annotate(num_answer=Count("answer")).filter(author = author_id)	
	latest_question_list = question_list.order_by('-rating')
	pages = pagination(request, latest_question_list)
	context.update(pages)
	context['title'] = "Search by author: "
	context['profile'] = get_user_data(request)
	context['authors'] = Profile.objects.order_by('-user_rating')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'index.html', context)

#page of one question
def question(request, question_id):
	try:
		question = Question.objects.annotate(num_answer=Count("answer")).get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	context = {}
	context['profile'] = {}
	context['profile'] = get_user_data(request)
	context['question'] =  question
	context['authors'] = Profile.objects.order_by('-user_rating')[:10]
	context['answers'] = Answer.objects.filter(question = question_id)
	#if context['profile']['nickname']:
	if context['profile'].get('nickname') == str(question.author):
		context['special_status'] = True
	pages = pagination(request, context['answers'])
	context.update(pages)
	context['answers'] = context['questions']
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	return render(request, 'question.html', context)

#add new question
@login_required
def new_q(request):
	context = {}
	context['profile'] = get_user_data(request)
	context['authors'] = Profile.objects.order_by('-user_rating')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	form = NewQuestion()		
	if request.POST:
		form = NewQuestion(request.POST)
		context['form'] = form
		if form.is_valid():
			title = form.cleaned_data["title"]
			text = form.cleaned_data["text"]
			tags = form.cleaned_data["tags"].replace(" ", "").split(",")
			q = Question.objects.create(question_title = title, question_text = text, author = Profile.objects.get(user_id=request.user), pub_date = timezone.now())
			q.save()
			for t in tags:
				if len(t) > 0:
					try:
						tn = Tag.objects.get(word=str(t).lower())
					except Tag.DoesNotExist:
						tn = Tag.objects.create(word=str(t).lower())
					q.tags.add(tn)
			up_rating(request, 5)
			return redirect('/')
		else:
			return render(request, 'new_q.html', context)
	else:
		context['form'] = form
	return render(request, 'new_q.html', context)

#add answer
@login_required
def answer(request, question_id):
	if request.POST:
		text = request.POST['answer']
		if(len(text) > 10):
			a = Answer.objects.create(answer_text = text, pub_date = timezone.now(), author = Profile.objects.get(user_id=request.user), question = Question.objects.get( pk = question_id))
			a.save()
			up_rating(request, 3)
	return redirect(reverse('question', kwargs = {'question_id': question_id} ))
	

def login(request):
	context = {}
	context['authors'] = Profile.objects.order_by('-user_rating')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	if request.POST:
		name = request.POST['username']
		password =  request.POST['password']
		user  = auth.authenticate(username=name, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			context['error'] = "Login or password is incorrect"
			return render(request, 'login.html', context )
	return render(request, 'login.html', context)


def logout_view(request):
	auth.logout(request)
	return redirect('/')

def reg(request):
	context = {}
	context['authors'] = Profile.objects.order_by('-user_rating')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	form = ProfileUser()		
	if request.POST:
		form = ProfileUser(request.POST, request.FILES)
		context['form'] = form
		if form.is_valid():
			password =  form.cleaned_data.get('password')
			password2 =  form.cleaned_data.get('passwordSecond')
			if password2 != password:
				context['error'] = "Passwords are different!"
				return render(request, 'register.html', context)
			name = form.cleaned_data.get('username')
			mail = form.cleaned_data.get('mail')
			nick = form.cleaned_data.get('nick')
			ava = form.cleaned_data.get('avatar')
			try:
				u = User.objects.create(username = name, email = mail )
				u.set_password(password)
				u.save()
				p = Profile.objects.create(user_id = u, user_name = nick, user_rating = 5, avatar = ava )
				p.save()
			except:
				context['error'] = "Cann't create user"
				return render(request, 'register.html', context)
			context['title'] = "Congratulations! "
			context['message']='New user has been created successfully! You can login now'
			return render(request, 'message.html', context)
		else:
			return render(request, 'register.html', context)
	else:
		context['form'] = form	
	return render(request, 'register.html', context)

#for fouture search
def search(req):
	context = { }
	query = req.GET.get('query')
	queryset = Question.search.query(query).order_by('@weight')
	pages = pagination(req, latest_question_list)
	context.update(pages)
	return render(req, 'index.html', context)

#user's settings
@login_required
def settings(request):
	context = {}
	context['profile'] = get_user_data(request)
	context['authors'] = Profile.objects.order_by('-user_rating')[:10]
	context['popular_tags'] = Tag.objects.all().values('id', 'word').annotate(Count("question")).order_by('-question__count')[0:5]	
	form = EditProfile()
	if request.POST:
			form = EditProfile(request.POST, request.FILES)
			context['form'] = form
			if form.is_valid():
				p = Profile.objects.get(user_id=request.user.id)
				password =  form.cleaned_data.get('password')
				if password:
					u = User.objects.get(pk = request.user.id)
					password2 =  form.cleaned_data.get('passwordSecond')
					if password2 != password:
						context['error'] = "Passwords are different!"
						return render(request, 'settings.html', context)
					u.set_password(password)
					u.save()
				mail = form.cleaned_data.get('mail')
				ava = form.cleaned_data.get('avatar')
				if mail:
					p.mail = mail
					p.save()
				if ava:
					p.avatar = ava
					p.save()
				context['title'] = "Success!"
				context['message']='Your profile was successfully changed'
				return render(request, 'message.html', context)
			else:
				return render(request, 'settings.html', context)
	context['form'] = form	
	
	return render(request, 'settings.html', context)


@login_required
def like(req):
	pk = req.POST.get('id')
	mark = int(req.POST.get('mark'))
	ptype = int(req.POST.get('ptype'))
	p_change = "#q" + str(pk)
	if ptype == 0:
		p_change = "#q" + str(pk)
	else:
		p_change = "#a" + str(pk)
	new_rate = '0'
	status = False
	try:
		if ptype == 0:
			p = Question.objects.get(id = pk)
		else:
			p = Answer.objects.get(id = pk)
		new_rate = str(p.rating)
		if p.author != req.user.id:
			Vote = VoteForPosts.objects.filter(p_type = ptype).filter(post = pk).filter(voter_id = req.user.id)
			if Vote.count() != 0:
				vote_last = Vote[0].value
			else:
				vote_last = 0
			if mark * vote_last != 1:
				Pr = p.author
				Pr.user_rating += mark
				Pr.save()
				p.rating = p.rating + mark
				if vote_last != 0:
					Vote[0].delete()
				else:
					Vote = VoteForPosts(post = pk, voter_id = req.user.id, value = mark, p_type = ptype)
					Vote.save()
				message = 'Thanks for your vote!'
				p.save()
			else:
				message = 'You cant`t make a double vote!'
			status = True
			new_rate = str(p.rating)
		else:
			message = 'You are not permitted to vote your post!'
	except:
		message = p_change
	import json
	content = json.dumps({'status': status, 'q_change': p_change , 'message': message, 'new_rating': new_rate})

	return HttpResponse(content, content_type = 'application/json')


#this function allow to mark answer as correct
@login_required	
def check_answer(request):
	status = False	
	try:
		pk = request.POST.get('id')
		new_flag = int(request.POST.get('mark'))
		answer = Answer.objects.get(id = pk)				
		answer.flag = new_flag					
		answer.save()		
		if new_flag:
			answers = Answer.objects.filter(question = answer.question)
			print('flag=1')
			for a in answers:
				if a.id != int(pk):
					print(a.id)		
					a.flag = False
					a.save()
		status = True
		message = "You successfully used checkbox!"
	except:
		message = "Sorry, you can't mark this answer"
	import json
	content = json.dumps({'status': status, 'message': message})
	return HttpResponse(content, content_type = 'application/json')

@login_required
def get_user_data(request):
	context = {}
	prop = Profile.objects.get(user_id=request.user.id)
	context["id"] = request.user.id
	context["nickname"] = prop.user_name
	context["avatar"] = prop.avatar
	context["rating"] = prop.user_rating
	return context


def pagination(request, objects):
	context = {}
	limit = 5
	pager = Paginator(objects, limit) 
	page = request.GET.get('page', 1)
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
	context['questions'] = pager.page(page).object_list
	context['pager'] = pager
	context['minPageNum'] = int(page) - 3
	context['maxPageNum'] = int(page) + 3
	return context

#for automatic update of user's rating
@login_required
def up_rating(request, mark):
	prop = Profile.objects.get(user_id=request.user.id)
	prop.user_rating += mark
	prop.save()
	return request
