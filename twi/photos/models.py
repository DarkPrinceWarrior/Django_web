from django.db import models


class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)

    def dict(self):
        return {
            "login": self.login,
            "password": self.password,
            "email_address": self.email_address,
        }




class Photos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo_path = models.CharField(max_length=200)

    def dict(self):
        return {
            "photo_path": self.photo_path,
        }

