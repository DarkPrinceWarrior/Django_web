from aiogram import Dispatcher, Bot, executor
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .management.commands.startbot import start_message, bot
from .models import User, ImageForm, Bot, BotList_form
import requests


def index(request):
    users = User.objects.all()
    return render(request, template_name='bot/index.html',
                  context={'user_information': users})


def detail(request, user_id):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the templates
            return HttpResponseRedirect(reverse('bot:detail', args=(user_id,)))
    else:
        form = ImageForm()
        user = get_object_or_404(User, pk=user_id)
        return render(request, template_name='bot/detail.html',
                      context={'form': form, 'user': user})


def choose_bot(request):
    # choose a bot from dropdown menu
    form = BotList_form()
    list_bots = Bot.objects.all()
    return render(request, template_name='bot/BotList.html', context={'form': form,
                                                                      "bots_list": list_bots})


async def start_bot(request, token_id):
    # start a bot
    get_bot = requests.get(f'https://api.telegram.org/bot{token_id}/getMe')
    return HttpResponse(f"Results:  {get_bot.json()}")
