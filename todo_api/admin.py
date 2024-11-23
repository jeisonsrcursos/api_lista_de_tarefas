from django.contrib import admin
from todo_api.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'tarefa', 'data', 'concluida')