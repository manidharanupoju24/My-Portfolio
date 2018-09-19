from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now=False,auto_now_add=False)
    blogpost = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

# Procedure

# Create a blog model
    #title
    #publication date
    #blogpost
    #image

# add the blog app to the settings

# create a migration

# Migrate

# Add to the admin