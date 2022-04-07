from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import PermissionSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        permissions = []
        permissions_serializers = []
        for group in user.groups.all():
          permissions = [*permissions, *group.permissions.all()]
        for permission in permissions:
          permission_serializer = PermissionSerializer (permission)
          permissions_serializers.append (permission_serializer.data)
        return Response({
            'token': token.key,
            'permissions': permissions_serializers
        })