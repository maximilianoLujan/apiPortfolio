from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    titleProject = models.CharField(max_length=200)
    img = models.TextField()
    branch = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)