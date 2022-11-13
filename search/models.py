from django.db import models

class Search(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_ad = models.DateTimeField()