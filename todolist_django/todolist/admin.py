from django.contrib import admin
from .models import ToDo

# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'todo')
    search_fields = ('todo',)
    list_filter = ('user',)

admin.site.register(ToDo, ToDoAdmin)