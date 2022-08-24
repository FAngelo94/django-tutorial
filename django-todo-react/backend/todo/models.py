
# todo/models.py      
from urllib import request
from django.db import models

# Create your models here.

# add this
class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField(default="")
  completed = models.BooleanField(default=False)
      
  def __str__(self):
    return self.title