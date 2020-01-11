from django.db import models


# Create your models here.
# Django ORM
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='Sub-título')
    content = models.TextField(verbose_name='Descrição')

    class Meta:
        verbose_name = 'Artigo'

    def __str__(self):
        return self.title

class Fernando(models.Model):
    nota = models.FloatField(max_length=255)
