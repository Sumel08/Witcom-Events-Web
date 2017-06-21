from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User as UserAuth

# Create your models here.

class Event(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=25)
     code = models.CharField(max_length=10)
     description = models.CharField(max_length=250)
     date_created = models.DateTimeField(default=datetime.now())
     start_date = models.DateTimeField()
     end_date = models.DateTimeField()
     #event_image = models.ForeignKey(Image, to_field='id')
     #sketch = models.ForeignKey(Image, to_field='id')
     #place = models.ForeignKey(Place, to_field='id')
     #schedule = models.ForeignKey(Schedule, to_field='id')
     auth = models.ForeignKey(UserAuth, to_field='id')