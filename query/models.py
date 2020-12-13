from django.db import models


class Query(models.Model):
    url = models.URLField()
