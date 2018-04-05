from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from django.db import models

from vps.views import home_page
from vps.models import Instance, Disk, Network





class CreateUserTest(TestCase):

    def test_create_user_renders_form(self):
        response = self.client.get('/user/create/')
        self.assertTemplateUsed(response, 'createuser.html')
        expected_html = render_to_string('createuser.html')
        self.assertIn('Enter User Name', response.content.decode())



# class HomePageTest(TestCase):
#
#     def test_home
