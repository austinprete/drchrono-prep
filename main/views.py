from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html', None)


def create_user(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    user.save()
    return HttpResponseRedirect(reverse('forms:index'))


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('main:user'))
    else:
        return HttpResponseRedirect(reverse('main:index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))


@login_required
def user(request):
    user = request.user
    return render(request, 'main/user.html', {'request': request, 'user': user, })
