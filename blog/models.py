# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Artigo(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField(default=datetime.now)
    
    def __unicode__(self):
        return self.titulo
    
    @models.permalink
    def get_absolute_url(self):
        return ('artigo', (), {'artigo_id':self.id})

