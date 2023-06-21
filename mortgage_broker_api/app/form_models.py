from django.db import models


PROPERTY_TYPE = (
    ('House', 'House'),
    ('Flat', 'Flat'),
    ('Villa', 'Villa'),
    ('Appartment', 'Appartment'),
    ('Condo', 'Condo'),
    ('Commercial', 'Commercial'),

)

PROPERTY = (
    ('New', 'New'),
    ('Secondhand', 'Secondhand'),

)


COUNTRY = (
    ('India', 'India'),
    ('Anguilla', 'Anguilla'),
    ('Aruba', 'Miss'),
    ('Australia', 'Mx'),
    ('Austria', 'Dr'),
    ('Bahamas', 'Ms'),
    ('Barbados', 'Ind.'),
    ('Belgium', 'Msr'),
    ('Bonaire', 'Mre'),
    ('Bulgaria', 'M'),
    ('Cape Verde', 'Pr'),
    ('Canada', 'M'),
    ('China', 'M'),
    ('Corsica', 'M'),
    ('Costa Rica', 'M')
    ('Cyprus', 'M'),
    ('Dominican Republic', 'M'),
    ('Bulgaria', 'M'),
    ('Bulgaria', 'M'),

)  


class Country(models.Model):
    country_name=models.CharField(max_length=50)

class SituationSearch(models.model):
    search=models.CharField(max_length=100)
    
class SituationExisting(models.Model):
    existing=models.CharField(max_length=100)


class CurrentCircumstances(models.Model):
    hear_my_services=models.CharField(max_length=100)
    situation_regarding_search =models.ForeignKey(SituationSearch, on_delete=models.CASCADE)  
    situation_regarding_existing =models.ForeignKey(SituationExisting, on_delete=models.CASCADE)
    location_country=models.ForeignKey(Country, on_delete=models.CASCADE)
    location_town=models.CharField(max_length=50)  
    postal_address=models.TextField(blank=True, null=True)
    web_link=models.CharField(max_length=50,blank=True, null=True)
    property_type=models.CharField(max_length=50, choices=PROPERTY_TYPE)
    property=models.CharField(max_length=50, choices=PROPERTY,blank=True, null=True)





OPTION = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)  

class SourceOfFunds(models.Model):
    source_of_funds=models.CharField(max_length=50)


class MortgageRequirements(models.Model):
    purchase_price=models.IntegerField()
    currency=models.CharField(max_length=50)
    loan_required=models.IntegerField()
    years=models.IntegerField()
    savings_resources=models.CharField(max_length=50,choices=OPTION)
    source=models.ForeignKey(SourceOfFunds,on_delete=models.CASCADE)
    rent_new_property=models.CharField(max_length=50,choices=OPTION ,blank=True, null=True)
    improvements_in_property=models.CharField(max_length=50,choices=OPTION ,blank=True, null=True)




TITLE = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Miss', 'Miss'),
    ('Mx', 'Mx'),
    ('Dr', 'Dr'),
    ('Ms', 'Ms'),
    ('Ind.', 'Ind.'),
    ('Msr', 'Msr'),
    ('Mre', 'Mre'),
    ('M', 'M'),
    ('Pr', 'Pr'),
)  

class Apps(models.Model):
    apps=models.CharField(max_length=50)

class Applicant(models.Model):
    title=models.CharField(max_length=50,choices=TITLE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    dob = models.DateField(max_length=20)
    marital_status=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    current_residence=models.CharField(max_length=50,blank=True, null=True)
    three_years_address_history_including_dates=models.TextField()
    portfolio_details=models.TextField(blank=True, null=True)
    day_telephone=models.TextField(unique=True)
    home_telephone =models.IntegerField(blank=True, null=True)
    mobile_telephone=models.IntegerField(blank=True, null=True)
    whatsapp_telephone=models.IntegerField(blank=True, null=True)
    apps=models.ForeignKey(Apps, on_delete=models.CASCADE)
    email_address=models.CharField(max_length=50, unique=True)
    skype_address=models.CharField(max_length=50,blank=True, null=True)


class Status(models.model):
    status=models.CharField(max_length=50)

class Employment(models.Model):
    status=models.ForeignKey(Status, on_delete=models.CASCADE)
    employer_name=models.CharField(max_length=50)
    employer_email=models.CharField(max_length=50, unique=True)
    occupation= models.CharField(max_length=50)
    shareholding_percent=models.IntegerField()
    employed_current_company=models.IntegerField(blank=True, null=True)  
    gross_income=  models.IntegerField(blank=True, null=True)
    income_after_tax=  models.IntegerField(blank=True, null=True)
    income_after_tax_and_pension_ANNUM=  models.IntegerField(blank=True, null=True)
    income_after_tax_and_pension_MONTH=  models.IntegerField(blank=True, null=True)
    bonus=  models.IntegerField(blank=True, null=True)

class Loans(models.Model):
    school_fees=models.CharField(max_length=50,choices=OPTION)
    maintenance =models.CharField(max_length=50,choices=OPTION)    
    credit_card=models.CharField(max_length=50,choices=OPTION)    
    other_loans=models.CharField(max_length=50,choices=OPTION)   


class AdditionalAssistance(models.Model):
    assistance=models.CharField(max_length=100)

class Assets(models.Model):
    existing_property=models.TextField(blank=True, null=True)  
    other_savings=models.TextField(blank=True, null=True)
    bad_debts=models.CharField(max_length=50,choices=OPTION,blank=True, null=True) 
    assistance=models.ForeignKey(AdditionalAssistance, on_delete=models.CASCADE,blank=True, null=True)


class AdditionalApplicnats(models.model):
    applicant_form=models.CharField(max_length=50,choices=OPTION)   