from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import mail
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from forms.models import Form


@login_required
def index(request):
    user = request.user
    forms = user.form_set.all()
    return render(request, 'forms/index.html', {'request': request, 'forms': forms,})


def new_user(request):
    return render(request, 'forms/newuser.html', None)


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
            return HttpResponseRedirect(reverse('forms:user', args=(user.id,)))
    else:
        return HttpResponseRedirect(reverse('forms:index'))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('forms:index'))


@login_required
def new_form(request):
    user = request.user
    return render(request, 'forms/newform.html', {'request': request, 'user': user, })


@login_required
def create_form(request):
    user = request.user
    form = user.form_set.create(name=request.POST['name'], description=request.POST['description'])
    form.save()
    return HttpResponseRedirect(reverse('forms:form', args=(form.id,)))


@login_required
def form(request, form_id):
    user = request.user
    form = Form.objects.filter(user=user, pk=form_id)[0]
    elements = form.element_set.all()
    return render(request, 'forms/form.html', {'request': request, 'user': user, 'form': form, 'elements': elements})


@login_required
def add_element(request, form_id):
    user = request.user
    form = Form.objects.filter(user=user, pk=form_id)[0]
    element = form.element_set.create(name=request.POST['name'], type=request.POST['type'])
    element.save()
    return HttpResponseRedirect(reverse('forms:form', args=(form.id,)))


def view_form(request, form_id):
    form = get_object_or_404(Form, pk=form_id)
    elements = form.element_set.all()
    return render(request, 'forms/view_form.html', {'request': request, 'form': form, 'elements': elements, })


@login_required
def share_form(request, form_id):
    user = request.user
    link = "http://" + request.get_host() + reverse('forms:view_form', args=(form_id,))
    connection = mail.get_connection()
    send_mail('Form Designer: Shared form from ' + user.username, request.POST['message'] + '\n\n' + link, user.email, [request.POST['to_email']], connection=connection)
    connection.close()
    return HttpResponseRedirect(reverse('forms:form', args=(form_id,)))
