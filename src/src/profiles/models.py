# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail 
from django.core.urlresolvers import reverse

from .utils import code_generator

from ww import f

User =  settings.AUTH_USER_MODEL 



class ProfileManager(models.Manager):
	def toggle_follow(self, request_user, username_to_toggle):
		profile_ = Profile.objects.get(user__username__iexact=username_to_toggle)
		user = request_user
		is_following = False
		if user in profile_.followers.all():
			profile_.followers.remove(user)
		else:
			is_following = True
			profile_.followers.add(user)
		return profile_, is_following
	
# Create your models here.
class Profile(models.Model):
	user			= models.OneToOneField(User) 	# user.profile 
	followers		= models.ManyToManyField(User, related_name='is_following', blank=True) 	 	
	#following		= models.ManyToManyField(User, related_name='following', blank=True) 	 	# user.profile__set.all()
	activation_key 	= models.CharField(max_length=120, blank=True, null=True)
	activated		= models.BooleanField(default=False)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	
	objects = ProfileManager()
	
	def __str__(self):
		return self.user.username
	def send_activation_email(self):
		print "Activation"
		if not self.activated: 
			self.activation_key = code_generator()
			self.save()
			path_ = reverse('activate', kwargs={"code":self.activation_key})
			subject = 'Activate Account'
			from_email = settings.DEFAULT_FROM_EMAIL
			message = f("Activate your account here :{path_}")
			recipient_list = [self.user.email]
			print "user email to --> "
			print self.user.email
			html_message = f("<p>Activate your account here :{path_}</p>")
			
			sent_mail = send_mail(
								subject,
								message,
								from_email,
								recipient_list,
								fail_silently=False,
								html_message=html_message
								)
			return sent_mail

		pass
		

def post_save_user_reciver(sender, instance, created, *args, **kwargs):
	if created:
		profile, is_created = Profile.objects.get_or_create(user=instance)
		default_user_profile = Profile.objects.get_or_create(user__id=1)[0] # user__username = username
		default_user_profile.followers.add(instance)
		#default_user_profile.save()
		profile.followers.add(default_user_profile.user)
		profile.followers.add(2)
		
		
post_save.connect(post_save_user_reciver,  sender=User)