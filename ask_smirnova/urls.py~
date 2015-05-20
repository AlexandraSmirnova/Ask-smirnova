from django.conf.urls import patterns, url, include

from polls import views

urlpatterns = patterns('',
    #url(r'^$', views.getparametres, name='getparametres'),
  url(r'^$', views.index, name='index'),
	url(r'^reiting$', views.reiting, name='reiting'),
	url(r'^que/(?P<question_id>[0-9]+)$', views.question, name='question'),
	url(r'^tag/(?P<tag_id>[0-9]+)$', views.tags, name='tag'),
	url(r'^new$', views.new_q, name='new_q'),
	url(r'^login$', views.login, name='login'),
	url(r'^reg$', views.reg, name='reg'),    
)

