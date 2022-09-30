from django.db import models

# Create your models here.

class user(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad = models.IntegerField()
 
  
    def __str__(self):
        return self.nombre
    
 