from rest_framework.routers import DefaultRouter
from .views import UserInfoViewSet
router = DefaultRouter()
router.register('', UserInfoViewSet, basename='addition')

urlpatterns = router.urls