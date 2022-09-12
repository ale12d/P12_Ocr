from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.

class ReadTestCase(APITestCase):

    def test_client(self):
        response = self.client.get("/api/clients/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_client_detail(self):
        response = self.client.get("/api/clients/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_contract(self):
        response = self.client.get("/api/contracts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contract_detail(self):
        response = self.client.get("/api/contracts/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_event(self):
        response = self.client.get("/api/events/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_detail(self):
        response = self.client.get("/api/events/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateTestCase(APITestCase):

    def test_client(self):
        data = {"first_name":"test","last_name":"test","email":"test@test.test","company_name":"test"}
        response = self.client.post("/api/clients/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class DeleteTestCase(APITestCase):

    def test_client(self):
        response = self.client.delete("/api/clients/1/")
        self.assertEqual(response.status_code,  status.HTTP_200_OK)

    def test_contract(self):
        response = self.client.delete("/api/contracts/1/")
        self.assertEqual(response.status_code,  status.HTTP_200_OK)

    def test_event(self):
        response = self.client.delete("/api/events/1/")
        self.assertEqual(response.status_code,  status.HTTP_200_OK)


class UpdateTestCase(APITestCase):

    def test_client(self):
        data = {"first_name":"test_update","last_name":"test","email":"test@test.test","company_name":"test"}
        response = self.client.patch("/api/clients/1/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
