from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.utils.html import escape

from vps.views import home_page

class HomePageTest(TestCase):

    def test_home_page_renders_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

class CreateVPSTest(TestCase):

    def test_create_vps_renders_form(self):
        response = self.client.get('/createvps/')
        self.assertTemplateUsed(response, 'createvps.html')
        expected_html = render_to_string('createvps.html')
        self.assertEqual(response.content.decode(), expected_html)

class CreateUserTest(TestCase):

    def test_create_user_renders_form(self):
        response = self.client.get('/createuser/')
        self.assertTemplateUsed(response, 'createuser.html')
        expected_html = render_to_string('createuser.html')
        self.assertEqual(response.content.decode(), expected_html)
