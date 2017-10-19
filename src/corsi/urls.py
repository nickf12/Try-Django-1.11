from django.conf.urls import url

from .views import (
	CorsiCreateView,
	CorsiListView,
	CorsiDetailView
)

urlpatterns = [
	url(r'^$' , CorsiListView.as_view(), name='list'),
	url(r'^create/$', CorsiCreateView.as_view(), name='create'),
	url(r'^ (?P<pk>\d+)/$', CorsiDetailView .as_view(), name='detail'),
	#url(r'^ (?P<pk>\d+)/edit/$', ItemUpdateView .as_view(), name='edit'),
]