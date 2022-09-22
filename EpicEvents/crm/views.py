from django.shortcuts import render
from crm.serializers import ClientsSerializer, ContractsSerializer, EventsSerializer, ClientsDetailSerializer, ContractsDetailSerializer, EventsDetailSerializer
from .models import Client, Contract, Event
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import Support, Seller
from django_filters.rest_framework import DjangoFilterBackend

class ClientAPIView(ModelViewSet):
    permission_classes = [IsAuthenticated, Support|Seller]

    serializer_class = ClientsSerializer
    detail_serializer_class = ClientsDetailSerializer
    queryset = Client.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company_name', 'email', 'sales_contact']

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client','sales_contact','status']

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client','event_date','support_contact','event_status']

    def get_serializer_class(self):
        if self.action != 'list':
            return self.detail_serializer_class
        return super().get_serializer_class()
