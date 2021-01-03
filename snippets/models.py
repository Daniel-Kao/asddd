from django.db import models

class Snippet(models.Model):
    name = models.CharField(max_length=150)
