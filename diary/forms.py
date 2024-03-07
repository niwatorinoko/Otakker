from django import forms

from .models import Diary

class DiaryForm(forms.ModelForm):
    """
    投稿用フォーム
    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = '投稿内容' # labelの文字を変更
    

    body = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input mb-5'
        }
    ))
    """
    
    class Meta:
        model = Diary
        exclude = ['author', 'good_count']
    
    prefix = 'post'
