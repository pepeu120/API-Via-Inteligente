
from rest_framework import serializers
from .models import Acidente, Status


class AcidenteSerializer(serializers.ModelSerializer):
    criado_por = serializers.StringRelatedField()
    modificado_por = serializers.StringRelatedField()
    status = serializers.StringRelatedField()

    class Meta:
        model = Acidente
        fields = ['url', 'id', 'descricao', 'imagem_base64', 'localizacao',
                  'criado_por', 'modificado_por', 'criado_em', 'modificado_em', 'status',]


class StatusSerializer(serializers.ModelSerializer):
    criado_por = serializers.StringRelatedField()
    modificado_por = serializers.StringRelatedField()

    class Meta:
        model = Status
        fields = ['url', 'nome', 'id', 'criado_por',
                  'modificado_por', 'criado_em', 'modificado_em']
