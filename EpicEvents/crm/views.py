from django.shortcuts import render
from crm.serializers import ClientsSerializer, ContractsSerializer, EventsSerializer, ClientsDetailSerializer, ContractsDetailSerializer, EventsDetailSerializer
from .models import Client, Contract, Event
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import Support, Seller

class ClientAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated, Support|Seller]

    serializer_class = ClientsSerializer
    detail_serializer_class = ClientsDetailSerializer
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

class ContractAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated, Support|Seller]

    serializer_class = ContractsSerializer
    detail_serializer_class = ContractsDetailSerializer
    queryset = Contract.objects.all()

    def get_serializer_class(self):
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

class EventAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated, Support|Seller]

    serializer_class = EventsSerializer
    detail_serializer_class = EventsDetailSerializer
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()
