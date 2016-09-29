from __future__ import unicode_literals
from django.contrib.auth.models import User
from datetime import datetime
from django.db import models

class Board(models.Model):
    board_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date of creation', default=datetime.now, blank=True)
    def __str__(self):
        return self.board_name

class List(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=200)
    def __str__(self):
        return self.list_name

class Task(models.Model):
    task_list = models.ForeignKey(List, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    deadline = models.DateTimeField(default=datetime.now)
    executor = models.ForeignKey(User)
    def __str__(self):
        return self.task_text

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', default = '')
    author = models.ForeignKey(User)
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.text

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
