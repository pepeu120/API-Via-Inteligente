from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import AcidenteCreateView, StatusCreateView
from .routers import CustomRouter

router = CustomRouter()
router.register('acidentes', AcidenteCreateView, basename='acidente')
router.register('status', StatusCreateView, basename='status')

router.add_extra_route('schema', 'schema')
router.add_extra_route('docs', 'swagger-ui')

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

urlpatterns += router.urls
