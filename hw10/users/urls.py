from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.profile, name='profile'),
    # todo: change pass for authenticated user
    path('password_change/', views.password_reset, name='password_change'),
    # path('password_change/done/', views.password_reset, name='password_change_done'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete')
]