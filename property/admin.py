from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_buiding', 'construction_year', 'town')
    list_editable = ['new_buiding']
    list_filter = ['new_buiding']


class ComlaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['appt_complaint_about']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComlaintAdmin)