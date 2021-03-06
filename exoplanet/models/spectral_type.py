from django.db import models
from .star import Star


class SpectralType(models.Model):
    type: models.CharField = models.CharField(max_length=100)

    stars: models.ManyToManyField = models.ManyToManyField(Star)

    class Meta:
        db_table: str = 'spectral_type'
        app_label: str = 'exoplanet'

    def __str__(self) -> str:
        return self.name