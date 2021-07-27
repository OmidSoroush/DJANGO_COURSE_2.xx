from django.urls import path
from thirdapp import views

urlpatterns = [
    path('', views.index, name='index')
]
