from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=255)
    population = models.BigIntegerField(null=True, blank=True)  # Some planets might not have a known population.
    terrains = models.TextField()
    climates = models.TextField()

    def __str__(self):
        return self.name
