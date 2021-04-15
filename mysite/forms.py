from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PersonalLoanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PersonalLoanForm, self).__init__(*args, **kwargs)
        print(self.visible_fields, 'self fieldss')
        for field_ in self.visible_fields():
            field_.field.widget.attrs['class'] = 'form-control'
            field_.field.widget.attrs['placeholder'] = field_.field.label

    class Meta:
        model = PersonalLoan
        fields='__all__'


class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        print(self.visible_fields, 'self fieldss')
        for field_ in self.visible_fields():
            field_.field.widget.attrs['class'] = 'form-control'
            field_.field.widget.attrs['placeholder'] = field_.field.label

    class Meta:
        model = Contact
        fields='__all__'


class CreditCardForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CreditCardForm, self).__init__(*args, **kwargs)
        print(self.visible_fields, 'self fieldss')
        for field_ in self.visible_fields():
            field_.field.widget.attrs['class'] = 'form-control'
            field_.field.widget.attrs['placeholder'] = field_.field.label

    class Meta:
        model = CreditCard
        fields='__all__'
    

class businessloanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(businessloanForm, self).__init__(*args, **kwargs)
        print(self.visible_fields, 'self fieldss')
        for field_ in self.visible_fields():
            field_.field.widget.attrs['class'] = 'form-control'
            field_.field.widget.attrs['placeholder'] = field_.field.label

    class Meta:
        model = businessloan
        fields='__all__'

class educationloanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(educationloanForm, self).__init__(*args, **kwargs)
        print(self.visible_fields, 'self fieldss')
        for field_ in self.visible_fields():
            field_.field.widget.attrs['class'] = 'form-control'
            field_.field.widget.attrs['placeholder'] = field_.field.label

    class Meta:
        model = educationloan
        fields='__all__'

class carloanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(carloanForm, self).__init__(*args, **kwargs)
        print(self.visible_fields, 'self fieldss')
        for field_ in self.visible_fields():
            field_.field.widget.attrs['class'] = 'form-control'
            field_.field.widget.attrs['placeholder'] = field_.field.label

    class Meta:
        model = carloan
        fields='__all__'

class homeloanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(homeloanForm, self).__init__(*args, **kwargs)
        print(self.visible_fields, 'self fieldss')
        for field_ in self.visible_fields():
            field_.field.widget.attrs['class'] = 'form-control'
            field_.field.widget.attrs['placeholder'] = field_.field.label

    class Meta:
        model = homeloan
        fields='__all__'