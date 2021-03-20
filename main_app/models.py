from django.db import models
from authenticate.models import User
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Food_Pack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,  null=False)
    description = models.CharField(max_length=255,  null=False)
    categories = ArrayField(
            models.CharField(max_length=255, blank=True),
            size=8,
        )
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    is_halal = models.BooleanField(default=False)
    is_kosher = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)



