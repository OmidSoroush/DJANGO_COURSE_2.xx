from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from groups.model import Group, GroupMember



class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'desription')
    model = Group

#details about groups
class SingleGroup(generic.detailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group
