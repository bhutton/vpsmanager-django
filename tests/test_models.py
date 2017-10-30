from django.test import TestCase

# import collections

from vps.models import Instance, Disk, Network, Bridge


class InstanceInventoryTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Instance()
        first_item.name = 'Instance1'
        first_item.description = 'my instance'
        first_item.memory = 512
        first_item.disk = 20
        first_item.console = 204
        first_item.image = 1
        first_item.path = 'mypath'
        first_item.start_script = 'startscript.sh'
        first_item.stop_script = 'stopscript.sh'
        first_item.create_disk = True
        first_item.create_path = True
        first_item.ip = '1.2.3.4'
        first_item.save()

        second_item = Instance()
        second_item.name = 'Instance2'
        second_item.description = 'my instance'
        second_item.memory = 512
        second_item.disk = 20
        second_item.console = 204
        second_item.image = 1
        second_item.path = 'mypath'
        second_item.start_script = 'startscript.sh'
        second_item.stop_script = 'stopscript.sh'
        second_item.create_disk = True
        second_item.create_path = True
        second_item.ip = '1.2.3.4'

        second_item.save()

        saved_items = Instance.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.name, 'Instance1')
        self.assertEqual(first_saved_item.description, 'my instance')
        self.assertEqual(first_saved_item.memory, 512)
        self.assertEqual(first_saved_item.console, 204)
        self.assertEqual(first_saved_item.image, 1)
        self.assertEqual(first_saved_item.path, 'mypath')
        self.assertEqual(first_saved_item.start_script, 'startscript.sh')
        self.assertEqual(first_saved_item.stop_script, 'stopscript.sh')
        self.assertEqual(first_saved_item.create_disk, True)
        self.assertEqual(first_saved_item.create_path, True)
        self.assertEqual(first_saved_item.ip, '1.2.3.4')
        self.assertEqual(second_saved_item.name, 'Instance2')
        self.assertEqual(second_saved_item.description, 'my instance')
        self.assertEqual(second_saved_item.memory, 512)
        self.assertEqual(second_saved_item.console, 204)
        self.assertEqual(second_saved_item.image, 1)
        self.assertEqual(second_saved_item.path, 'mypath')
        self.assertEqual(second_saved_item.start_script, 'startscript.sh')
        self.assertEqual(second_saved_item.stop_script, 'stopscript.sh')
        self.assertEqual(second_saved_item.create_disk, True)
        self.assertEqual(second_saved_item.create_path, True)
        self.assertEqual(second_saved_item.ip, '1.2.3.4')

    def test_deleting_items(self):
        first_item = Instance()
        first_item.name = 'Instance1'
        first_item.description = 'my instance'
        first_item.memory = 512
        first_item.disk = 20
        first_item.bridge = 1
        first_item.console = 204
        first_item.image = 1
        first_item.path = 'mypath'
        first_item.start_script = 'startscript.sh'
        first_item.stop_script = 'stopscript.sh'
        first_item.create_disk = True
        first_item.create_path = True
        first_item.ip = '1.2.3.4'
        first_item.save()

        second_item = Instance()
        second_item.name = 'Instance2'
        second_item.description = 'my instance'
        second_item.memory = 512
        second_item.disk = 20
        second_item.bridge = 1
        second_item.console = 204
        second_item.image = 1
        second_item.path = 'mypath'
        second_item.start_script = 'startscript.sh'
        second_item.stop_script = 'stopscript.sh'
        second_item.create_disk = True
        second_item.create_path = True
        second_item.ip = '1.2.3.4'

        second_item.save()
        saved_items = Instance.objects.all()
        self.assertEqual(saved_items.count(), 2)

        response = second_item.delete()
        saved_items = Instance.objects.all()
        self.assertEqual(saved_items.count(), 1)

    def test_create_instance_with_disk(self):
        first_item = Instance()
        first_item.name = 'Instance1'
        first_item.description = 'my instance'
        first_item.memory = 512
        first_item.disk = 20
        first_item.bridge = 1
        first_item.console = 204
        first_item.image = 1
        first_item.path = 'mypath'
        first_item.start_script = 'startscript.sh'
        first_item.stop_script = 'stopscript.sh'
        first_item.create_disk = True
        first_item.create_path = True
        first_item.ip = '1.2.3.4'
        first_item.save()

        first_disk = Disk(name='test', instance=first_item)
        first_disk.save()

    def test_create_and_retrieve_instance_with_disk(self):
        first_item = Instance()
        first_item.name = 'Instance1'
        first_item.description = 'my instance'
        first_item.memory = 512
        first_item.disk = 20
        first_item.bridge = 1
        first_item.console = 204
        first_item.image = 1
        first_item.path = 'mypath'
        first_item.start_script = 'startscript.sh'
        first_item.stop_script = 'stopscript.sh'
        first_item.create_disk = True
        first_item.create_path = True
        first_item.ip = '1.2.3.4'
        first_item.save()

        first_disk = Disk(name='test', instance=first_item)
        first_disk.save()

        instance = Instance.objects.all().filter(pk=first_item.id)
        disk = Disk.objects.all().filter(instance_id=first_item.id)
        item = instance[0]
        self.assertEqual(item.name, 'Instance1')
        self.assertEqual(disk.count(), 1)



    @staticmethod
    def test_create_instance_with_network():
        first_item = Instance()
        first_item.name = 'Instance1'
        first_item.description = 'my instance'
        first_item.memory = 512
        first_item.disk = 20
        first_item.console = 204
        first_item.image = 1
        first_item.path = 'mypath'
        first_item.start_script = 'startscript.sh'
        first_item.stop_script = 'stopscript.sh'
        first_item.create_disk = True
        first_item.create_path = True
        first_item.ip = '1.2.3.4'
        first_item.save()

        first_disk = Disk(name='test', size=20, instance=first_item)
        first_disk.save()
        first_nw = Network(name='test', bridge=1, instance=first_item)
        first_nw.save()

    def test_create_and_retrieve_instance_with_network(self):
        first_item = Instance()
        first_item.name = 'Instance1'
        first_item.description = 'my instance'
        first_item.memory = 512
        first_item.disk = 20
        first_item.bridge = 1
        first_item.console = 204
        first_item.image = 1
        first_item.path = 'mypath'
        first_item.start_script = 'startscript.sh'
        first_item.stop_script = 'stopscript.sh'
        first_item.create_disk = True
        first_item.create_path = True
        first_item.ip = '1.2.3.4'
        first_item.save()

        first_network = Network(name='test', bridge=1, instance=first_item)
        first_network.save()

        instance = Instance.objects.all().filter(pk=first_item.id)
        network = Network.objects.all().filter(instance_id=first_item.id)

        item = instance[0]
        self.assertEqual(item.name, 'Instance1')
        self.assertEqual(network.count(), 1)

    def test_vps_get_status(self):
        first_item = Instance()
        first_item.name = 'My old list item'
        first_item.description = 'My description'
        first_item.image = 1
        first_item.memory = 512
        first_item.disk = 30
        first_item.bridge = 2
        first_item.create_disk = False
        first_item.create_path = False
        first_item.save()

        instance = Instance.objects.all().filter(pk=first_item.id)
        item = instance[0]
        self.assertEqual(item.status, 'Stopped')

    def test_update_item(self):
        first_item = Instance()
        first_item.name = 'Instance1'
        first_item.description = 'my instance'
        first_item.memory = 512
        first_item.disk = 20
        first_item.bridge = 1
        first_item.console = 204
        first_item.image = 1
        first_item.path = 'mypath'
        first_item.start_script = 'startscript.sh'
        first_item.stop_script = 'stopscript.sh'
        first_item.create_disk = True
        first_item.create_path = True
        first_item.ip = '1.2.3.4'
        first_item.save()

        saved_items = Instance.objects.all()
        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.name, 'Instance1')

        first_item.name = 'Instance2'
        first_item.save()

        saved_items = Instance.objects.all().filter(name="Instance2")
        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.name, 'Instance2')
