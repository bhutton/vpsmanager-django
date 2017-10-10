from django.test import TestCase

import collections

from vps.models import Instance

class InstanceInventoryTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Instance()
        first_item.name = 'Instance1'
        first_item.description = 'my instance'
        first_item.ram = 512
        first_item.console = 204
        first_item.image = 1
        first_item.path = 'mypath'
        first_item.startscript = 'startscript.sh'
        first_item.stopscript = 'stopscript.sh'
        first_item.ip = '1.2.3.4'
        first_item.save()

        second_item = Instance()
        second_item.name = 'Instance2'
        second_item.description = 'my instance'
        second_item.ram = 512
        second_item.console = 204
        second_item.image = 1
        second_item.path = 'mypath'
        second_item.startscript = 'startscript.sh'
        second_item.stopscript = 'stopscript.sh'
        second_item.ip = '1.2.3.4'

        second_item.save()

        saved_items = Instance.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.name, 'Instance1')
        self.assertEqual(first_saved_item.description, 'my instance')
        self.assertEqual(first_saved_item.ram, 512)
        self.assertEqual(first_saved_item.console, 204)
        self.assertEqual(first_saved_item.image, 1)
        self.assertEqual(first_saved_item.path, 'mypath')
        self.assertEqual(first_saved_item.startscript, 'startscript.sh')
        self.assertEqual(first_saved_item.stopscript, 'stopscript.sh')
        self.assertEqual(first_saved_item.ip, '1.2.3.4')
        self.assertEqual(second_saved_item.name, 'Instance2')
        self.assertEqual(second_saved_item.ram, 512)
        self.assertEqual(second_saved_item.description, 'my instance')
        self.assertEqual(second_saved_item.console, 204)
        self.assertEqual(second_saved_item.image, 1)
        self.assertEqual(second_saved_item.path, 'mypath')
        self.assertEqual(second_saved_item.startscript, 'startscript.sh')
        self.assertEqual(second_saved_item.stopscript, 'stopscript.sh')
        self.assertEqual(second_saved_item.ip, '1.2.3.4')


