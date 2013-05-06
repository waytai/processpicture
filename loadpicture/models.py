from django.db import models

# Create your models here.
class Mesbook(models.Model):
    mestext = models.CharField(max_length=30)
    mestime = models.CharField(max_length=50)
    def __unicode__(self):
        return self.mestext