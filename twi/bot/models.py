from django import forms
from django.contrib.sites import requests
from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='/media/images')


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


class Bot(models.Model):
    id = models.AutoField(primary_key=True, help_text="Database ID")
    tid = models.IntegerField(null=False, unique=True, editable=False,
                              help_text="Telegram API ID")
    # Change editable to False for token in prod
    token = models.CharField(max_length=46, unique=True, null=False, blank=False,
                             editable=True, help_text="Telegram API Token")
    username = models.CharField(max_length=64, unique=False, null=False, editable=False)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    @staticmethod
    def check_token(token: str) -> bool:
        print(token)
        # https: // api.telegram.org / bot5442595961: AAFW_4y8vesQaPMQZXhrKruPNVXIPTHoauc / getMe
        response = requests.get(f"https://api.telegram.org/bot{token}/getMe")
        if response.status_code == 200:
            return True
        else:
            print(response.status_code)
            raise ValueError("Telegram response status code is not 200 :(")

    # def save(self, *args, **kwargs):
    #     print("ARGS", args)
    #     print("KWARGS", kwargs)
    #     if self.check_token(self.token):
    #         bot = TBot(token=self.token)
    #         self.tid = bot.id
    #         self.username = bot.username
    #         super(Bot, self).save(*args, **kwargs)

    def __str__(self):
        return f"<Bot id: {self.id} tid: {self.tid}>"
