from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor=models.ForeignKey("auth.User")
    titulo=models.CharField(max_length=200)
    texto=models.TextField()
    p_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo
