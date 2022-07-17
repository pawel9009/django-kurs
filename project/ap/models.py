from django.db import models

class User(models.Model):
    fm = models.CharField(max_length=50)
    lm = models.CharField(max_length=60)
    email = models.CharField(max_length= 100)

    def __str__(self):
        return self.fm

# Create your models here.
