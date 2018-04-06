from django.test import TestCase


from django.template.loader import render_to_string

from user.models import User


class UserViewTest(TestCase):

    def test_list_users(self):
        response = self.client.get('/user/')
        self.assertTemplateUsed(response, 'listuser.html')


class UserCreateTest(TestCase):

    def test_create_user_renders_form(self):
        response = self.client.get('/user/create/')
        self.assertTemplateUsed(response, 'createuser.html')
        expected_html = render_to_string('createuser.html')
        self.assertTemplateUsed(response, 'createuser.html')
        self.assertIn('Enter User Name', response.content.decode())
        self.assertIn('Enter Password', response.content.decode())
        self.assertIn('Enter Password Again', response.content.decode())


    def test_modify_user_renders_form(self):
        response = self.client.post('/user/create/',
                                    data={'name': 'fredbloggs', 'email': 'fred@bloggs.com', 'password': 'abc123'}, follow=True)

        self.assertIn('fredbloggs', response.content.decode())
        self.assertTemplateUsed(response, 'listuser.html')
        response = self.client.get('/user/modify/1/')
        self.assertTemplateUsed(response, 'modifyuser.html')
        expected_html = render_to_string('modifyuser.html')
        self.assertIn('User Name', response.content.decode())
        self.assertIn('fredbloggs', response.content.decode())
        self.assertIn('fred@bloggs.com', response.content.decode())
        self.assertIn('Username', response.content.decode())
        self.assertIn('Password', response.content.decode())

        response = self.client.post('/user/modify/1',
                                    data={'name': 'fredbloggs2', 'email':'fred2@bloggs.com','password': 'abc123'})
        response = self.client.get('/user/modify/1/')
        self.assertIn('fredbloggs2', response.content.decode())
        self.assertIn('fred2@bloggs.com', response.content.decode())

    def test_create_and_delete_user(self):
        self.client.post('/user/create/',
                                    data={'name': 'fredbloggs', 'email': 'fred@bloggs.com','password': 'abc123'})
        response = self.client.get('/user/')
        self.assertIn('fredbloggs', response.content.decode())
        response = self.client.post('/user/delete/1')
        self.assertIn('Deleted', response.content.decode())
        self.assertNotIn('fredbloggs', response.content.decode())




class UserModelTest(TestCase):
    def populate_users(self):
        first_item = User()

    def test_create_user(self):
        response = self.client.post('/user/create/',
                                    data={'name': 'fredbloggs',
                                          'email': 'fred@bloggs.com',
                                          'password': 'abc123'})
        self.assertEqual(User.objects.count(), 1)
        new_item = User.objects.first()
        self.assertEqual(new_item.name,'fredbloggs')
        self.assertEqual(new_item.password, 'abc123')

class UserTest(TestCase):

    @staticmethod
    def populate_instance():
        first_item = User()
        first_item.id = 1
        first_item.name = 'Fred Bloggs'
        first_item.email = 'fred@bloggs.com'
        first_item.password = 'abc123'
        first_item.save()
        return first_item

    def test_create_user_renders_form(self):
        response = self.client.get('/user/create/')
        self.assertTemplateUsed(response, 'createuser.html')
        expected_html = render_to_string('createuser.html')
        self.assertIn('User Name', response.content.decode())

    def test_modify_user_renders_form(self):
        self.populate_instance()
        response = self.client.get('/user/modify/1')
        self.assertTemplateUsed(response, 'modifyuser.html')

    def test_user_view(self):
        first_item = User()
        first_item.name = 'fredbloggs'
        first_item.description = 'abc123'
        first_item.save()

        response = self.client.get('/user/1/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewuser.html')
        # self.assertIn('fredbloggs', response.content.decode())

    def test_user_list(self):
        response = self.client.get('/user/')
        self.assertIn('No users have been created', response.content.decode())
        self.assertIn('Create', response.content.decode())

        # first_item = User()
        # first_item.username = 'fredbloggs'
        # first_item.description = 'abc123'
        # first_item.save()
        self.populate_instance()

        response = self.client.get('/user/')
        self.assertTemplateUsed(response, 'listuser.html')
        self.assertIn('Fred Bloggs', response.content.decode())
        self.assertIn('fred@bloggs.com', response.content.decode())
        self.assertIn('edit', response.content.decode())
        self.assertIn('delete', response.content.decode())
        self.assertIn('/user/modify/1', response.content.decode())
