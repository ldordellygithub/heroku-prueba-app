
from rest_framework import viewsets, permissions
from authApp.models.user import user
from authApp.serializers.userserializer import userserializer


##  creacion de  vista 
class create(viewsets.ModelViewSet):

    queryset = user.objects.all()
    serializer_class = userserializer
    permissions_classes = [permissions.AllowAny]
