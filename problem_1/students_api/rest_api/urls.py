"""
@author  : Santiago Quiroga Turdera
@version : 1.0
"""


from django.urls import path, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from .views import ClassViewSet, StudentViewSet


schema_view = get_schema_view(title='Students-Classes API')
schema_view_swagg = get_swagger_view(title='Students-Classes API')


router = routers.DefaultRouter()
router.register(r'class', ClassViewSet)
router.register(r'student', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', include('rest_framework.urls')),
    path('schema/', schema_view),
    path('swagger/', schema_view_swagg),
]
