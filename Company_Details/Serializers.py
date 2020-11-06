from rest_framework import serializers
from .models import *
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
# from .Scheduler import Schedules_operation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response


class CompanySerializer(serializers.ModelSerializer):
    class Meta():
        model = Company
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Department
        exclude = ('companyid',)

class UserSerializer(serializers.ModelSerializer):
    class Meta():

        model = User
        fields = ('id','username','email','password','full_name','department','employee_id','mobile_number','date_of_birth','company_id','role','is_staff','is_superuser')
        extra_kwargs = {'password':{"write_only":True,'required':True}}

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()

        return user

class Get_User_infoSerializer(serializers.ModelSerializer):
    class Meta():

        model = User
        exclude = ('password','groups','user_permissions',)

class Hod_names_Serializer(serializers.ModelSerializer):

    class Meta():
        model = Department
        fields = ('hod_name',)

class Location_names_Serializer(serializers.ModelSerializer):

    class Meta():
        model = Department
        fields = ('locations_names',)