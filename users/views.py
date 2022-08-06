from ast import Return
from atexit import register
from tkinter.tix import Form
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import FormRegister
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def register(request):

    if request.method == "POST":

        form = FormRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Acount build for {username}')
            form.save()
            return redirect('home')

    else:
        form = FormRegister()
    return render(request, 'users/register.html', {'form': form})
