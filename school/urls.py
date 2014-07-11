from django.conf.urls import patterns, include, url
from school.views import index
from school.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testfarmArch.views.home', name='home'),
    # url(r'^testfarmArch/', include('testfarmArch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'school.views.index'),
    url(r'^myClasses/$', 'school.views.myClasses'),
    url(r'^accounts/login/$', 'school.views.login'),
    url(r'^accounts/auth/$', 'school.views.auth_view'),
    url(r'^accounts/logout/$', 'school.views.logout'),
    url(r'^accounts/logggedin/$', 'school.views.loggedin'),
    url(r'^accounts/invalid/$', 'school.views.invalid_login'),
    
    
)
