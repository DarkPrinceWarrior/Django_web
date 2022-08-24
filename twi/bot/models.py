from django import forms
from django.core.files.storage import FileSystemStorage
from django.db import models
import requests
from aiogram import Bot as Tbot
from requests import Response

fs = FileSystemStorage(location='/media/images')

# for the bot
STOPPED = 0
RUNNING = 1

BOT_STATUS_CHOICES = (
    (RUNNING, 'Running'),
    (STOPPED, 'Stopped'),
)


class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)

    def __str__(self):
        return self.login

    def dict(self):
        return {
            "login": self.login,
            "password": self.password,
            "email_address": self.email_address,
        }


class Photos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', default=None)


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = Photos
        fields = ('user', 'image')

# {"ok":true,"result":{"id":5442595961,"is_bot":true,"first_name":"two_bot","username":"twi_safaev_bot",
#                      "can_join_groups":true,"can_read_all_group_messages":false,"supports_inline_queries":false}}

class Bot(models.Model):
    class Meta:
        db_table = 'bots'

    id = models.AutoField(primary_key=True, help_text="Database ID")
    tid = models.IntegerField(null=False, unique=True, editable=False,
                              help_text="Telegram API ID")
    # Change editable to False for token in prod
    token = models.CharField(max_length=46, unique=True, null=False, blank=False,
                             editable=True, help_text="Telegram API Token")
    username = models.CharField(max_length=64, unique=False, null=False, editable=False)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.IntegerField(choices=BOT_STATUS_CHOICES, default=STOPPED)

    @staticmethod
    def check_token(token: str) -> Response:
        print(token)
        response = requests.get(f"https://api.telegram.org/bot{token}/getMe")
        if response.status_code == 200:
            return response
        else:
            print(response.status_code)
            raise ValueError("Telegram response status code is not 200 :(")

    def save(self, *args, **kwargs):
        print("ARGS", args)
        print("KWARGS", kwargs)
        response = self.check_token(str(self.token))
        if response.status_code:
            bot = Tbot(token=str(self.token))
            self.tid = bot.id
            bot_json = response.json()
            self.username = bot_json['result']['username']
            super(Bot, self).save(*args, **kwargs)

    def __str__(self):
        return f"<Bot id: {self.id} tid: {self.tid}>"


class BotList_form(forms.ModelForm):
    """Form for the Bot model"""

    class Meta:
        model = Bot
        fields = ['token']
