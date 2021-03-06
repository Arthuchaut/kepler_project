from django.db import models
from .body_detection_type import BodyDetectionType


class Star(models.Model):
    name: models.CharField = models.CharField(max_length=255)
    right_ascension: models.FloatField = models.FloatField(
        blank=True, null=True
    )
    declination: models.FloatField = models.FloatField(blank=True, null=True)
    mag_v: models.FloatField = models.FloatField(blank=True, null=True)
    mag_i: models.FloatField = models.FloatField(blank=True, null=True)
    mag_j: models.FloatField = models.FloatField(blank=True, null=True)
    mag_h: models.FloatField = models.FloatField(blank=True, null=True)
    mag_k: models.FloatField = models.FloatField(blank=True, null=True)
    distance: models.FloatField = models.FloatField(
        blank=True, null=True
    )  # Distance between observer to the star.
    metallicity: models.FloatField = models.FloatField(blank=True, null=True)
    mass: models.FloatField = models.FloatField(blank=True, null=True)
    radius: models.FloatField = models.FloatField(blank=True, null=True)
    age: models.FloatField = models.FloatField(blank=True, null=True)
    temp_effective: models.FloatField = models.FloatField(
        blank=True, null=True
    )
    has_magnetic_field: models.BooleanField = models.BooleanField(
        blank=True, null=True
    )

    body_detection_type: models.ForeignKey = models.ForeignKey(
        BodyDetectionType, on_delete=models.DO_NOTHING
    )

    class Meta:
        db_table: str = 'star'
        app_label: str = 'exoplanet'

    def __str__(self) -> str:
        return self.name