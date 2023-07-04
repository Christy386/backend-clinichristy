from django.db import models

# Create your models here.
class ServiceAgenda(models.Model):
    #minimum user characteristics  
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    typeOf = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    #address
    number = models.IntegerField()
    street = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    #communication info
    phoneNumber = models.IntegerField()
    instagram = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    #data of medics
    specialization = models.CharField(max_length=100)
    workDays = models.JSONField()
    servicesPerDay = models.IntegerField()
    workStartTime = models.TimeField()

    #service agenda
    serviceDay = models.DateTimeField()
    patient = models.IntegerField()
    medic = models.IntegerField()

