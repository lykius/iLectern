from django.contrib import admin
from .models import Sheet

@admin.register(Sheet)
class SheetAdmin(admin.ModelAdmin):
    fieldsets = [('Music Sheet', {'fields': ['title', 'file_name', 'number_of_pages']})]
    list_display = ('title', 'file_name', 'number_of_pages')
    search_fields = ['title']
