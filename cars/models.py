from django.db import models

TRANSMISSION_CHOICES = (
	(1, 'механика'),
	(2, 'автомат'),
	(3, 'робот'),
)

class Car(models.Model):
	production = models.CharField(max_length=50)
	model = models.CharField(max_length=50)
	year = models.IntegerField()
	transmission = models.SmallIntegerField(choices=TRANSMISSION_CHOICES)
	color = models.CharField(max_length=20)

	def __str__(self):
		return self.production + ' ' + self.model + ' ' + str(self.year)