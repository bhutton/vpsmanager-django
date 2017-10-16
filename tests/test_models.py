from django.test import TestCase

import collections

from vps.models import Instance

class InstanceInventoryTest(TestCase):

    def test_saving_and_retrieving_items(self):
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

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.name, 'Instance1')
        self.assertEqual(first_saved_item.description, 'my instance')
        self.assertEqual(first_saved_item.memory, 512)
        self.assertEqual(first_saved_item.disk, 20)
        self.assertEqual(first_saved_item.bridge, 1)
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
        self.assertEqual(second_saved_item.disk, 20)
        self.assertEqual(second_saved_item.bridge, 1)
        self.assertEqual(second_saved_item.console, 204)
        self.assertEqual(second_saved_item.image, 1)
        self.assertEqual(second_saved_item.path, 'mypath')
        self.assertEqual(second_saved_item.start_script, 'startscript.sh')
        self.assertEqual(second_saved_item.stop_script, 'stopscript.sh')
        self.assertEqual(second_saved_item.create_disk, True)
        self.assertEqual(second_saved_item.create_path, True)
        self.assertEqual(second_saved_item.ip, '1.2.3.4')


