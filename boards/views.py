from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponse
from datetime import datetime
from django import forms

from .models import Board, List, Task, Comment
from .forms import BoardForm, ListForm, TaskForm, CommentForm

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
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'boards/list_content.html', {'board': board, 'list': list})

def task_content(request, board_id, list_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    list = get_object_or_404(List, pk=list_id)
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'boards/task_content.html', {'board': board, 'list': list, 'task': task})


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

def board_edit(request, board_id):
        board = get_object_or_404(Board, pk=board_id)
        if request.method == "POST":
            form = BoardForm(request.POST, instance=board)
            if form.is_valid():
                board = form.save(commit=False)
                board.creation_date = datetime.now()
                board.save()
                return redirect('/boards/%s/lists/' %board.pk, pk=board.pk)
        else:
            form = BoardForm(instance=board)
        return render(request, 'boards/board_edit.html', {'form': form})

def list_edit(request, board_id, list_id):
        list = get_object_or_404(List, pk=list_id)

        if request.method == "POST":
            form = ListForm(request.POST, instance=list)
            if form.is_valid():
                list = form.save(commit=False)
                board = get_object_or_404(Board, pk=board_id)
                list.board = board
                list.save()
                page = '/boards/' + str(board_id) + '/lists/' + str(list_id)
                return redirect(page, pk=list.pk)
        else:
            form = ListForm(instance=list)
        return render(request, 'boards/list_edit.html', {'form': form})

def board_remove(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.delete()
    return redirect('/boards/')

def list_remove(request, board_id, list_id):
    list = get_object_or_404(List, pk=list_id)
    list.delete()
    return redirect('/boards/%s/lists/' %board_id)

def add_comment_to_task(request, board_id, list_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.created_date = datetime.now()
            comment.save()
            page = '/boards/' + str(board_id) + '/lists/' + str(list_id) + '/tasks/' + str(task_id)
            return redirect(page)
    else:
        form = CommentForm()
    return render(request, 'boards/add_comment_to_task.html', {'form': form})
