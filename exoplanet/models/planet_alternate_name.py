from django.db import models
from .planet import Planet


class PlanetAlternateName(models.Model):
    name: models.CharField = models.CharField(max_length=255)

    planet: models.ForeignKey = models.ForeignKey(
        Planet, on_delete=models.CASCADE
    )

    class Meta:
        db_table: str = 'planet_alternate_name'
        app_label: str = 'exoplanet'

    def __str__(self) -> str:
        return self.name
