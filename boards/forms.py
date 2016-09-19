from django import forms
from .models import Board, List, Task, Comment

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('board_name',)

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('list_name',)
#        fields = ('list_name','board',)

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task_text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
