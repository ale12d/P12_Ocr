from rest_framework.serializers import ModelSerializer
from crm.models import Client, Contract, Event


class ClientsSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email',
                  'company_name', 'sales_contact']


class ClientsDetailSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone',
                  'mobile', 'company_name', 'sales_contact']


class ContractsSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'status']


class ContractsDetailSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'sales_contact', 'client', 'status',
                  'amount', 'payement_due']


class EventsSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'client', 'event_date', 'support_contact',
                  'event_status']


class EventsDetailSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'client', 'event_date', 'support_contact',
                  'event_status', 'attendees', 'notes']
