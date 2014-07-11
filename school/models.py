from django.db import models
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.forms import ModelForm
from django.db import connection, models        
from datetime import datetime

from bs4 import BeautifulSoup    
#from chartit import DataPool, Chart

       
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
AVAILABLE_CHOICES = ((True, 'Available'), (False, 'In Use'))



def __unicode__(self):
      return str(self.pk)
      
class User(models.Model):
	username = forms.CharField()
	email = forms.EmailField()
	
	
	
