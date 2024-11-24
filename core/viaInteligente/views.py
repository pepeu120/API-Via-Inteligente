from rest_framework import viewsets, views
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
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


class SchemaView(views.APIView):
    def get(self, request, *args, **kwargs):
        return SpectacularAPIView.as_view()(request._request)


class SwaggerView(views.APIView):
    def get(self, request, *args, **kwargs):
        return SpectacularSwaggerView.as_view(url_name='schema')(request._request)
