from django.db import models

# Create your models here.
class dashbordModel(models.Model):
    end_year = models.CharField(max_length=100)
    intensity = models.IntegerField(null=True, blank=True)
    sector = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    insight = models.TextField() # This size may be big str
    url = models.TextField()
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    impact = models.CharField(max_length=100)
    added = models.CharField(max_length=100)
    # published = models.DateTimeField()
    published = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField(max_length=100)
    source = models.TextField()
    title = models.TextField() # This size may be big str
    likelihood = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return  f"{self.title} {self.sector}"