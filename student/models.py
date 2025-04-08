from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=30)
    country_field = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.PositiveIntegerField()




