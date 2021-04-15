from django.contrib import admin
from mysite.models import *

# Register your models here.

@admin.register(PersonalLoan)
class PersonalLoanAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(EmailRecord)
class EmailAdmin(admin.ModelAdmin):
    pass

@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    pass

@admin.register(businessloan)
class BusinessLoanAdmin(admin.ModelAdmin):
    pass

@admin.register(educationloan)
class educationLoanAdmin(admin.ModelAdmin):
    pass

@admin.register(carloan)
class carLoanAdmin(admin.ModelAdmin):
    pass

@admin.register(homeloan)
class homeloanAdmin(admin.ModelAdmin):
    pass

