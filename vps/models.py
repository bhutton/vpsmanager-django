from django.db import models
# from django.urls import reverse


class Instance(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    memory = models.IntegerField(default=0)
    bridge = models.IntegerField(default=0)
    console = models.IntegerField(default=0)
    image = models.IntegerField(default=0)
    path = models.TextField(default='')
    start_script = models.TextField(default='')
    stop_script = models.TextField(default='')
    create_disk = models.BooleanField(default=False)
    create_path = models.BooleanField(default=False)
    status = models.TextField(default='Stopped')
    ip = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        # unique_together = ('name','path')


class Disk(models.Model):
    name = models.TextField(default='')
    size = models.IntegerField(default=20)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

class Network(models.Model):
    name = models.TextField(default='')
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

class Bridge(models.Model):
    name = models.TextField(default='')
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)