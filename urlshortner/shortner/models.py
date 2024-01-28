from django.db import models

class short_url(models.Model):
    short_url = models.CharField(max_length=20)
    long_url= models.URLField("URL", unique=True)


