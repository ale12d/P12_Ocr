from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from crm.models import Client, Contract, Event
from django.test import Client as ClientTest
from auth_epic_events.models import User
from rest_framework.test import force_authenticate


class ReadTestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username='test', role=1, is_superuser=True)
        user.set_password("1234")
        user.save()
        client = Client(id=1, first_name="test", last_name="test", email="test@test.test", company_name="test")
        client.save()
        Contract.objects.create(id=1, client=client, amount="1")
        Event.objects.create(id=1, client=client, attendees="1", event_date="2022-10-12")
        response = self.client.post('/login/', data={'username':'test', 'password':'1234'})
        self.access_token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_client(self):
        response = self.client.get("/api/clients/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_detail(self):
        response = self.client.get("/api/clients/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_contract(self):
        response = self.client.get("/api/contracts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contract_detail(self):
        response = self.client.get("/api/contracts/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_event(self):
        response = self.client.get("/api/events/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_detail(self):
        response = self.client.get("/api/events/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='test', role=1, is_superuser=True)
        user.set_password("1234")
        user.save()
        client = Client(id=2, first_name="test", last_name="test", email="test@test.test", company_name="test")
        client.save()
        response = self.client.post('/login/', data={'username':'test', 'password':'1234'})
        self.access_token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_client(self):
        data = {"first_name":"test_create","last_name":"test","email":"test_create@test.test","company_name":"test"}
        response = self.client.post("/api/clients/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_contract(self):
        data = {"client":"2", "amount":"2"}
        response = self.client.post("/api/contracts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_event(self):
        data = {"client":"2", "event_date":"2022-09-12", "attendees":"2"}
        response = self.client.post("/api/events/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class DeleteTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create(username='test', role=1, is_superuser=True)
        user.set_password("1234")
        user.save()
        client = Client(id=1, first_name="test", last_name="test", email="test@test.test", company_name="test")
        client.save()
        Contract.objects.create(id=1, client=client, amount="1")
        Event.objects.create(id=1, client=client, attendees="1", event_date="2022-10-12")
        response = self.client.post('/login/', data={'username':'test', 'password':'1234'})
        self.access_token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_client(self):
        response = self.client.delete("/api/clients/1/")
        self.assertEqual(response.status_code,  status.HTTP_204_NO_CONTENT)

    def test_contract(self):
        response = self.client.delete("/api/contracts/1/")
        self.assertEqual(response.status_code,  status.HTTP_204_NO_CONTENT)

    def test_event(self):
        response = self.client.delete("/api/events/1/")
        self.assertEqual(response.status_code,  status.HTTP_204_NO_CONTENT)


class UpdateTestCase(APITestCase):

    def setUp(self):
        user = User.objects.create(username='test', role=1, is_superuser=True)
        user.set_password("1234")
        user.save()
        client = Client(id=1, first_name="test", last_name="test", email="test@test.test", company_name="test")
        client.save()
        Contract.objects.create(id=1, client=client, amount="1")
        Event.objects.create(id=1, client=client, attendees="1", event_date="2022-10-12")
        response = self.client.post('/login/', data={'username':'test', 'password':'1234'})
        self.access_token = response.json()['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_client(self):
        data = {"first_name":"test_update","last_name":"test","email":"test@test.test","company_name":"test"}
        response = self.client.patch("/api/clients/1/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contract(self):
        data = {"amount":"2"}
        response = self.client.patch("/api/contracts/1/", data)
        self.assertEqual(response.status_code,  status.HTTP_200_OK)

    def test_event(self):
        data = {"attendees":"2"}
        response = self.client.patch("/api/events/1/", data)
        self.assertEqual(response.status_code,  status.HTTP_200_OK)
