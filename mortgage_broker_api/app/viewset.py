from rest_framework import viewsets
from . models import *
from . serializer import *

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer

class SituationSearchViewSet(viewsets.ModelViewSet):
    queryset = SituationSearch.objects.all()
    serializer_class =SituationSearchSerializer

class SituationExistingViewSet(viewsets.ModelViewSet):
    queryset = SituationExisting.objects.all()
    serializer_class = SituationExistingSerializer

class CurrentCircumstancesViewSet(viewsets.ModelViewSet):
    queryset = CurrentCircumstances.objects.all()
    serializer_class = CurrentCircumstancesSerializer

class SourceOfFundsViewSet(viewsets.ModelViewSet):
    queryset = SourceOfFunds.objects.all()
    serializer_class =SourceOfFundsSerializer

class MortgageRequirementsViewSet(viewsets.ModelViewSet):
    queryset = MortgageRequirements.objects.all()
    serializer_class = MortgageRequirementsSerializer

class AppsViewSet(viewsets.ModelViewSet):
    queryset = Apps.objects.all()
    serializer_class = AppsSerializer

class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class EmploymentViewSet(viewsets.ModelViewSet):
    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer

    

class LoansViewSet(viewsets.ModelViewSet):
    queryset = Loans.objects.all()
    serializer_class = LoansSerializer

class AdditionalAssistanceViewSet(viewsets.ModelViewSet):
    queryset = AdditionalAssistance.objects.all()
    serializer_class = AdditionalAssistanceSerializer 

class AssetsViewSet(viewsets.ModelViewSet):
    queryset = Assets.objects.all()
    serializer_class = AssetsSerializer 

class AdditionalApplicnatsViewSet(viewsets.ModelViewSet):
    queryset = AdditionalApplicnats.objects.all()
    serializer_class = AdditionalApplicnatsSerializer                 


