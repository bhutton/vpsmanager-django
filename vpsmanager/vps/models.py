from django.db import models
from django.core.urlresolvers import reverse


class Instance(models.Model):

    name = models.TextField(default='')
    description = models.TextField(default='')
    ram = models.IntegerField(default=0)
    console = models.IntegerField(default=0)
    image = models.IntegerField(default=0)
    path = models.TextField(default='')
    startscript = models.TextField(default='')
    stopscript = models.TextField(default='')
    ip = models.TextField(default='')

    # def __str__(self):
    #     return self.name
    #
    # def get_vps_list(self):
    #     return self.vps_instances

