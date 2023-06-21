"""
URL configuration for mortgage_broker_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.viewset import *
from rest_framework.routers import DefaultRouter
from app import views


router= DefaultRouter()
router.register(r'property', PropertyViewSet , basename='property')
router.register(r'country', CountryViewSet, basename='country')
router.register(r'propertytype', PropertyTypeViewSet, basename='Propertytype')
router.register(r'situationsearch', SituationSearchViewSet, basename='situationsearch')
router.register(r'situationexisting', SituationExistingViewSet, basename='situationexisting')
router.register(r'currentcircumstances', CurrentCircumstancesViewSet, basename='currentcircumstances')
router.register(r'sourceoffunds', SourceOfFundsViewSet, basename='sourceoffunds')
router.register(r'mortgagerequirements', MortgageRequirementsViewSet, basename='mortgagerequirements')
router.register(r'apps', AppsViewSet, basename='apps')
router.register(r'applicant', ApplicantViewSet, basename='applicant')
router.register(r'status', StatusViewSet, basename='status')
router.register(r'employment', EmploymentViewSet, basename='employment')
router.register(r'loans', LoansViewSet, basename='loans')
router.register(r'additionalassistance', AdditionalAssistanceViewSet, basename='additionalassistance')
router.register(r'assets', AssetsViewSet, basename='assets')
router.register(r'additionalapplicants', AdditionalApplicnatsViewSet, basename='additionalapplicants')




urlpatterns = [
    path("admin/", admin.site.urls),
    path('',include('app.urls')),
    path('formapi/', include(router.urls)),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf'))
]
