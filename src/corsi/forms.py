from django import forms

from restaurants.models import RestaurantLocation

from .models import Corsi

class CorsiForm(forms.ModelForm):
	class Meta:
		model = Corsi
		fields = [
			'name',
			'description',
			'contents',
		]