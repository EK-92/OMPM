from django.db import models

class Tmprtr(models.Model):
  temperature = models.CharField(max_length=10)
  def __str__(self):
    return self.temperature