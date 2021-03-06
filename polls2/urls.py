from django.conf.urls import patterns, url, include
from polls2 import views

urlpatterns = patterns('',
  	url(r'^$', views.index, name='index'),
	url(r'^rating$', views.rating, name='rating'),
	url(r'^que/(?P<question_id>[0-9]+)$', views.question, name='question'),
	url(r'^que/(?P<question_id>[0-9]+)/answer$', views.answer, name='answer'),
	url(r'^tag/(?P<tag_id>[0-9]+)$', views.tags, name='tag'),
	url(r'^author/(?P<author_id>[0-9]+)$', views.authors, name='author'),
	url(r'^new$', views.new_q, name='new_q'),
	url(r'^login$', views.login, name='login'),
	url(r'^logout$', views.logout_view, name='logout'),
	url(r'^reg$', views.reg, name='reg'),   
	url(r'^like/$', views.like, name='like'),
	url(r'^edit$', views.settings, name='settings'),
	url(r'^search', views.search, name='search'),
	url(r'^check_answer$', views.check_answer, name='check'), 
)

