from django.db import models
from django import forms
from django.core.files.storage import FileSystemStorage

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








