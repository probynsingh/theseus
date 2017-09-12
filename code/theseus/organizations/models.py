from django.db import models
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(verbose_name="Company Name", max_length=100)
    created_at = models.DateTimeField(verbose_name="Created At")
    updated_at = models.DateTimeField(verbose_name="Last Updated")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
