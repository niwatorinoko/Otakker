from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Diary
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DiaryForm

# Create your views here.
class DiaryListView(ListView):
    model = Diary
    template_name = 'diary/list.html'

class DiaryCreateView(LoginRequiredMixin, CreateView):
    template_name = 'diary/diary_create.html'

    def get(self, request):
        diary_form = DiaryForm()
        context = {
            'post_form': diary_form,
        }
        return render(request, 'diary/diary_create.html', context)

    def post(self, request, *args, **kwargs):
        """ 
        Postリクエスト時の処理
        """
        diary_form = DiaryForm(request.POST, prefix='post')
        if diary_form.is_valid():
            # postモデルのオブジェクトを作成
            # commit=Falseでまだデータベースには保存されない
            new_post = diary_form.save(commit=False)
            new_post.author = request.user
            #new_post.good_count = request.
            new_post.save()
            return redirect('diary:list')
        context = {
            'diary_form': diary_form,
        }
        return render(request, 'diary/diary_create.html', context)
    