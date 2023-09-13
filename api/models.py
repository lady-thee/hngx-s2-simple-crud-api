from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=250, blank=False)
    email = models.CharField(max_length=250, blank=False)
    username = models.CharField(max_length=200, blank=False)
    

    def __str__(self):
        return str(self.name)


{
    "email": "theolam6@gmail.com",
    "name": "Theola",
    "username": "tee-tee"
}

{
    "email": "theolam6@gmail.com",
    "name": "theola",
    "username": "tee-tee"
}