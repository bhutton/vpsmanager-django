from django.test import TestCase

from vps.models import Instance, Disk


class TestStatusVPS(TestCase):

    @staticmethod
    def populate_instances():
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

        second_item = Disk()
        second_item.instance = first_item
        second_item.name = 'test'
        second_item.size = int(30)
        second_item.save()

    def test_status_all_vps(self):
        self.populate_instances()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('My old list item', response.content.decode())
        self.assertIn('My description', response.content.decode())
        self.assertIn('1', response.content.decode())

    def test_status_specific_vps(self):
        self.populate_instances()
        response = self.client.get('/vps/1/')
        self.assertEquals(response.status_code, 200)
        self.assertIn('My old list item', response.content.decode())
        self.assertIn('My description', response.content.decode())
        self.assertIn('1', response.content.decode())
        self.assertIn('512', response.content.decode())
        self.assertIn('30', response.content.decode())
        self.assertIn('2', response.content.decode())