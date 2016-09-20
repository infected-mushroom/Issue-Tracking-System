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
        fields = ('task_text', 'deadline')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

'''class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))'''
