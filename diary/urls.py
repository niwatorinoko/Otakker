from django.contrib import admin
from django.urls import path, include
from .views import DiaryListView, DiaryCreateView



urlpatterns = [
    path('diary/lists/', DiaryListView.as_view(), name='list'),
    path('diary/create/', DiaryCreateView.as_view(), name='create'),
]
