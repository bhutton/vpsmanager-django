from django.db import models
from django.urls import reverse


# class vps(models.Model):
#     def get_absolute_url(self):
#         return reverse('view_vps', args=[self.id])


class Instance(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    ram = models.IntegerField(default=0)
    console = models.IntegerField(default=0)
    image = models.IntegerField(default=0)
    path = models.TextField(default='')
    start_script = models.TextField(default='')
    stop_script = models.TextField(default='')
    ip = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        unique_together = ('name','path')


