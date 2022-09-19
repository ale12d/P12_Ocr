from rest_framework.serializers import ModelSerializer
from auth_epic_events.models import User

class UsersSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','role']

        extra_kwargs = {
            'role': {'required': True}
        }