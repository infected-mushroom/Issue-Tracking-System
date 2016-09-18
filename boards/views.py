from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponse
from datetime import datetime
from django import forms
#from django.template import loader

from .models import Board, List, Task
from .forms import BoardForm, ListForm, TaskForm

def index(request):
    boards = Board.objects.order_by('-creation_date')[:10]
    context = {
        'boards': boards,
    }
    return render(request, 'boards/index.html', context)


def board_content(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'boards/board_content.html', {'board': board})    

def list_content(request, board_id, list_id):
    list = get_object_or_404(List, pk=list_id)
    return render(request, 'boards/list_content.html', {'list': list})


def board_new(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.creation_date = datetime.now()
            board.save()
            return redirect('/boards/%s/lists/' %board.pk, pk=board.pk)
    else:
        form = BoardForm()
    return render(request, 'boards/board_new.html', {'form': form})

#import pdb;
#pdb.set_trace()
def list_new(request, board_id):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            board = get_object_or_404(Board, pk=board_id)
            list.board = board
            list.save()
            page = '/boards/' + str(board_id) + '/lists/'
            return redirect(page, pk = list.pk)
    else:
        form = ListForm()
    return render(request, 'boards/list_new.html', {'form': form})

def task_new(request, board_id, list_id):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.pub_date = datetime.now()
            task_list = get_object_or_404(List, pk=list_id)
            task.task_list = task_list
            task.save()
            page = '/boards/' + str(board_id) + '/lists/' + str(list_id)
            return redirect(page, pk = task.pk)
        else:
            form = TaskForm()
    return render(request, 'boards/task_new.html', {'form': form})
