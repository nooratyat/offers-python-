from django.db import models

class Offer(models.Model):
	company_name=models.CharField(max_length=200)
	discription=models.CharField(max_length=200)
	date=models.DateTimeField('date published')

class company(models.Model):
	offer=models.Foreignkey(Offer,on_delete=models.CASCADE)
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	password=models.CharField(max_length=200)