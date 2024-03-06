from django.shortcuts import render
from django.views.generic import ListView
from .models import Diary

# Create your views here.
class DiaryListView(ListView):
    model = Diary
    template_name = 'diary/list.html'