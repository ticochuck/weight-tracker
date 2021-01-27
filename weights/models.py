from django.db import models
from django.urls import reverse


class Weights(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    date_created = models.DateTimeField()
    weight = models.CharField(max_length=10)
    addinfo = models.TextField(blank=True)


    def __str__(self):
        return f'{self.weight}, {self.date_created}'


    def get_absolute_url(self):
        return reverse('home')