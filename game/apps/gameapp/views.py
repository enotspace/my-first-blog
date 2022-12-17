from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from .models import Game

def index(request):
    Game_list=Game.objects.order_by('-pub_date')[:5]
    return render(request, 'game/list.html', {'Game_list':Game_list})

def detail(request, game_id):
    try:
        a= Game.objects.get( id = game_id)
    except:
        raise Http404("Сайт гри не знайдено =(")

    Comment_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'game/detail.html', {'game':a, 'Comment_list': Comment_list})

def leave_comment(request, game_id):
    try:
        a= Game.objects.get( id = game_id)
    except:
        raise Http404("Сайт гри не знайдено =(")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect( reverse('gameapp:detail', args = (a.id,)))