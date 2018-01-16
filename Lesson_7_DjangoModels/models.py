# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'User'
    User_NickName = models.CharField(max_length=200)
    User_FIO = models.CharField(max_length=200)
    User_DateReg = models.DateTimeField()



class Post(models.Model):
    class Meta:
        db_table = 'Post'
    Post_Title = models.CharField(max_length=200)
    Post_Text = models.TextField()
    Post_DatePub = models.DateTimeField()
    User_Id = models.ForeignKey('User',on_delete=models.CASCADE)

class Comment(models.Model):
    class Meta:
        db_table = 'Comment'
    Comment_Text = models.TextField()
    User_Id = models.ForeignKey('User',on_delete=models.CASCADE)
    Post_Id = models.ForeignKey('Post',on_delete=models.CASCADE)

