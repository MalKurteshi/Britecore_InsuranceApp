from django.db import models
from django.contrib.auth.models import User

class RegUser(models.Model):
    RegUser_name = models.CharField(max_length=50, blank=False)
    RegUser_surname = models.CharField(max_length=50, blank=False)
    RegUser_email = models.CharField(max_length=20, blank=False)
    RegUser_username = models.CharField(primary_key = True, max_length=15, blank=False)
    RegUser_birthday = models.DateField()
    RegUser_photo = models.URLField(blank=False) 
    RegUser_streetaddress = models.CharField(max_length=50, blank=False)
    RegUser_city = models.CharField(max_length=50, blank=False)
    RegUser_contry = models.CharField(max_length=50, blank=False)
    RegUser_zipcode = models.IntegerField()
    RegUser_password = models.CharField(max_length=15, blank=False)
    RegUser_created_at = models.DateTimeField(auto_now_add=True)


class RegPolicies(models.Model):
    RegPolicies_id = models.AutoField( primary_key = True)
    RegPolicies_username =  models.ForeignKey(RegUser, on_delete=models.CASCADE)
    RegPolicies_type = models.CharField(max_length=50, blank=False)
    RegPolicies_startdate = models.DateField()
    RegPolicies_enddate = models.DateField()
    RegPolicies_previouslyInsured = models.CharField(max_length=50, blank=False)
    RegPolicies_previouslyDamaged = models.CharField(max_length=50, blank=False)
    RegPolicies_Bday_YearOfProduction = models.DateField()
    RegPolicies_costOfProduct = models.DecimalField(max_digits=19, decimal_places=2)
    RegPolicies_description = models.CharField(max_length=50, blank=False)

