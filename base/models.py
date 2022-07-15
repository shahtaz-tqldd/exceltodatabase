from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length = 50)
	email = models.EmailField()
	phone = models.CharField(max_length = 30)

	def __str__(self):
		return self.name