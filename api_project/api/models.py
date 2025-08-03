from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=255)
    author= models.CharField(max_length=255)


    def _str_(self):
        return f"{self.title} by {self.author}"     
    