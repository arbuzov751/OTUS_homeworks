from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class MenuTest(TestCase):
    def setUp(self):
        # self.super_user_data = {
        #     'username': 'myname',
        #     'email': 'someemail@otus.local',
        #     'password': 'MyPassword',
        # }
        # self.user = get_user_model().objects.create_superuser(
        #     **self.super_user_data
        # )
        response = self.client.post('/menu/create/', data={
            'product_name': 'cappuccino',
            'type': 'coffee',
            'price': 200,
        })
        self.assertEqual(302, response.status_code)

    def test_menu(self):
        response = self.client.get('/menu/')
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.context['user'].is_anonymous)

    def test_deteil_menu_item(self):
        response = self.client.get('/menu/detail/1/')
        self.assertEqual(200, response.status_code)
        # print(response.context['menu'])
        self.assertContains(response, "cappuccino")
        self.assertEqual(str(response.context['menu']), 'coffee: cappuccino = 200р')

    def tearDown(self):
        response = self.client.post('/menu/delete/1/', follow=True)
        self.assertEqual(200, response.status_code)


