from django.db import models


class User(models.Model):
    username = models.TextField(default='')
    password = models.TextField(default='')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)

