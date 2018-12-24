
from Backend.models import RegUser, RegPolicies
from django.contrib.auth.models import User, Group
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }   


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class RegUserSerializer(serializers.HyperlinkedModelSerializer):

    RegUser_id = serializers.PrimaryKeyRelatedField( read_only=True)
    RegUser_name = serializers.CharField(max_length = 50)
    RegUser_surname = serializers.CharField(max_length = 50)
    RegUser_email = serializers.CharField(max_length= 20)
    RegUser_username = serializers.CharField(max_length = 15)
    RegUser_birthday = serializers.DateField()
    RegUser_photo = serializers.URLField()
    RegUser_streetaddress = serializers.CharField(max_length=50)
    RegUser_city = serializers.CharField(max_length=50)
    RegUser_contry = serializers.CharField(max_length=50)
    RegUser_zipcode = serializers.IntegerField()
    RegUser_password = serializers.CharField(max_length = 15)


    class Meta:
        model = RegUser
        fields = '__all__'
        extra_kwargs = {
            'RegUser_password': {
                'write_only': True,
            },
        }   


class RegPoliciesSerializer(serializers.HyperlinkedModelSerializer):

    RegPolicies_username = serializers.PrimaryKeyRelatedField(read_only=True)
    RegPolicies_type = serializers.CharField(max_length=50)
    RegPolicies_startdate = serializers.DateField()
    RegPolicies_enddate = serializers.DateField()
    RegPolicies_previouslyInsured = serializers.CharField(max_length=50)
    RegPolicies_previouslyDamaged = serializers.CharField(max_length=50)
    RegPolicies_Bday_YearOfProduction = serializers.DateField()
    RegPolicies_costOfProduct = serializers.DecimalField(max_digits=19, decimal_places=2)
    RegPolicies_description = serializers.CharField(max_length=50)

    RegPolicies_username = User.username
    class Meta:
        model = RegPolicies
        fields = '__all__'
