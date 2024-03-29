from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),              # default
    path('page/<int:page>', views.main, name='main_paginated'),              # next page

    path('add/', views.add_quote, name='add_quote'),   # add quote

    path('tags/add/', views.add_tag, name='add_tag'),
    path('tags/<int:tag_id>/', views.tag_detail, name='tags'),

    path('author/add/', views.add_author, name='add_author'),   # add author
    path('author/<str:author_id>/', views.author_detail, name='author_detail')

]