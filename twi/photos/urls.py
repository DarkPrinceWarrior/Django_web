from django.urls import path

from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /photos/5/
    path('user/<int:user_id>/', views.detail, name='detail'),
]
