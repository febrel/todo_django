from django.db import models

# Create your models here.


class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
