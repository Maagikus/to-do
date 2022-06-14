from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserInfoSerializer
from todolist.models import ToDo

# Create your views here.
class UserInfoViewSet(ModelViewSet):
    http_metod_names = ['get', 'post']
    queryset = ToDo.objects.all()
    serializer_class = UserInfoSerializer


    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            for item in request.data:
                if item['user'] is None:
                    item['user'] = request.user.id
        else:
            if request.data['user'] is None:
                request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def list(self, request, *args, **kwargs):
        infos = ToDo.objects.all()
        context = {'request':request}
        serializer = UserInfoSerializer(infos, many=True, context=context)
        return Response(serializer.data)