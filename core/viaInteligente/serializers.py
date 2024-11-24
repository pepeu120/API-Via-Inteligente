
from rest_framework import serializers
from .models import Acidente, Status

class AcidenteSerializer(serializers.ModelSerializer):
    usuario= serializers.StringRelatedField()
    status=serializers.StringRelatedField()
    class Meta:
        model = Acidente
        fields = ['url', 'id', 'descricao', 'imagem_base64', 'localizacao', 'usuario', 'data_hora', 'status',]

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model= Status
        fields= ['url', 'nome', 'id']


