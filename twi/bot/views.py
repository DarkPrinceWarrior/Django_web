from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, ImageForm


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
            # Get the current instance object to display in the template
            return HttpResponseRedirect(reverse('bot:detail', args=(user_id,)))
    else:
        form = ImageForm()
        user = get_object_or_404(User, pk=user_id)
        return render(request, template_name='bot/detail.html',
                      context={'form': form, 'user': user})
