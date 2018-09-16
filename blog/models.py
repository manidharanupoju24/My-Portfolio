from django.db import models


# Create your models here.
class Blog(models.Model):
    blogpost = models.CharField(max_length=1000)
