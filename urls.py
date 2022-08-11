from django.urls import re_path, include
from noteTaker import views

urlpatterns=[
    re_path(r'^notes/$', views.noteApi),
    re_path(r'^notes/([0-9]+)$', views.noteApi),
]