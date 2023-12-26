from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models

class DataModel(models.Model):
    end_year = models.CharField(max_length=255, blank=True)
    intensity = models.IntegerField(blank=True)
    sector = models.CharField(max_length=255,blank=True)
    topic = models.CharField(max_length=255,blank=True)
    insight = models.CharField(max_length=255,blank=True)
    url = models.CharField(blank=True,max_length=500)
    region = models.CharField(max_length=255,blank=True)
    start_year = models.CharField(max_length=255, blank=True)
    impact = models.CharField(max_length=255, blank=True)
    added_string = models.CharField(max_length=255, blank=True)  # Input as string
    published_string = models.CharField(max_length=255, blank = True)  # Input as string
    country = models.CharField(max_length=255,blank=True)
    relevance = models.IntegerField(blank=True)
    pestle = models.CharField(max_length=255,blank=True)
    source = models.CharField(max_length=255,blank=True)
    title = models.CharField(max_length=455,blank=True)
    likelihood = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        # Convert the input strings to datetime objects before saving
        if self.added_string:
            self.added = datetime.strptime(self.added_string, "%B, %d %Y %H:%M:%S")
        if self.published_string:
            self.published = datetime.strptime(self.published_string, "%B, %d %Y %H:%M:%S")
        super().save(*args, **kwargs)
