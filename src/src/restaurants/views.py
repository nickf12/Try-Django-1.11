# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

from ww import f

from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

class RestaurantListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)
	
	# def get_object(self, *args, **kwargs):
	# 	rest_id = self.kwargs.get('rest_id')
	#  	obj = get_object_or_404(RestaurantLocation, id=rest_id)
	# 	print obj.slug
	#  	return obj
	# 

class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/'
	template_name = 'form.html'
	#success_url = "/restaurants/"
	
	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestaurantCreateView, self).form_valid(form)
	
	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Create Restaurant'
		return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/'
	template_name = 'restaurants/detail-update.html'
	#success_url = "/restaurants/"
	
	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = f('Update Restaurant: {self.get_object().name}')
		return context
	
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)












# Create your views here.
#function base view
# class HomeView(TemplateView):
# 	template_name = 'home.html'
# 	
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(HomeView, self).get_context_data(*args, **kwargs)
# 		context = {
# 		  "html_var" : "context variable"
# 		}
# 		print context
# 		return context
# 
# class AboutView(TemplateView):
# 	template_name = 'about.html'	
# 	
# class ContactView(TemplateView):
# 	template_name = 'contact.html'
	
	
	
	