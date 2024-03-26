from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from .models import Diary
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from diary.forms import DiaryForm
from django.views.generic.edit import FormView


# Create your views here.
class DiaryListView(ListView):
    model = Diary
    template_name = 'diary/list.html'

    # get_querysetメソッドをオーバーライドして、順序を指定
    def get_queryset(self):
        # '-created_at'は作成日時の降順（最新のものが最初）を意味する
        return Diary.objects.order_by('-created_at')

class DiaryCreateView(LoginRequiredMixin, FormView):
    template_name = 'diary/diary_create.html'
    form_class = DiaryForm
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        diary_instance = form.save(commit=False)
        diary_instance.author = self.request.user
        diary_instance.save()
        return super().form_valid(form)