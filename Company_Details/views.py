from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,viewsets, views,generics,status
from .models import *
from .Serializers import *
from rest_framework.permissions import IsAuthenticated
from django.db.models.functions import Concat
from django.db.models import CharField, Value as V
# Create your views here.

class CompanyViewset(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    http_method_names = ['get', 'post', 'put']
    serializer_class = CompanySerializer

class DepartmentViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get', 'post','put']
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(User.objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Department.objects.filter(companyid=company_id)
            serializer = DepartmentSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self,request):
        form_data = request.data
        user = request.user
        usersid = user.id
        company = list(User.objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']

        new_data = Department.objects.create(companyid=company_id,department=form_data["department"],locations_names=form_data["locations_names"],hod_name=form_data["hod_name"])
        serializer =DepartmentSerializer(new_data)
        return Response(serializer.data)


class UserViewset(viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get','post', 'put','delete']
    def list(self,request):
        user = request.user
        usersid = user.id
        company = list(User.objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
                company_id = c['company_id_id']
        queryset = User.objects.all().filter(company_id=company_id)
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)

class User_infoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = Get_User_infoSerializer
    http_method_names = ['get']
    def list(self, request):
        users = request.user
        usersid = users.id
        User_info=User.objects.filter(id=usersid).values()
        serializer = Get_User_infoSerializer(User_info,many=True)
        return Response(serializer.data)


class Hod_namesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = Hod_names_Serializer
    http_method_names = ['get']
    def list(self, request):
        users = request.user
        usersid = users.id
        company = list(User.objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']


        #Hod_names = list(Department.objects.values_list('hod_name').filter(companyid=company_id))
        Hod_names = Department.objects.annotate(Hod=Concat('hod_name', V(' ('), 'department', V(','),'locations_names',V(')'))).filter(companyid=company_id).values_list('Hod')
        return Response(Hod_names)

class LocationsViewsets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = Location_names_Serializer
    http_method_names = ['get']

    def list(self, request):
            users = request.user
            usersid = users.id
            company = list(User.objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Location_names = Department.objects.annotate(Hod=Concat('department', V(' ('), 'locations_names', V(')'))).filter(companyid=company_id).values_list('Hod')
            #serializer = Location_names_Serializer(Location_names, many=True)
            context = {'locations':Location_names}
            return Response(Location_names)
            # return Response(Hod_names)