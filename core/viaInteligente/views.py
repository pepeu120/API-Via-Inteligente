from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Acidente, Status
from .serializers import AcidenteSerializer, StatusSerializer


class AcidenteCreateView(viewsets.ModelViewSet):
    queryset = Acidente.objects.all()
    serializer_class = AcidenteSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'criado_por']

    search_fields = ['descricao', 'localizacao']
    ordering_fields = ['criado_em', 'modificado_em']
    ordering = ['criado_em']

    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user,
                        modificado_por=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modificado_por=self.request.user)


class StatusCreateView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nome']
    search_fields = ['nome']
    ordering_fields = ['criado_em', 'modificado_em']
    ordering = ['criado_em']

    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user,
                        modificado_por=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modificado_por=self.request.user)
