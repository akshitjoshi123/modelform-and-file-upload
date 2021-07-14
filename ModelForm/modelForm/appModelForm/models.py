from django.db import models

# Create your models here.


class feedback(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name
