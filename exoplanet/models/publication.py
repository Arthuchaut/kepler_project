from django.db import models


class Publication(models.Model):
    support: models.CharField = models.CharField(max_length=255)

    class Meta:
        db_table: str = 'publication'
        app_label: str = 'exoplanet'

    def __str__(self) -> str:
        return self.name