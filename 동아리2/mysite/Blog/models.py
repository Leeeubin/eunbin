from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length= 50)
    content = models.TextField()
    score = models.IntegerField()
    dt_created = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.title