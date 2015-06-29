from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask_smirnova.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('polls2.urls')),
		url(r'^', include('polls2.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

