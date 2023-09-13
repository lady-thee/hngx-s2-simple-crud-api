from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from .models import Person
from .views import (createAPIView, readUserAPIViewModel,
                    updateUserAPIViewModel, deleteUserAPIViewModel)

class CreateViewAPITestCase(APITestCase):
    def setUp(self) -> None:
        pass
    
    def test_create_endpoint(self):
        url = reverse(createAPIView)
        data = {
            'name': 'Jane Doe',
            'username': 'janey',
            'email': 'janedoe@gmail.com'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'User successfully created')
        self.assertEqual(response.data['user']['name'], 'Jane Doe')

        created_user = Person.objects.get(name='Jane Doe')
        self.assertEqual(response.data['user']['id'], created_user.id)



class ReadEndpointViewTestCase(TestCase):
    def setUp(self) -> None:
        data = {
            'name': 'Jane Doe',
            'username': 'janey',
            'email': 'janedoe@gmail.com'
        }
        self.model_instance = Person.objects.create(**data)


    def test_read_endpoint(self):
        user = Person.objects.get(name='Jane Doe')
        pk = user.id
        url = reverse(readUserAPIViewModel, kwargs={'pk': pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['name'], user.name)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['email'], user.email)



class UpdateAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        data = {
            'name': 'Jane Doe',
            'username': 'janey',
            'email': 'janedoe@gmail.com'
        }
        self.model_instance = Person.objects.create(**data)

    def test_update_endpoint(self):
        data = {
            'name': 'Jane Doe',
            'username': 'jane',
            'email': 'janedoe@gmail.com'
        }
       
        user = Person.objects.get(name='Jane Doe')
        pk = user.id
        url = reverse(updateUserAPIViewModel, kwargs={'pk': pk})

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.data['message'], 'User details updated successfully!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        data = {
            'name': 'Jane Doe',
            'username': 'janey',
            'email': 'janedoe@gmail.com'
        }
        self.model_instance = Person.objects.create(**data)

    def test_update_endpoint(self):
       
        user = Person.objects.get(name='Jane Doe')
        pk = user.id
        url = reverse(deleteUserAPIViewModel, kwargs={'pk': pk})

        response = self.client.delete(url)

        self.assertEqual(response.data['message'], 'User successfully deleted!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
