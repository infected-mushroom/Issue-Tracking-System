from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Board

def index(request):
    boards = Board.objects.order_by('-creation_date')[:5]
    template = loader.get_template('boards/index.html')
    context = {
        'boards': boards,
    }
    return HttpResponse(template.render(context, request))

def board_content(request, board_id):
    return HttpResponse("You're looking at board %s." % board_id)

def list_content(request, board_id, list_id):
    response = "You're looking at list %s."
    return HttpResponse(response % list_id)
