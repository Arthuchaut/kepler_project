from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from .star import Star
from .publication import Publication
from .body_detection_type import BodyDetectionType
from .mass_detection_type import MassDetectionType
from .radius_detection_type import RadiusDetectionType


class Planet(models.Model):
    class Status(models.TextChoices):
        CONFIRMED: str = 'CONFIRMED'
        CANDIDATE: str = 'CANDIDATE'
        RETRACTED: str = 'RETRACTED'
        CONTROVERSIAL: str = 'CONTROVERSIAL'

    def _year_validator(self, value: int) -> None:
        if 1960 > value > datetime.now().year:
            raise ValidationError(_(f'{value} is not a valid year.'))

    name: models.CharField = models.CharField(max_length=255)
    status: models.CharField = models.CharField(
        max_length=13, choices=Status.choices, default=Status.CANDIDATE
    )
    mass: models.FloatField = models.FloatField(blank=True, null=True)
    mass_sini: models.FloatField = models.FloatField(blank=True, null=True)
    radius: models.FloatField = models.FloatField(blank=True, null=True)
    orbital_periof: models.FloatField = models.FloatField(
        blank=True, null=True
    )
    semi_major_axis: models.FloatField = models.FloatField(
        blank=True, null=True
    )
    eccentricity: models.FloatField = models.FloatField(blank=True, null=True)
    inclination: models.FloatField = models.FloatField(blank=True, null=True)
    angular_distance: models.FloatField = models.FloatField(
        blank=True, null=True
    )
    discovered_year: models.PositiveIntegerField = models.PositiveIntegerField(
        validators=[_year_validator]
    )
    updated_date: models.DateField = models.DateField(auto_now=True)
    omega: models.FloatField = models.FloatField(blank=True, null=True)
    tperi: models.FloatField = models.FloatField(blank=True, null=True)
    tconj: models.FloatField = models.FloatField(blank=True, null=True)
    tzero_tr: models.FloatField = models.FloatField(blank=True, null=True)
    tzero_tr_sec: models.FloatField = models.FloatField(blank=True, null=True)
    lambda_angle: models.FloatField = models.FloatField(blank=True, null=True)
    impact_parameter: models.FloatField = models.FloatField(
        blank=True, null=True
    )
    tzero_vr: models.FloatField = models.FloatField(blank=True, null=True)
    k: models.FloatField = models.FloatField(blank=True, null=True)
    temp_calculated: models.IntegerField = models.IntegerField(
        blank=True, null=True
    )
    temp_measured: models.IntegerField = models.IntegerField(
        blank=True, null=True
    )
    hot_point_lon: models.FloatField = models.FloatField(blank=True, null=True)
    geometric_albedo: models.FloatField = models.FloatField(
        blank=True, null=True
    )
    log_g: models.FloatField = models.FloatField(blank=True, null=True)

    star: models.ForeignKey = models.ForeignKey(
        Star, on_delete=models.DO_NOTHING, blank=True, null=True
    )
    publication: models.ForeignKey = models.ForeignKey(
        Publication, on_delete=models.DO_NOTHING
    )
    body_detection_type: models.ForeignKey = models.ForeignKey(
        BodyDetectionType, on_delete=models.DO_NOTHING
    )
    mass_detection_type: models.ForeignKey = models.ForeignKey(
        MassDetectionType, on_delete=models.DO_NOTHING
    )
    radius_detection_type: models.ForeignKey = models.ForeignKey(
        RadiusDetectionType, on_delete=models.DO_NOTHING
    )

    class Meta:
        db_table: str = 'planet'
        app_label: str = 'exoplanet'

    def __str__(self) -> str:
        return self.name