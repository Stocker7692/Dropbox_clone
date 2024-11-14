# files/models.py
from django.db import models

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    content_type = models.CharField(max_length=50)
    size = models.IntegerField()

    def __str__(self):
        return self.name
