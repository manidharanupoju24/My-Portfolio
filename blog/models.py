from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now=False,auto_now_add=False)
    blogpost = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        summary = self.blogpost[:50] + '......'
        return summary

    def pub_date_modified(self):
        return self.pub_date.strftime('%b %e %Y')

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