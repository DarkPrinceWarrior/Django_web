from django.http import HttpResponse
from django.template import loader

from .models import User


def index(request):
    users = User.objects.all()
    template = loader.get_template('photos/index.html')
    context = {
        'user_information': users,
    }
    return HttpResponse(template.render(context, request))
