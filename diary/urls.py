from django.contrib import admin
from django.urls import path, include
from .views import DiaryListView



urlpatterns = [
    path('list/', DiaryListView.as_view(), name='list'),
]
