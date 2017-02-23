from django.db import models

class Sheet(models.Model):
    title = models.CharField(max_length=255)
