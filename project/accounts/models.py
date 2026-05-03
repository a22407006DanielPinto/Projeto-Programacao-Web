from django.db import models
from django.contrib.auth.models import User

class MagicToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    criado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Token de {self.user.username}"