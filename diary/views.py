from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView, DeleteView
from .models import Diary
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from diary.forms import DiaryForm

class AuthorOnly(LoginRequiredMixin, UserPassesTestMixin):
    """
    ユーザーのアクセスを制限するクラス
    """
    def test_func(self):
        """
        投稿の作者とログインしてるユーザーが同じかどうか判定する
        """
        post = self.get_object()
        return post.author == self.request.user
    
    def handle_no_permission(self):
        """
        test_funcでFalseだった場合特定のページにリダイレクトする
        """
        return redirect('posts:detail', pk=self.kwargs['pk'])
    
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
    
class DiaryDetailView(DetailView):
    model = Diary
    template_name = 'diary/diary_detail.html' 
    #DiaryUpdateViewができたらもう一回設定する！
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add the edit URL to the context if the user is authenticated
        if self.request.user.is_authenticated:
            diary_instance = context.get('object')  # This is the default context object name if not specified
            if diary_instance:
                edit_url = reverse(f'admin:{diary_instance._meta.app_label}_{diary_instance._meta.model_name}_change', args=[diary_instance.id])
                # Directly add the edit_url to the context
                context['edit_url'] = edit_url
        return context

class DiaryDeleteView(AuthorOnly, DeleteView):
    """
    投稿削除するHTMLを渡す
    削除成功後投稿一覧ページにリダイレクト
    """
    template_name = 'diary/diary_delete.html'
    model = Diary
    success_url = reverse_lazy('diary:list')