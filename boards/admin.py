from django.contrib import admin

from .models import Board, List, Task, Comment

admin.site.register(Board)
admin.site.register(List)
admin.site.register(Task)
admin.site.register(Comment)
