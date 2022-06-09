from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Дело'
        verbose_name_plural = 'Дела'

    def __str__(self):
        return str(self.todo)