from django.db import models
from snippets.models import Snippet

class Language(models.Model):
    # snippet = models.ForeignKey(Snippet, related_name='language', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

