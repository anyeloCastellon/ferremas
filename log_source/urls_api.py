from rest_framework.routers import DefaultRouter
from django.urls import path, include
from log_source import views_api


router = DefaultRouter()
router.register(r'log_source_power_bi_view_set', views_api.LogSourcePowerByViewSet, basename='log_source_power_bi_view_set')

urlpatterns = [
   	path('', include(router.urls)),
	]