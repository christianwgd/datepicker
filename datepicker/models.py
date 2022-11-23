from django.db import models


class DatedObject(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=10)
    timestamp = models.DateTimeField()