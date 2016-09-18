from django import forms
from .models import Board, List

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('board_name',)

class ListForm(forms.ModelForm):
   # board = forms.ModelChoiceField(queryset=Board.objects.all())
    class Meta:
        model = List
        fields = ('list_name',)
#        fields = ('list_name','board',)
