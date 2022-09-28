from django.db import models
from .clientes import clientes

#  creation de models  customers


class  compra(models.Model):
     total_v =  models.PositiveIntegerField()
     fecha =  models.DateTimeField()
     clientes = models.ForeignKey(clientes,on_delete=models.CASCADE)
     
     
     
    