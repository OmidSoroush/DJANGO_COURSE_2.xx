from django.urls import path
from mywebapp import views

urlpatterns = [
    path('', views.index, name='index')
]
