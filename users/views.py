from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, CustomUserLoginForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'singupA.html'


def LoginView(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = get_object_or_404(User, username=username)
            login(request, user)
            return redirect('default')

    return render(request, 'login.html', {'form': CustomUserLoginForm()})


def LogoutView(request):
    logout(request)
    return render(request, 'logout.html')
