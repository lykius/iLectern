from django.contrib import admin
from .models import Sheet

@admin.register(Sheet)
class SheetAdmin(admin.ModelAdmin):
    fieldsets = [('Music Sheet', {'fields': ['title']})]
    list_display = ['title']
    search_fields = ['title']
