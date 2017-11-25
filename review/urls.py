"""Defines URL patterns for reviews."""
from django.conf.urls import url
from . import views
urlpatterns = [
# Home page
url(r'^review/$', views.index, name='index'),
url(r'^review/allreviews/$', views.allreviews, name='allreviews'),
url(r'^review/save reviews/$', views.save_review, name='save_review'),

        ]