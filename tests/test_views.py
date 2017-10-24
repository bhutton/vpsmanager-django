from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from django.db import models

from vps.views import home_page
from vps.models import Instance

class HomePageTest(TestCase):

    def test_home_page_renders_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_contains_list_table(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('VPS Manager', response.content.decode())

    def test_home_page_contains_list_items(self):
        response = self.client.get('/vps/create/')
        self.assertTemplateUsed(response, 'createvps.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertIn('Enter Instance Name', response.content.decode())

class CreateVPSTest(TestCase):

    def test_create_vps_renders_form(self):
        response = self.client.get('/vps/create/')
        self.assertTemplateUsed(response, 'createvps.html')
        self.assertIn('Enter Instance Name', response.content.decode())

    def test_vps_user_can_save_a_POST_request(self):
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
        self.assertEqual(new_item.name, 'A new list item')
        self.assertEqual(new_item.description, 'My description')
        self.assertEqual(new_item.image, 1)
        self.assertEqual(new_item.memory, 512)
        self.assertEqual(new_item.disk, 20)
        self.assertEqual(new_item.bridge, 1)
        self.assertEqual(new_item.create_disk, True)
        self.assertEqual(new_item.create_path, True)


        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')



class CreateUserTest(TestCase):

    def test_create_user_renders_form(self):
        response = self.client.get('/user/create/')
        self.assertTemplateUsed(response, 'createuser.html')
        expected_html = render_to_string('createuser.html')
        self.assertEqual(response.content.decode(), expected_html)



# class HomePageTest(TestCase):
#
#     def test_home
