from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TaskAPITestCase(APITestCase):

    def setUp(self):
        # Crear un usuario para las pruebas
        self.user = User.objects.create_user(username='daniel', password='admin123')

        # Crear un JWT para autenticación
        self.refresh = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh.access_token)

        # Crear la URL base para tareas
        self.url = reverse('task-list')  # Asegúrate de que la URL sea correcta

    def test_create_task(self):
        """Prueba la creación de una nueva tarea"""
        data = {
            'title': 'Tarea de prueba',
            'completed': False,
        }
        response = self.client.post(self.url, data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task(self):
        """Prueba la obtención de las tareas"""
        # Crear una tarea antes de la solicitud
        task_data = {
            'title': 'Tarea de prueba',
            'completed': False,
        }
        self.client.post(self.url, task_data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Debería haber una tarea

    def test_update_task(self):
        """Prueba la actualización de una tarea"""
        task_data = {
            'title': 'Tarea de prueba',
            'completed': False,
        }
        # Crear una tarea
        response = self.client.post(self.url, task_data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        task_id = response.data['id']
        
        # Actualizar la tarea
        updated_data = {
            'title': 'Tarea actualizada',
            'completed': True,
        }
        response = self.client.put(reverse('task-detail', args=[task_id]), updated_data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Tarea actualizada')

    def test_delete_task(self):
        """Prueba la eliminación de una tarea"""
        task_data = {
            'title': 'Tarea de prueba',
            'completed': False,
        }
        # Crear una tarea
        response = self.client.post(self.url, task_data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        task_id = response.data['id']
        
        # Eliminar la tarea
        response = self.client.delete(reverse('task-detail', args=[task_id]), HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verificar que la tarea ha sido eliminada
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        self.assertEqual(len(response.data), 0)

    def test_unauthorized_access(self):
        """Prueba el acceso no autorizado"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
