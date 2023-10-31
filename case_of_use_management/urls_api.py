from django.urls import path
from .views_api import CaseOfUseDataView, CaseOfUseDataDynamicCompanyView, CaseOfUseTechnologyCoverageView, CaseOfUseMissingTechnologyView, CaseOfUseRuleTypeCoverageView, CaseOfUseMissingRuleTypeView, CaseOfUseIncidentCoverageView, CaseOfUseMissingIncidentView, CaseOfUseIncidentTypeCoverageView, CaseOfUseMissingIncidentTypeView

urlpatterns = [
    path('case_of_use_data/', CaseOfUseDataView.as_view(), name='case_of_use_data'),
    path('case_of_use_data/unassigned_caseofuse/<int:company_id>/', CaseOfUseDataDynamicCompanyView.as_view(), name='unassigned_caseofuse'),
    path('case_of_use_data/technology_coverage/<int:company_id>/', CaseOfUseTechnologyCoverageView.as_view(), name='technology_coverage'),
    path('case_of_use_data/missing_technology_coverage/<int:company_id>/', CaseOfUseMissingTechnologyView.as_view(), name='missing_technology_coverage'),
    path('case_of_use_data/rule_type_coverage/<int:company_id>/', CaseOfUseRuleTypeCoverageView.as_view(), name='rule_type_coverage'),
    path('case_of_use_data/missing_rule_type_coverage/<int:company_id>/', CaseOfUseMissingRuleTypeView.as_view(), name='missing_rule_type_coverage'),
    path('case_of_use_data/missing_incident_coverage/<int:company_id>/', CaseOfUseIncidentCoverageView.as_view(), name='missing_incident_coverage'),
    path('case_of_use_data/incident_coverage/<int:company_id>/', CaseOfUseMissingIncidentView.as_view(), name='incident_coverage'),
    path('case_of_use_data/incident_type_coverage/<int:company_id>/', CaseOfUseMissingIncidentTypeView.as_view(), name='case_of_use_incident_type_coverage'),
    path('case_of_use_data/missing_incident_type_coverage/<int:company_id>/', CaseOfUseIncidentTypeCoverageView.as_view(), name='case_of_use_missing_incident_type_coverage'),

]