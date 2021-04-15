from django.db import models
from django.db.models.base import Model


# # Create your models here.
# GENDER_CHOICES = ( 
#    ('GENDER', 'GENDER'), 
#    ('MALE', 'MALE'),
#    ('FEMALE', 'FEMALE'),
#    ('OTHERS', 'OTHERS'),
# )


class PersonalLoan(models.Model):
      your_name = models.CharField(max_length= 50)
      email = models.EmailField(max_length = 300)
      mobile = models.CharField(max_length= 13, null=True)

      def __str__(self):
         return self.your_name
       


class EmailRecord(models.Model):
   email = models.EmailField(null=False, blank=False)

   def __str__(self):
       return self.email


class Contact(models.Model):
   your_name = models.CharField(max_length= 50)
   email = models.EmailField(max_length = 300)
   subject = models.CharField(max_length = 300)
   message = models.CharField(max_length = 500)

   def __str__(self):
       return self.your_name


class CreditCard(models.Model):
   your_name = models.CharField(max_length= 50)
   email = models.EmailField(max_length = 300)
   mobile = models.CharField(max_length= 13, null=True)

   def __str__(self):
       return self.your_name


class businessloan(models.Model):
   your_name = models.CharField(max_length= 50)
   email = models.EmailField(max_length = 300)
   mobile = models.CharField(max_length= 13, null=True)

   def __str__(self):
       return self.your_name

class educationloan(models.Model):
   your_name = models.CharField(max_length= 50)
   email = models.EmailField(max_length = 300)
   mobile = models.CharField(max_length= 13, null=True)

   def __str__(self):
       return self.your_name

class homeloan(models.Model):
   your_name = models.CharField(max_length= 50)
   email = models.EmailField(max_length = 300)
   mobile = models.CharField(max_length= 13, null=True)

   def __str__(self):
       return self.your_name

class carloan(models.Model):
   your_name = models.CharField(max_length= 50)
   email = models.EmailField(max_length = 300)
   mobile = models.CharField(max_length= 13, null=True)

   def __str__(self):
       return self.your_name







   

    
