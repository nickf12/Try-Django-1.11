# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

User =  settings.AUTH_USER_MODEL 

# Create your models here.
class Corsi(models.Model):
	# Association
	owner 				= models.OneToOneField(User)
	seguono       = models.ManyToManyField(User, related_name='seguiti', blank=True)
	
	# Model stuff
	name 		= models.CharField(max_length=120)
	description 		= models.CharField(max_length=120)
	contents	= models.TextField(help_text='separate each item by comma')
	
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	
	def get_absolute_url(self):
		#return f('/restaurants/{self.slug}')
		return reverse('corsi:detail', kwargs={"pk":self.pk})
