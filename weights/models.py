from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Weights(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    weight = models.CharField(max_length=6)

    def __str__(self):
        return f'{self.weight}, {self.date_created}, {self.time}'


    def get_absolute_url(self):
        return reverse('home')