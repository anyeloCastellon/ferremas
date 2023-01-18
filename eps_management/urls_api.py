from rest_framework.routers import DefaultRouter
from django.urls import path, include
from eps_management import views_api


router = DefaultRouter()
router.register(r'eps_viewset', views_api.EPSViewSet, basename='eps_viewset')
router.register(r'eps_powerby_viewset', views_api.EPSPowerByViewSet, basename='eps_powerby_viewset')
router.register(r'eps_log_source_powerby_viewset', views_api.EpsLogSourcePowerByViewSet, basename='eps_log_source_powerby_viewset')
router.register(r'eps_erc_all_mcafee_powerby_vieswset', views_api.EpsERCAllMcafeePowerByViewSet, basename='eps_log_source_powerby_viewset')
router.register(r'eps_erc_minimus_mcafee_powerby_vieswset', views_api.EpsERCMinimusMcafeePowerByViewSet, basename='eps_log_source_powerby_viewset')

urlpatterns = [
   	path('', include(router.urls)),
	]