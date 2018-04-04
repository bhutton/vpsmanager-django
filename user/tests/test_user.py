from django.test import TestCase


from django.template.loader import render_to_string

from user.models import User


class UserViewTest(TestCase):

    def test_create_user_renders_form(self):
        response = self.client.get('/user/create/')
        self.assertTemplateUsed(response, 'createuser.html')
        expected_html = render_to_string('createuser.html')
        self.assertIn('Enter User Name', response.content.decode())

    def test_modify_user_renders_form(self):
        response = self.client.get('/user/modify/')
        self.assertTemplateUsed(response, 'modifyuser.html')
        expected_html = render_to_string('modifyuser.html')
        self.assertIn('User Name', response.content.decode())

class UserModelTest(TestCase):
    def populate_users(self):
        first_item = User()

    # def test_create_user(self):
