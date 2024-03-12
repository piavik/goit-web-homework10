from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from .forms import RegisterForm, LoginForm, ProfileForm


class SignupView(generic.CreateView):
    template_name = "users/signup.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:login")

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:profile')

    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'profile_form': profile_form})

# @login_required
# def password_change(request):
#     ...

# @login_required
# def password_change_done(request):
#     ...
    
def password_reset(request):
    ...
    
def password_reset_done(request):
    ...

def password_reset_confirm(request):
    ...
    
def password_reset_complete(request):
    ...