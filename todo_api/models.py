from django.db import models


class Todo(models.Model):
    titulo = models.CharField(max_length=250)
    tarefa = models.CharField(max_length=250)
    data = models.DateField()
    concluida = models.BooleanField()

    def __str__(self):
        return self.titulo
    
