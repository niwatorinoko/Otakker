from django.contrib import admin
from django.urls import path, include
from .views import DiaryListView, DiaryCreateView, DiaryDetailView



urlpatterns = [
    path('', DiaryListView.as_view(), name='list'),
    path('diary/detail/<int:pk>', DiaryDetailView.as_view(), name='detail'),
    path('diary/create/', DiaryCreateView.as_view(), name='create'),
]
