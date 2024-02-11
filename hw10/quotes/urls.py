from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),              # default
    # path('<int:page>', views.main, name='main_paginated'),              # next page
    path('tag/', views.tag, name='tag'),            # edit tags


    # path('detail/<int:quote_id>', views.detail, name='detail'),
    # path('delete/<int:quote_id>', views.delete_quote, name='delete_quote'),
    # path('delete/<int:tag_id>', views.delete_tag, name='delete_tag'),
]