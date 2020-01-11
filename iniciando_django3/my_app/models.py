from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Categoria'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='Sub-título')
    content = models.TextField(verbose_name='Descrição')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='autor')
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Artigo'

    def __str__(self):
        return self.title


class Fernando(models.Model):
    nota = models.FloatField(max_length=255)



