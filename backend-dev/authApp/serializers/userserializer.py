from dataclasses import field, fields
from rest_framework import serializers
from authApp.models.user import user



class userserializer(serializers.modelSerializer):
    class Meta:
        
        models =user
        fields = ('id', 'nombre', 'apellido', 'edad')
        
