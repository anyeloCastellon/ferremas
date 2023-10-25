from django.urls import path
from .views_api import CaseOfUseDataView

urlpatterns = [
    path('case_of_use_data/', CaseOfUseDataView.as_view(), name='case_of_use_data'),
]