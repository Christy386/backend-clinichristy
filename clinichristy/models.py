from django.db import models

# Create your models here.
class Users(models.Model):
    #minimum user characteristics  
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    typeOf = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    age = models.DateField()

class UserPersonalInfo(models.Model):
    #address
    number = models.IntegerField()
    street = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    #communication info
    phoneNumber = models.IntegerField()
    instagram = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    #user primary key
    userId = models.IntegerField(Users, on_delete=models.CASCADE)

class MedicsData(models.Model):
    #data of medics
    specialization = models.CharField(max_length=100)
    workDays = models.JSONField()
    servicesPerDay = models.IntegerField()
    workStartTime = models.TimeField()
    servicePrice = models.IntegerField()

    #user primary key
    userId = models.ForeignKey(Users, on_delete=models.CASCADE)

class ServiceAgenda(models.Model):
    serviceDay = models.DateField()
    patientId = models.IntegerField()
    medicId = models.IntegerField()
    serviceStatusId = models.IntegerField()

class ServiceStatus(models.Model):
    status = models.CharField(max_length=20)

class ServicesReschedule():
    oldServiceId = models.IntegerField()
    newServiceId = models.IntegerField()

class Queue(models.Model):
    serviceDay = models.DateField()
    patientId = models.IntegerField(Users, on_delete=models.CASCADE)
    medicId = models.IntegerField(Users, on_delete=models.CASCADE)
    registredAt = models.DateTimeField(auto_now_add=True)

class Exams(models.Model):
    patientId = models.IntegerField(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    data = models.JSONField()

