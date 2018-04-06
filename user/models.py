from django.db import models


class User(models.Model):
    name = models.TextField(default='')
    email = models.TextField(default='')
    password = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

