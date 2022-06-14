from rest_framework.serializers import ModelSerializer
from todolist.models import ToDo

class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['user', 'todo']

