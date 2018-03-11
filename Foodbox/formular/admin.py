from django.contrib import admin
from models import Formular


class FormularAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Formular, FormularAdmin)