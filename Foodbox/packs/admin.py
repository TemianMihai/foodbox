from django.contrib import admin
from models import Packs


class PacksAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Packs, PacksAdmin)