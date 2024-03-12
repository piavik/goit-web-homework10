from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .views import profile, SignupView
from .forms import RegisterForm, LoginForm

app_name = 'users'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path("login/", 
        LoginView.as_view(
            template_name="users/login.html",
            authentication_form=LoginForm,
            redirect_authenticated_user=True,
            ),
        name="login",
        ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/', profile, name='profile'),
    path('password_change/', 
        PasswordChangeView.as_view(
            template_name="users/password_change.html",
            # form_class=PasswordChangeForm,  # this is default
            ),
        name='password_change'
        ),
    path('password_change/done/', 
        PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html",
            ), 
        name='password_change_done'
        ),
    path('password_reset/', 
        PasswordResetView.as_view(
            template_name="users/password_reset.html",
            email_template_name="users/password_reset_email.html",
            success_url = reverse_lazy('users:password_reset_done')
            ),
        name='password_reset'
        ),
    path('password_reset/done/', 
        PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html",
            ), 
        name='password_reset_done'
        ),
    path('reset/<uidb64>/<token>/', 
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url = reverse_lazy('users:password_reset_complete')
            ),
        name='password_reset_confirm'
        ),
    path('reset/done/',
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html",
            ), 
        name='password_reset_complete'
        )
]       