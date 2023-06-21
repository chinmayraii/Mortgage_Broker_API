from django.contrib import admin
from . models import *

admin.site.register(Chatbot)
admin.site.register(CustomUser)
admin.site.register(Message)
admin.site.register(Ticket)

admin.site.register(Property)
admin.site.register(Country)

admin.site.register(SituationSearch)
admin.site.register(SituationExisting)
admin.site.register(CurrentCircumstances)
admin.site.register(SourceOfFunds)
admin.site.register(MortgageRequirements)
admin.site.register(Apps)
admin.site.register(Applicant)
admin.site.register(Status)
admin.site.register(Employment)
admin.site.register(Loans)
admin.site.register(AdditionalAssistance)
admin.site.register(Assets)
admin.site.register(AdditionalApplicnats)