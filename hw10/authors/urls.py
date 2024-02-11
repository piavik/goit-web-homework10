from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('author/', views.main, name='main'),              # default
    path('author/add/', views.add_author, name='add_author'),   # add author
]