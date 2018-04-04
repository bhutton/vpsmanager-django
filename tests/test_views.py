from django.template.loader import render_to_string
from django.test import TestCase
from mock import mock

from vps.models import Instance, Disk, Network, InstanceControl


class HomePageTest(TestCase):

    def test_home_page_renders_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertIn('VPS Manager', response.content.decode())
        self.assertIn('Home', response.content.decode())
        self.assertIn('Users', response.content.decode())


class CreateVPSTest(TestCase):

    def populate_instances(self):
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

    def test_create_vps_renders_form(self):
        response = self.client.get('/vps/create/')
        self.assertTemplateUsed(response, 'createvps.html')
        self.assertIn('Enter Instance Name', response.content.decode())

    def test_vps_user_can_create_an_instance(self):
        response = self.client.post('/vps/create/',
                                    data={'item_name': 'A new list item',
                                          'item_description': 'My description',
                                          'item_image': 1,
                                          'item_memory': 512,
                                          'item_disk': 20,
                                          'item_bridge': 1,
                                          'item_create_disk': 'on',
                                          'item_create_path': 'on'}
                                    )

        self.assertEqual(Instance.objects.count(), 1)
        new_item = Instance.objects.first()
        new_network = Network.objects.all().filter(instance_id=new_item)
        self.assertEqual(new_item.name, 'A new list item')
        self.assertEqual(new_item.description, 'My description')
        self.assertEqual(new_item.image, 1)
        self.assertEqual(new_item.memory, 512)
        # self.assertEqual(new_item.disk, 20)
        # self.assertEqual(new_network.bridge, 1)
        self.assertEqual(new_item.create_disk, True)
        self.assertEqual(new_item.create_path, True)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_vps_user_can_update_instance(self):
        self.populate_instances()
        response = self.client.post('/vps/modify/1',
                                    data={'item_id': 1,
                                          'item_name': 'A changed list item',
                                          'item_description': 'My description',
                                          'item_image': 2,
                                          'item_memory': 1024,
                                          'item_disk': 20,
                                          'item_bridge': 1,
                                          'item_create_disk': 'on',
                                          'item_create_path': 'on'}
                                    )

        self.assertEqual(Instance.objects.count(), 1)
        new_item = Instance.objects.first()
        self.assertEqual(new_item.name, 'A changed list item')
        self.assertEqual(new_item.description, 'My description')
        self.assertEqual(new_item.image, 2)
        self.assertEqual(new_item.memory, 1024)
        # self.assertEqual(new_item.disk, 20)
        # self.assertEqual(new_item.bridge, 1)
        self.assertEqual(new_item.create_disk, True)
        self.assertEqual(new_item.create_path, True)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

        response = self.client.post('/vps/modify/1',
                                    data={'item_id': 1,
                                          'item_name': 'A changed list item',
                                          'item_description': 'My description',
                                          'item_image': 2,
                                          'item_memory': 1024,
                                          'item_disk': 20,
                                          'item_bridge': 1,
                                          'item_create_disk': 'on',
                                          'item_create_path': 'on'}
                                    )

        self.assertEqual(Instance.objects.count(), 1)
        new_item = Instance.objects.first()
        self.assertEqual(new_item.name, 'A changed list item')
        self.assertEqual(new_item.description, 'My description')
        self.assertEqual(new_item.image, 2)
        self.assertEqual(new_item.memory, 1024)
        self.assertEqual(new_item.create_disk, True)
        self.assertEqual(new_item.create_path, True)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_vps_user_can_delete_instance(self):
        self.populate_instances()
        response = self.client.get('/vps/delete/1')
        self.assertEquals(response.status_code, 302)

        new_item = Instance.objects.first()
        self.assertEquals(new_item, None)

    def test_vps_view_instance(self):
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

        disk = Disk()
        disk.name = 'My old list item'
        disk.instance = first_item
        disk.save()

        network = Network()
        network.name = 'Another test'
        network.instance = first_item
        network.save()

        response = self.client.get('/vps/1/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed('viewvps.html')
        self.assertContains(response,'VPS Manager')

    @mock.patch('vps.models.InstanceControl.make_call_to_vpssvr')
    def test_stop_vps(self, fake_make_call_to_vpssvr):
        fake_make_call_to_vpssvr.return_value = True

        first_item = self.populate_instance()

        disk = Disk()
        disk.name = 'My old list item'
        disk.instance = first_item
        disk.save()

        network = Network()
        network.name = 'Another test'
        network.instance = first_item
        network.save()

        response = self.client.get('/vps/stop/608')
        self.assertEquals(response.status_code, 200)

        # status = Instance.objects.all().filter(pk=first_item.id)
        # self.assertEquals(status[0].status, 'Stopped')

    @mock.patch('vps.models.InstanceControl.make_call_to_vpssvr')
    def test_start_vps(self, fake_make_call_to_vpssvr):
        fake_make_call_to_vpssvr.return_value = True

        first_item = self.populate_instance()

        disk = Disk()
        disk.name = 'My old list item'
        disk.instance = first_item
        disk.save()

        network = Network()
        network.name = 'Another test'
        network.instance = first_item
        network.save()

        response = self.client.get('/vps/stop/608/')
        self.assertEquals(response.status_code, 200)

    def test_snapshot(self):
        first_item = self.populate_instance()
        response = self.client.get('/vps/snapshot/608/')
        self.assertEquals(response.status_code, 200)

    @staticmethod
    def populate_instance():
        first_item = Instance()
        first_item.id = 608
        first_item.name = 'My old list item'
        first_item.description = 'My description'
        first_item.image = 1
        first_item.memory = 512
        first_item.disk = 30
        first_item.bridge = 2
        first_item.status = 'Stopped'
        first_item.create_disk = False
        first_item.create_path = False
        first_item.save()
        return first_item


class UserTest(TestCase):

    def test_create_user_renders_form(self):
        response = self.client.get('/user/create/')
        self.assertTemplateUsed(response, 'createuser.html')
        expected_html = render_to_string('createuser.html')
        self.assertIn('User Name', response.content.decode())

    def test_modify_user_renders_form(self):
        response = self.client.get('/user/modify/')
        self.assertTemplateUsed(response, 'modifyuser.html')

