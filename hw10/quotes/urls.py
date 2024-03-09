from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),              # default
    # path('<int:page>', views.main, name='main_paginated'),              # next page
    path('add/', views.add_quote, name='add_quote'),   # add quote
    path('tag/', views.tag, name='tag'),
    path('author/', views.author, name='author'),              # default
    path('author/add/', views.add_author, name='add_author'),   # add author

    path('author_detail/<int:author_id>/', views.author_detail, name='author_detail'),
    path('quote_detail/<int:quote_id>/', views.quote_detail, name='quote_detail'),
]