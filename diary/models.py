from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

#タイトル、場所、イベント名、イベント種類、内容、いいね、投稿日、写真、投稿者
CHOICE = (('ライブ','ライブ'),('握手会','握手会'),('オンラインイベント','オンラインイベント'),('オフラインイベント','オフラインイベント'),('その他','その他'))

class Diary(models.Model):
    #日記（投稿）に関するモデル
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    event_name = models.CharField(max_length=50)
    event_choice = models.CharField(
        max_length=50,
        choices = CHOICE
        )
    content = models.TextField()
    good_count = models.IntegerField(null=True, blank=True, default=0)
    image = models.ImageField(upload_to="")

class Comment(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.TextField()