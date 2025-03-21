from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, PhotoViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
