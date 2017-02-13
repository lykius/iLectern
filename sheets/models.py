from django.db import models

class Sheet(models.Model):
    title = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    number_of_pages = models.IntegerField()
