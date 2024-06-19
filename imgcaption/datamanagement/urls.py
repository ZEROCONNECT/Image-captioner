from django.urls import path, include
from rest_framework import routers
from .views import ImageDetailViewSet

router = routers.DefaultRouter()
router.register(r'captionImage', ImageDetailViewSet)

IMAGE_CAPTION = router.registry

urlpatterns = [
    path('', include(router.urls)),
]