from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=45, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'pessoa'
