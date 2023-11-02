from django.urls import path
from .views_api import MyCustomIncidentView

urlpatterns = [
    path('incident_view_summary/<int:company_id>/', MyCustomIncidentView.as_view(), name='my_custom_incident_view'),

]