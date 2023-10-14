from django.db import models
from django.contrib.auth import get_user_model


class Dictionary(models.Model):
    name = models.CharField(max_length=30)
    data = models.TextField(max_length=1000)
    holder = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='dictionaries'
    )
