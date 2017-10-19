# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import CorsiForm
from .models import Corsi

# Create your views here.
class CorsiCreateView(CreateView):
	template_name = 'form.html'
	form_class = CorsiForm



class CorsiListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Corsi.objects.all()
	
class CorsiDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Corsi.objects.all()