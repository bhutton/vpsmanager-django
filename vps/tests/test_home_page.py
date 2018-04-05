from django.test import TestCase


from django.http import HttpRequest
from django.template.loader import render_to_string

from vps.views import home_page


class HomePageTest(TestCase):

    def test_home_page_renders_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        self.assertIn('Home', response.content.decode())
        self.assertIn('User Management', response.content.decode())
        self.assertIn('/', response.content.decode())
        self.assertIn('/user', response.content.decode())

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