from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.http import HttpResponse
from datetime import datetime
#from django.template import loader

from .models import Board, List
from .forms import BoardForm, ListForm

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
#    response = "You're looking at list %s."
#    return HttpResponse(response % list_id)


def board_new(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.creation_date = datetime.now()
            board.save()
            return redirect('/boards/%s/lists/' %board.pk, pk=board.pk)
#            return redirect('boards/board_content', pk=board.pk)
    else:
        form = BoardForm()
    return render(request, 'boards/board_new.html', {'form': form})

def list_new(request, board_id):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.save()
            return redirect('/boards/%s/lists/%s' %board_id %list.pk, pk=list.pk)
    else:
        form = ListForm()
    return render(request, 'boards/list_new.html', {'form': form})
