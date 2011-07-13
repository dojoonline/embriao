# -*- coding: utf-8 -*-
from django.db import models

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField()

    def __unicode__(self):
        return self.titulo
