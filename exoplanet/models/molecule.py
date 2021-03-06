from django.db import models
from .planet import Planet


class Modecule(models.Model):
    structure: models.CharField = models.CharField(max_length=100)
    planets: models.ManyToManyField = models.ManyToManyField(Planet)

    class Meta:
        db_table: str = 'molecule'
        app_label: str = 'exoplanet'

    def __str__(self) -> str:
        return self.name