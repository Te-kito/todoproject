from django.db import models

# Create your models here.

# TODO 左側はtemplateに表示される文字列、みぎは保存されてるデータの中身
PRIORITY = (('danger','high'),('info','normal'),('success','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100) 
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()

    # ? Field どんなモデルなのか,特徴、種類
    # ? CharField は文字列型のField (max_length必須) 
    # ? 選択肢を選択させたい場合、choices=listを使う in CharField
    # ? textField はcharFieldより長い
    # ? 日付はDateFieldが多い

    def __str__(self):
        return self.title
