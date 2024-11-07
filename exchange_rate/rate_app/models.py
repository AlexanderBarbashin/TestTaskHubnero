from django.db import models


class Rate(models.Model):
    """Модель курса. Родитель: Model."""

    rate = models.FloatField()

    class Meta:
        ordering = ['-id']