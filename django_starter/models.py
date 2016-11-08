from django.db import models

class Task(models.Model):
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
