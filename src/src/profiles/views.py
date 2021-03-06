# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView
from django.http import Http404

from restaurants.models import RestaurantLocation
from menus.models import Item

from .forms import RegisterForm
from .models import Profile

from ww import f

User = get_user_model()

def activate_user_view(request, code=None, *args, **kwargs):
	if code:
		qs = Profile.objects.filter(activation_key=code)
		if qs.exists() and qs.count() == 1:
			profile = qs.first()
			if not profile.activated:
				user_ = profile.user
				user_.is_active = True
				user_.save()
				profile.activated = True
				profile.activation_key = None
				profile.save()
				return redirect("/login")
	redirect("/login")
			

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name =  'registration/register.html'
	success_url = '/'
	
	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated():
			return redirect("/logout")
		return super(RegisterView, self).dispatch(*args, **kwargs )

class ProfileFollowToggle(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		#print request.POST
		user_to_toggle = request.POST.get("username")
		name = user_to_toggle.split(' ')[1]
		profile_, is_following = Profile.objects.toggle_follow(request.user, name)
		return redirect('/u/'+profile_.user.username)

# Create your views here.
class ProfileDetailView(DetailView):
	template_name = 'profiles/user.html'	
	def get_object(self):
		username  = self.kwargs.get("username")
		print username		
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)
	
	def get_context_data(self, *args,**kwargs):
		context 				 = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
		query 					= self.request.GET.get('q')
 		user 					= context['user']
		is_following 			= False
		if user.profile in self.request.user.is_following.all():
			is_following 		= True
		print is_following
		context['is_following'] = is_following
		items_exist 			= Item.objects.filter(user=user).exists()
		qs = RestaurantLocation.objects.filter(owner=user).search(query)
		# if query:
		# 	qs = qs. search(query) #just user items
			#qs = RestaurantLocation.objects.search(query) #all items of the query

		if items_exist and qs.exists():
			context['locations']= qs
		return context