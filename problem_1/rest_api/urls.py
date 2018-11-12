from django.urls import path, include
from rest_framework import routers
from .views import ClassViewSet, StudentViewSet


router = routers.DefaultRouter()
router.register(r'class', ClassViewSet)
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', include('rest_framework.urls')),
]
