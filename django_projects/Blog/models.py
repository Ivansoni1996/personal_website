from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self):#this methode means that if i creat an object the object will be seen as it title 
        return self.title

