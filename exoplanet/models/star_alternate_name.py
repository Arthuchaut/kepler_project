from django.db import models
from .star import Star


class StarAlternateName(models.Model):
    name: models.CharField = models.CharField(max_length=255)

    star: models.ForeignKey = models.ForeignKey(Star, on_delete=models.CASCADE)

    class Meta:
        db_table: str = 'star_alternate_name'
        app_label: str = 'exoplanet'

    def __str__(self) -> str:
        return self.name