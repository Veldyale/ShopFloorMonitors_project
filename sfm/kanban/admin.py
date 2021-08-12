from django.contrib import admin


from .models import *


@admin.register(Item)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("baan_id", "title", "iso", "diameter", "length", "height","strength", "assembly_place",)
    list_filter = ("iso", "title", "diameter", "length", "strength", "height", "assembly_place",)

    search_fields = ("baan_id", "title", "iso", "diameter", "length", "height", "strength", "assembly_place", "assembly_place",)