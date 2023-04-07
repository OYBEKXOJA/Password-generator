from django.urls import path
from .views import *

urlpatterns=[
    path('',Home,name='home'),
    path('pass/',Password,name='password')
]