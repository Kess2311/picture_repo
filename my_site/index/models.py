from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    message = models.TextField()
    read = models.BooleanField(default=False)


