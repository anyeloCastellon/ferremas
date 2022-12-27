from rest_framework.routers import DefaultRouter
from django.urls import path, include
from user_management import views

router = DefaultRouter()
router.register(r'company', views.CompanyViewSet, basename='company')
router.register(r'user_server', views.UserServerViewSet, basename='UserServerViewSet')
router.register(r'user_server_model', views.UserModelServerViewSet, basename='UserServerViewSet')
# router.register(r'geolocate', views.GeolocateViewSet, basename='GeolocateViewSet')
# router.register(r'pathurl', views.PathViewSet, basename='PathViewSet')

urlpatterns = [
    path('', include(router.urls)),
]
