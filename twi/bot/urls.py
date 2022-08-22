from django.urls import path

from . import views

app_name = 'bot'

urlpatterns = [
    path('', views.index, name='index'),
    # for generic view
    # path('', views.IndexView.as_view(), name='index'),

    # ex: /bot/5/
    path('user/<int:user_id>/', views.detail, name='detail'),
    # path('user/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
