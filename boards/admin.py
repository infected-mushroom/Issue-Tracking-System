from django.contrib import admin

#from .models import Board, List, Comment, UserProfile
from .models import Board, List, Task, Comment, UserProfile

admin.site.register(Board)
admin.site.register(List)
#admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(UserProfile)
