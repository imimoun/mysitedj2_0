# coding: utf-8
from django.contrib import admin
from api.models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "city", "postal_code", "gender", "uuid")
    ordering = ("last_name", "first_name")
    search_fields = ("first_name", "last_name")


admin.site.register(Client, ClientAdmin)
