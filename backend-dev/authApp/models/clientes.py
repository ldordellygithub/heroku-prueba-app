from mailbox import NoSuchMailboxError
from django.db import models

#  creation de models  customers


class  clientes(models.Model):
     nombre =  models.CharField(max_length=50)
     apellido =  models.CharField( max_length=50)
     direccion = models.CharField( max_length=50)
     telefono  = models.IntegerField( max_length=20)
     fecha_nacimiento =models.DateField()
     correo =  models.CharField( max_length=50)
     
     
     def __str__(self):
        return self.nombre
    