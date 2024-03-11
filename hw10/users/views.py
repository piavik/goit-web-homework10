from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from .forms import RegisterForm, LoginForm, ProfileForm


def signupuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'users/signup.html', context={"form": form})

    return render(request, 'users/signup.html', context={"form": RegisterForm()})


class SignupView(View):
    template_name = "users/signup.html"
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created')
            return redirect(to='users:login')
        return render(request, self.template_name, {"form": form})
        
        


def loginuser(request):
    if request.user.is_authenticated:
        return redirect(to='quotes:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotes:main')

    return render(request, 'users/login.html', context={"form": LoginForm()})

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='quotes:main')


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