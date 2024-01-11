#serializers para validar la data de ingreso y convertir la informacion que se envia.

from rest_framework import serializers
from .models import CategoriaModel


#serializar y validar que informacion input sea correcta
#usamos .ModelSerializer para basarnos en un modelo
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel #modelo a utilizar para hacer el serializador
       # fields = ['id','nombre']
        fields = '__all__'     #campos a ser validados
        # exclude = ['id'] en caso no querer ese