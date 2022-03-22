from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=25,
    )
    description = models.TextField()
