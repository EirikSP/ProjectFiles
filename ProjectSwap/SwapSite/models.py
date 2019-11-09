from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    item = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.item



