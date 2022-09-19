from django.shortcuts import render
from auth_epic_events.serializers import UsersSerializer
from auth_epic_events.models import User
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class SignUpAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            obj = UsersSerializer(data=request.data)
            if obj.is_valid():
                User.objects.create_user(username = obj['username'].value,
                                         password = obj['password'].value,role =obj['role'].value)
                return Response({'Message': 'valid sign up'}, status=status.HTTP_200_OK)
            return Response(obj.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message': 'Something Failed due to {}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)