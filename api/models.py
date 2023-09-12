from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=250, blank=False)
    email = models.CharField(max_length=250, blank=False)
    username = models.CharField(max_length=200, blank=False)
    age = models.PositiveIntegerField()
    track = models.CharField(max_length=150, blank=True)
    occupation = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return str(self.name)
