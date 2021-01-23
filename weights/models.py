from django.db import models
from django.urls import reverse


class Weights(models.Model):
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    weight = models.CharField(max_length=10)
    addinfo = models.TextField()


    def __str__(self):
        return f'{self.weight}'


    def get_absolute_url(self):
        return reverse('home')