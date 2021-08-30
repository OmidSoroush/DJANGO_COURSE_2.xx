from django.contrib import admin
from . import models
# Register your models here.


class GroupMemberInline(admin.TablularInline):
    model = models.GroupMember

admin.site.register(models.Group)
