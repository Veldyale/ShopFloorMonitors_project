from django.contrib import admin


from .models import *


@admin.register(Item)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("baan_id", "title", "iso", "size", "assembly_place",)
    list_filter = ("iso", "title", "size", "assembly_place",)

    search_fields = ("baan_id", "title", "iso", "size", "assembly_place",)