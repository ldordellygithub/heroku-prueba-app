from django.contrib import admin
from .models.user import user 
from .models.clientes import clientes
from .models.compra import compra
# Register your models here.

admin.site.register(user)
admin.site.register(clientes)
admin.site.register(compra)
