from django.db import models

# Create your models here.
class Portfolio(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Subject = models.CharField(max_length=100)
    Description = models.TextField()
    
    def __str__(self):
        return self.Name
