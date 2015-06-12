from django.conf.urls import patterns, include, url
from django.contrib import admin
from trips.views import hello_world
from trips.views import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'hello', hello_world),
    url(r'^$', home),
)
