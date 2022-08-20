from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.regex_helper import Choice

from .models import User


def index(request):
    users = User.objects.all()
    return render(request, template_name='photos/index.html',
                  context={'user_information': users})


def detail(request, user_id):
    # user = User.objects.get(pk=user_id)
    user = get_object_or_404(User, pk=user_id)
    return render(request, template_name='photos/detail.html', context={'user': user})


def some(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    try:
        selected_choice = user.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'photo/detail.html', {
            'question': user,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('photo:results', args=(user.id,)))
