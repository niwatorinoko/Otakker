from django import forms

from .models import Diary

CHOICE = (('ライブ','ライブ'),('握手会','握手会'),('オンラインイベント','オンラインイベント'),('オフラインイベント','オフラインイベント'),('その他','その他'))

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['title','content','venue','event_name','event_choice','image']
        exclude = ['author', 'good_count']

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = '日記のタイトル'
        self.fields['content'].label = '本文'
        self.fields['venue'].label = '場所'
        self.fields['event_name'].label = 'イベント名'
        self.fields['event_choice'].label = '種類'
        self.fields['image'].label = '写真'

    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input mb-5'
        }
    ))

    content = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input mb-5'
        }
    ))

    venue = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input mb-5',
        }
    ))    
    
    event_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'input mb-5',
        }
    ))

    event_choice = forms.ChoiceField(
        choices = CHOICE,
        widget=forms.Select(
            attrs={
                'class': 'select mb-5'
            }
        ) 
    )

    image = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': 'mb-5'
        }
    ))