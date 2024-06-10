from django.test import TestCase, Client
from django.urls import reverse
from CRUD.models import Usuarios
from django.contrib.auth.models import User

# Create your tests here.

class TestViews(TestCase):

    
    def setUp(self):
        self.client = Client()
        self.create_url = reverse('create_url')
        self.list_url = reverse('lista_url')
        self.logout_url = reverse('exit')
        self.user_test = User.objects.create_user(username='testuser', password='testpassword')
        self.user_created = Usuarios.objects.create(
                                                        cedula = '1234',
                                                        nombre = 'Gerson',
                                                        apellido = 'Moreno',
                                                        correo = 'uetyu@yahoo.es'
                                                    )

    def test_login(self):

        auth = self.client.login(username = 'testuser', password = 'testpassword')

        self.assertTrue(auth)


    def test_create_user(self):
        
        self.client.login(username = 'testuser', password = 'testpassword')


        response = self.client.post(self.create_url,{
            'cedula': '1236',
            'nombre': 'Alirio',
            'apellido': 'Rodríguez',
            'correo': 'jajah@hotmail.com'
        },
        follow=True)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'CRUD/lista.html')
        self.assertTrue(Usuarios.objects.filter(cedula='1236').exists())

    def test_update_user(self):
        
        self.client.login(username = 'testuser', password = 'testpassword')

        url = reverse('update_url', args = [self.user_created.cedula])

        response = self.client.post(url,                     
                                    {
                                        'cedula': '9876',
                                        'nombre': 'José',
                                        'apellido': 'Morales',
                                        'correo': 'mose17@hotmail.com'
                                    },
                                    follow=True)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'CRUD/lista.html')
        self.assertFalse(Usuarios.objects.filter(cedula=self.user_created.cedula).exists())
        self.assertTrue(Usuarios.objects.filter(cedula='9876').exists())
        self.assertEqual(Usuarios.objects.get(cedula='9876').nombre,'José')

    def test_delete_user(self):

        self.client.login(username = 'testuser', password = 'testpassword')

        url = reverse('delete_url', args=[self.user_created.cedula])
        
        response = self.client.post(url, follow=True)

        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'CRUD/lista.html')
        self.assertFalse(Usuarios.objects.filter(cedula=self.user_created.cedula).exists())


    def test_view_list_no_login(self):

        response = self.client.get(self.list_url, follow=True)

        self.assertTemplateNotUsed(response,'CRUD/lista.html')
        self.assertTemplateUsed(response,'registration/login.html')

    def test_view_create_no_login(self):

        response = self.client.get(self.create_url, follow=True)

        self.assertTemplateNotUsed(response,'CRUD/create.html')
        self.assertTemplateUsed(response,'registration/login.html')

    def test_view_update_no_login(self):
        
        url = reverse('update_url', args=[self.user_created.cedula])

        response = self.client.get(url, follow=True)

        self.assertTemplateNotUsed(response,'CRUD/create.html')
        self.assertTemplateUsed(response,'registration/login.html')

    def test_view_delete_no_login(self):

        url = reverse('delete_url', args=[self.user_created.cedula])

        response = self.client.get(url, follow=True)

        self.assertTemplateNotUsed(response,'CRUD/confirmation.html')
        self.assertTemplateUsed(response,'registration/login.html')

    def test_logout(self):

        self.client.login(username = 'testuser', password = 'testpassword')

        response = self.client.get(self.logout_url,follow=True)

        user_authenticated = '_auth_user_id' in self.client.session

        self.assertRedirects(response, reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertFalse(user_authenticated)
        self.assertTemplateUsed(response, 'CRUD/home.html')