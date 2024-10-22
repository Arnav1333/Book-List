from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField()
    date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title