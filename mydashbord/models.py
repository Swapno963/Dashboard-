from django.db import models

# Create your models here.
class dashbordModel(models.Model):
    end_year = models.CharField(max_length=100)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    impact = models.CharField(max_length=100)
    added = models.CharField(max_length=100)
    published = models.DateTimeField()
    country = models.CharField(max_length=100)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    likelihood = models.IntegerField()
    
    def __str__(self):
        return  f"{self.title} {self.sector}"