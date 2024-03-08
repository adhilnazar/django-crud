from django.db import models

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 220)

    def __str__(self):
        return self.first_name