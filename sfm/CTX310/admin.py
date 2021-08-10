from django.contrib import admin


from .models import *

# admin.site.register(Instruction)
# admin.site.register(Manual)
# admin.site.register(Circuit)
# admin.site.register(Catalog)

@admin.register(Instruction)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("operation", "title", "date",)
    list_filter = ("date",)

    search_fields = ("operation",)


@admin.register(Manual)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("operation", "title", "date")
    list_filter = ("date",)

    search_fields = ("operation",)


@admin.register(Circuit)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("operation", "title", "date")
    list_filter = ("date",)

    search_fields = ("operation",)


@admin.register(Catalog)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("operation", "title", "date")
    list_filter = ("date",)

    search_fields = ("operation",)
