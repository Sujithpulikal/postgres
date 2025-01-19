from django.db import models

class Movieinfo(models.Model):
    title = models.CharField(max_length=250)
    year = models.IntegerField(null=True)
    summary = models.TextField()
    img=models.ImageField(upload_to='Movieinfo')
    
    def __str__(self):
        return self.title
