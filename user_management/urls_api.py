from rest_framework.routers import DefaultRouter
from django.urls import path, include
from user_management import views

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
