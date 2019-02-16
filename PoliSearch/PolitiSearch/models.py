from django.db import models

# Create your models here.

class Voters(models.Model):
	name = models.CharField(max_length=200)
	party = models.CharField(max_length=200)
	