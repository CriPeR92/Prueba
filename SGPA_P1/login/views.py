#views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
 
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    if request.user.is_superuser:
        return render_to_response(
        '/admin', { 'user': request.user })
    else:
        return render_to_response(
        'home.html', { 'user': request.user }
    )
          
def modulo2(request):
        return render_to_response(
        'Menus/Administrar_Usuarios.html',
    )
def modulo3(request):
        return render_to_response(
        'Menus/moduloAdministrador.html',
    )
def modulo(request):
   return HttpResponseRedirect('Administrar_Usuarios')