from django.db import models


class Sheet(models.Model):
    sheet = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
