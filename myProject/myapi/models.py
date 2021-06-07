from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    # print the name if we ask django to print the name
    def __str__(self):
        return self.name