import base64

import requests
from django.db import models
# from django.urls import reverse


class Instance(models.Model):
    name = models.TextField(default='')
    description = models.TextField(default='')
    memory = models.IntegerField(default=0)
    # bridge = models.IntegerField(default=0)
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


class Bridge(models.Model):
    name = models.TextField(default='')

    class Meta:
        ordering = ('id',)


class Network(models.Model):
    name = models.TextField(default='')
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE)
    bridge = models.IntegerField(default=1)

    class Meta:
        ordering = ('id',)


class InstanceControl:

    def start(self, instance_id):
        return self.make_call_to_vpssvr('/vpssvr/api/v1.0/tasks/start/' + instance_id)

    def stop(self, instance_id):
        return self.make_call_to_vpssvr('/vpssvr/api/v1.0/tasks/stop/' + instance_id)

    def status(self, instance_id):
        return self.make_call_to_vpssvr('/vpssvr/api/v1.0/tasks/status/' + instance_id)

    def make_call_to_vpssvr(self, path):
        vps_server = 'http://10.128.2.1:9999'
        vps_username = 'miguel'
        vps_password = 'python'
        connection_string = vps_server + path
        try:
            return self.open_with_auth(connection_string,
                                       'GET', vps_username, vps_password)
        except:
            return "Error: was not able to connect"

    def open_with_auth(self, url, method, username, password):
        headers = {
            'Authorization': 'Basic %s' % base64.b64encode(b"miguel:python").decode("ascii")
        }
        return requests.get(url, headers=headers)


