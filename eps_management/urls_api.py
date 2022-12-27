from rest_framework.routers import DefaultRouter
from django.urls import path, include
from eps_management import views_api


router = DefaultRouter()
router.register(r'eps_viewset', views_api.EPSViewSet, basename='eps_viewset')

urlpatterns = [
   	path('', include(router.urls)),
	]