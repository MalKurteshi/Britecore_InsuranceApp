from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Backend.serializers import UserSerializer, GroupSerializer, RegUserSerializer, RegPoliciesSerializer
from Backend.models import RegUser, RegPolicies
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])

        serializer.save(password=password)

    def perform_update(self, serializer):
        password = make_password(self.request.data['password'])

        serializer.save(password=password)

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RegUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    def perform_create(self, serializer):
        RegUser_password = make_password(self.request.data['RegUser_password'])

        serializer.save(RegUser_password=RegUser_password)

    def perform_update(self, serializer):
        RegUser_password = make_password(self.request.data['RegUser_password'])

        serializer.save(RegUser_password=RegUser_password)

    queryset = RegUser.objects.all()
    serializer_class = RegUserSerializer


class RegPoliciesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    RegPolicies_username = User.username
    queryset = RegPolicies.objects.all()
    serializer_class = RegPoliciesSerializer
