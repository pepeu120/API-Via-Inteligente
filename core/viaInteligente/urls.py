from rest_framework import routers
from .views import AcidenteCreateView, StatusCreateView

router = routers.DefaultRouter()
router.register('acidentes', AcidenteCreateView)
router.register('status', StatusCreateView)
urlpatterns = router.urls
