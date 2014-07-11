# Create your views here.
from __future__ import division
from django.db.models import Q
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from django.shortcuts import render_to_response
import forms

from django.template import RequestContext, Context , loader
from django.contrib import auth
from django.core.context_processors import csrf


#from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import urllib
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django import template
from django.core.exceptions import ObjectDoesNotExist
from time import clock

import sys
import re, os
import string

from school.settings import PROJECT_ROOT, STATIC_URL


def index(request):
	
	cont = Context({'title': 'homepage', 'page': 'index'})
	return render_to_response('index.html', cont, context_instance=RequestContext(request))


def myClasses(request):
	
	cont = Context({'title': 'myClasses', 'page': 'myClasses', 'myClasses': 1})
	return render_to_response('myClasses.html', cont, context_instance=RequestContext(request))

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	
	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect("/accounts/logggedin/")
	else:
		return HttpResponseRedirect("/accounts/invalid/")


def loggedin(request):
	return render_to_response('loggedin.html', {'full_name': request.user.username})


def invalid_login(request):
	return render_to_response('invalid_login.html')


def logout(request):
	auth.logout(request)
	return  render_to_response('logout.html')
