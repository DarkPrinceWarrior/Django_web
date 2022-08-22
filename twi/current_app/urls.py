from django.urls import path

from . import views

app_name = 'current_app'

urlpatterns = [
    path('', views.index, name='index'),
    # for generic view
    # path('', views.IndexView.as_view(), name='index'),

    # ex: /current_app/5/
    path('user/<int:user_id>/', views.detail, name='detail'),
    # path('user/<int:pk>/', views.DetailView.as_view(), name='detail'),
]