from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Acidente, Status
from .serializers import AcidenteSerializer, StatusSerializer


class AcidenteCreateView(viewsets.ModelViewSet):
    queryset = Acidente.objects.all()
    serializer_class = AcidenteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user,
                        modificado_por=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modificado_por=self.request.user)


class StatusCreateView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(criado_por=self.request.user,
                        modificado_por=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modificado_por=self.request.user)
