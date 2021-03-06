from django.db import models


class MassDetectionType(models.Model):
    type: models.CharField = models.CharField(max_length=100)

    class Meta:
        db_table: str = 'mass_detection_type'
        app_label: str = 'exoplanet'

    def __str__(self) -> str:
        return self.name