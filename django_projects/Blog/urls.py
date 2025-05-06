from django.urls import path
from .views import *
url=[
    path('',post_list_view,name='post_list'),
    path('post/<int:pk>/',post_details,name='post_details')
    
]