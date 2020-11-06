from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .Serializer import *
from django.core import serializers
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from rest_framework import status,viewsets, views,generics,status
from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING, TYPE_ARRAY
from drf_yasg.utils import swagger_auto_schema
from datetime import date
from rest_framework.permissions import IsAuthenticated
from .Schedule import Shedules_operation
import requests
import time
import json
from .Rescheduler import rescheduler_operation
from django.http import JsonResponse
from Company_Details.models import Company
from django.contrib.auth import get_user_model
from .tests import *


User = get_user_model()
today = datetime.datetime.today().date()

class CustomTokenObtainPairView(TokenObtainPairView):

    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()

class Safety_FormsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = Safety_FormSerializer
    def list(self,request):
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            due_test = list(Safety_observation_Form.objects.values_list('due_date').filter(companyid=company_id))
            b = map(lambda x: x[0], due_test)
            b = list(b)
            res = []
            for val in b:
                if val != None:
                    res.append(val)
            Overdue_check(res,company_id)
            queryset = Safety_observation_Form.objects.filter(companyid=company_id)
            serializer = Safety_FormSerializer(queryset,many=True)
            return Response(serializer.data)

class Safety_Form_RPViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = Safety_observation_FormSerializer

    def create(self,request):
        form_data = request.data
        users = request.user
        usersid = user.id
        usersname = user.full_name
        company = list(get_user_model().objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']

        new_data  = Safety_observation_Form.objects.create(total_hours=form_data["total_hours"],department=form_data["department"],superviser_name=form_data["superviser_name"],location=form_data["location"],excution_department=form_data["excution_department"],issue="RP",descrption=form_data["descrption"],discussion_held=form_data["discussion_held"],agreement=form_data["agreement"],types=form_data["types"],injury_potential=form_data["injury_potential"],image=form_data["image"],observation_status=form_data["observation_status"],safe_situation=form_data["safe_situation"],persons_involved=form_data['persons_involved'],created_by=usersname,companyid=company_id)
        serializer = Safety_observation_FormSerializer(new_data)
        return Response(serializer.data)

class Safety_Form_PPViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = Safety_observation_FormSerializer

    def create(self,request):
        form_data = request.data
        user = request.user
        usersid = user.id
        usersname = user.full_name
        company = list(get_user_model().objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']
        new_data  = Safety_observation_Form.objects.create(total_hours=form_data["total_hours"],department=form_data["department"],superviser_name=form_data["superviser_name"],location=form_data["location"],excution_department=form_data["excution_department"],issue="PP",descrption=form_data["descrption"],discussion_held=form_data["discussion_held"],agreement=form_data["agreement"],types=form_data["types"],injury_potential=form_data["injury_potential"],image=form_data["image"],observation_status=form_data["observation_status"],safe_situation=form_data["safe_situation"],persons_involved=form_data['persons_involved'],created_by=usersname,companyid=company_id)
        serializer = Safety_observation_FormSerializer(new_data)
        return Response(serializer.data)

class Safety_Form_PPEViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = Safety_observation_FormSerializer

    def create(self,request):
        form_data = request.data
        user = request.user
        usersid = user.id
        usersname = user.full_name
        company = list(get_user_model().objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']
        new_data  = Safety_observation_Form.objects.create(total_hours=form_data["total_hours"],department=form_data["department"],superviser_name=form_data["superviser_name"],location=form_data["location"],excution_department=form_data["excution_department"],issue="PPE",descrption=form_data["descrption"],discussion_held=form_data["discussion_held"],agreement=form_data["agreement"],types=form_data["types"],injury_potential=form_data["injury_potential"],image=form_data["image"],observation_status=form_data["observation_status"],safe_situation=form_data["safe_situation"],persons_involved=form_data['persons_involved'],created_by=usersname,companyid=company_id)
        serializer = Safety_observation_FormSerializer(new_data)
        return Response(serializer.data)

class Safety_Form_TEViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = Safety_observation_FormSerializer

    def create(self,request):
        form_data = request.data
        user = request.user
        usersid = user.id
        usersname = user.full_name
        company = list(get_user_model().objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']
        new_data  = Safety_observation_Form.objects.create(total_hours=form_data["total_hours"],department=form_data["department"],superviser_name=form_data["superviser_name"],location=form_data["location"],excution_department=form_data["excution_department"],issue="TE",descrption=form_data["descrption"],discussion_held=form_data["discussion_held"],agreement=form_data["agreement"],types=form_data["types"],injury_potential=form_data["injury_potential"],image=form_data["image"],observation_status=form_data["observation_status"],safe_situation=form_data["safe_situation"],persons_involved=form_data['persons_involved'],created_by=usersname,companyid=company_id)
        serializer = Safety_observation_FormSerializer(new_data)
        return Response(serializer.data)

class Safety_Form_PROViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = Safety_observation_FormSerializer

    def create(self,request):
        form_data = request.data
        user = request.user
        usersid = user.id
        usersname = user.full_name
        company = list(get_user_model().objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']
        new_data  = Safety_observation_Form.objects.create(total_hours=form_data["total_hours"],department=form_data["department"],superviser_name=form_data["superviser_name"],location=form_data["location"],excution_department=form_data["excution_department"],issue="PRO",descrption=form_data["descrption"],discussion_held=form_data["discussion_held"],agreement=form_data["agreement"],types=form_data["types"],injury_potential=form_data["injury_potential"],image=form_data["image"],observation_status=form_data["observation_status"],safe_situation=form_data["safe_situation"],persons_involved=form_data['persons_involved'],created_by=usersname,companyid=company_id)
        serializer = Safety_observation_FormSerializer(new_data)
        return Response(serializer.data)

class Safety_Form_HKViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = Safety_observation_FormSerializer

    def create(self,request):
        form_data = request.data
        user = request.user
        usersid = user.id
        usersname = user.full_name
        company = list(get_user_model().objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']
        new_data  = Safety_observation_Form.objects.create(total_hours=form_data["total_hours"],department=form_data["department"],superviser_name=form_data["superviser_name"],location=form_data["location"],excution_department=form_data["excution_department"],issue="HK",descrption=form_data["descrption"],discussion_held=form_data["discussion_held"],agreement=form_data["agreement"],types=form_data["types"],injury_potential=form_data["injury_potential"],image=form_data["image"],observation_status=form_data["observation_status"],safe_situation=form_data["safe_situation"],persons_involved=form_data['persons_involved'],created_by=usersname,companyid=company_id)
        serializer = Safety_observation_FormSerializer(new_data)
        return Response(serializer.data)


class Safe_situationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = Safe_situationSerializer

    def create(self,request):
        form_data = request.data
        user = request.user
        usersid = user.id
        usersname = user.full_name
        company = list(get_user_model().objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']
        new_data=Safety_observation_Form.objects.create(total_hours=form_data["total_hours"],department=form_data["department"],superviser_name=form_data["superviser_name"],location=form_data["location"],excution_department=form_data["excution_department"],observation_status="Close",safe_situation=form_data["safe_situation"],closed_date=datetime.datetime.today().date(),created_by=usersname,companyid=company_id)
        serializer = Safe_situationSerializer(new_data)
        return Response(serializer.data)

class Others_FormsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = Others_FormsSerializer

    def create(self,request):
        form_data = request.data
        user = request.user
        usersid = user.id
        usersname = user.full_name
        company = list(get_user_model().objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']
        new_data  = Safety_observation_Form.objects.create(total_hours=form_data["total_hours"],department=form_data["department"],superviser_name=form_data["superviser_name"],location=form_data["location"],excution_department=form_data["excution_department"],issue="Others",descrption=form_data["descrption"],created_by=usersname,companyid=company_id)
        serializer = Safety_observation_FormSerializer(new_data)
        return Response(serializer.data)


class SchedulerViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get','post']
    queryset = Scheduler.objects.all()
    serializer_class = SchedulerSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Scheduler.objects.filter(companyid=company_id)
            serializer = SchedulerSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self,request):
        form_data = request.data
        user = request.user
        usersid = user.id
        company = list(get_user_model().objects.filter(id=usersid).values())
        company_id = ""
        for c in company:
            company_id = c['company_id_id']

        new_data = Scheduler.objects.create(companyid=company_id,holidays=form_data["holidays"],weekmask=form_data["weekmask"],holiday_types=form_data["holiday_types"],observations_required=form_data["observations_required"])
        serializer = SchedulerSerializer(new_data)
        return Response(serializer.data)

class Safe_SituationsCount(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = CountSerializer

    def list(self,request):
        if request.method=='GET':
            form_data = request.data
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id,safe_situation=True).count()
            context = {'count' : queryset}
            return Response(context)


class Safety_Forms_Agreed_Closes(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = CountSerializer

    def list(self,request):
        if request.method=='GET':
            form_data = request.data
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id,agreement="Agreed").count()
            context = {'count' : queryset}
            return Response(context)



class SchedulesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Schedules.objects.all()
    http_method_names = ['get']
    serializer_class = SchedulesSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            due_test = list(Schedules.objects.values_list('date').filter(companyid=company_id))
            b = map(lambda x: x[0], due_test) 
            b = list(b)
            Missed_Schedule(b,company_id)
            queryset = Schedules.objects.filter(companyid=company_id)
            serializer = SchedulesSerializer(queryset, many=True)
            return Response(serializer.data)

class Get_SchedulesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer
    http_method_names = ['get']
    def list(self,request):
        if request.method == 'GET':
            #Schedules.objects.all().delete()
            user = request.user
            usersid = user.id
            Shedules_operation(usersid)
            queryset = Schedules.objects.all()
            context = {'Done':'Schedules have been made'}
            return Response(context)

class OpenissuesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = OpenissuesSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id,observation_status='Open')
            serializer = Safety_FormSerializer(queryset, many=True)
            return Response(serializer.data)

class CloseissuesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = CloseissuesSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id,observation_status='Close')
            serializer = Safety_FormSerializer(queryset, many=True)
            return Response(serializer.data)


class OpenissuescountViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = CountSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id,observation_status='Open').count()
            context = {'count' : queryset}
            return Response(context)

class CloseissuescountViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = CountSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id,observation_status='Close').count()
            context = {'count':queryset}
            return Response(context)


class PendingissuesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = OpenissuesSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id,observation_status='Open')
            serializer = Safety_FormSerializer(queryset, many=True)
            return Response(serializer.data)



class PendingissuescountViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = CountSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id,observation_status='Open').count()
            context = {'count':queryset}
            return Response(context)

from django.db.models import Q

class OverdueissuesViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = OpenissuesSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id).filter(Q(due_date__gte=datetime.datetime.today().date()))
            serializer = Safety_FormSerializer(queryset, many=True)
            return Response(serializer.data)

class OverdueissuescountViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Safety_observation_Form.objects.all()
    serializer_class = CountSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            queryset = Safety_observation_Form.objects.filter(companyid=company_id).filter(Q(due_date__gte=datetime.datetime.today().date())).count()
            context = {'Count' : queryset}
            return Response(context)


class Schedules_userViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Schedules.objects.all()
    serializer_class = Schedules_userSerializer

    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            due_test = list(Schedules.objects.values_list('date').filter(companyid=company_id))
            b = map(lambda x: x[0], due_test)
            b = list(b)
            Missed_Schedule(b, company_id)
            queryset = Schedules.objects.filter(companyid=company_id,name=usersname)
            serializer = Schedules_userSerializer(queryset, many=True)
            return Response(serializer.data)

class RescheduleViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Schedules.objects.all()
    serializer_class = ReschedulerSerializer
    def create(self,request):
        if request.method == 'POST':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            reschedule_date = request.data.get('reschedule_date')
            date = request.data.get('date')
            reason_reschedule = request.data.get('reason_reschedule')
            scheduled = list(Schedules.objects.filter(name=usersname,date=date).values())
            schedule_id = ""
            for schedule in scheduled:
                schedule_id = schedule['id']

            queryset = Schedules.objects.filter(id=schedule_id).update(reschedule_date=reschedule_date,reason_reschedule=reason_reschedule)
            context = {'Date_of_Schedule':date,'Rescheduled_Date':reschedule_date,'reason_reschedule':reason_reschedule}
            return Response(context)

class Start_workViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']
    queryset = Schedules.objects.all()
    serializer_class = Start_workSerializer
    def create(self,request):
        if request.method == 'POST':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            date = request.data.get('date')
            scheduled = list(Schedules.objects.filter(name=usersname,date=date).values())
            schedule_id =""
            for schedule in scheduled:
                schedule_id = schedule['id']

            queryset = Schedules.objects.filter(id=schedule_id).update(status="Completed")
            context = {'Status':'Completed'}
            return Response(context)

class Total_observationsViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Schedules.objects.all()
    serializer_class = CountSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            queryset = Schedules.objects.filter(name=usersname).count()
            context = {'Count': queryset}
            return Response(context)

class Total_observations_completedViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Schedules.objects.all()
    serializer_class = CountSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            queryset = Schedules.objects.filter(name=usersname,status='Completed').count()
            context = {'Count': queryset}
            return Response(context)


class Completed_worksViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    queryset = Schedules.objects.all()
    serializer_class = Schedules_userSerializer
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            queryset = Schedules.objects.filter(name=usersname,status="Completed")
            serializer = Schedules_userSerializer(queryset, many=True)
            return Response(serializer.data)

class Pending_worksViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = Schedules_userSerializer
    queryset = Schedules.objects.all()
    def list(self,request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            queryset = Schedules.objects.filter(name=usersname,status="Pending")
            serializer = Schedules_userSerializer(queryset, many=True)
            return Response(serializer.data)

class Forward_issueViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['patch']
    serializer_class = Forward_issueSerializer
    queryset = Safety_observation_Form.objects.all()


class Get_Forward_issueViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = Get_Forward_issueSerializer
    queryset = Safety_observation_Form.objects.all()
    def list(self,request):
        if request.method=='GET':
            user = request.user
            usersid = user.id
            usersname= user.full_name
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            serializer = Get_Forward_issueSerializer(queryset)
            return Response(serializer.data)


class Assign_Due_dateViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['patch']
    serializer_class = Assign_due_dateSerializer
    queryset = Safety_observation_Form.objects.all()


class Closing_RequestViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['patch']
    serializer_class = Closing_RequestSerializer
    queryset = Safety_observation_Form.objects.all()


class Get_Closing_RequestViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = Get_Close_RequestSerializer
    queryset = Safety_observation_Form.objects.all()


class Close_RequestViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['patch']
    serializer_class = Close_RequestSerializer
    queryset = Safety_observation_Form.objects.all()


class Closed_AfteractionViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = Safety_observation_FormSerializer
    queryset = Safety_observation_Form.objects.all()

class Closed_AfteractioncountViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = CountSerializer
    queryset = Safety_observation_Form.objects.all()
    def list(self,request):
        if request.method=='GET':
            user = request.user
            usersid = user.id

            queryset = Safety_observation_Form.objects.filter(verified_hod=True).count()
            context = {'Count' : queryset}
            return Response(context)


class Hod_NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = NotificationSerializer
    queryset = Safety_observation_Form.objects.all()

    def list(self, request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            role = user.role
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Hod_Notification = Hod_Notification_Form(usersname,company_id)
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            context = {'Notification': Hod_Notification}
            return Response(context)

class Observer_Form_NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = NotificationSerializer
    queryset = Safety_observation_Form.objects.all()

    def list(self, request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            role = user.role
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Observer_Notification = Observer_Notification_Form(usersname,company_id)
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            context = {'Notification': Observer_Notification}
            return Response(context)

class Observer_Next_Schedule_NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = NotificationSerializer
    queryset = Safety_observation_Form.objects.all()

    def list(self, request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            role = user.role
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Observer_Notification_Schedule = Observer_Notification_Schedule_Next(usersname,company_id)
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            context = {'Notification': Observer_Notification_Schedule}
            return Response(context)

class Observer_Completed_Schedule_NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = NotificationSerializer
    queryset = Safety_observation_Form.objects.all()

    def list(self, request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            role = user.role
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Observer_Notification_Schedule_Previous = Observer_Notification_Schedule_Previous_completed(usersname,company_id)
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            context = {'Notification': Observer_Notification_Schedule_Previous}
            return Response(context)

class Observer_Missed_Schedule_NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = NotificationSerializer
    queryset = Safety_observation_Form.objects.all()

    def list(self, request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            role = user.role
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Observer_Notification_Schedule_Previous = Observer_Notification_Schedule_Previous_missed(usersname,company_id)
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            context = {'Notification': Observer_Notification_Schedule_Previous}
            return Response(context)

class Coordinator_New_Form_NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = NotificationSerializer
    queryset = Safety_observation_Form.objects.all()

    def list(self, request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            role = user.role
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Coordinator_Notification_Form = Coordinator_Notification_Form_New(usersname,company_id)
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            context = {'Notification': Coordinator_Notification_Form}
            return Response(context)

class Coordinator_Due_Form_NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = NotificationSerializer
    queryset = Safety_observation_Form.objects.all()

    def list(self, request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            role = user.role
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Coordinator_Notification_Form = Coordinator_Notification_Form_Due(usersname,company_id)
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            context = {'Notification': Coordinator_Notification_Form}
            return Response(context)

class Coordinator_Schedule_Missed_NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = NotificationSerializer
    queryset = Safety_observation_Form.objects.all()

    def list(self, request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            role = user.role
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Coordinator_Notification = Coordinator_Notification_Schedule(usersname,company_id)
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            context = {'Notification': Coordinator_Notification}
            return Response(context)

class Coordinator_Schedule_Missed_NotificationViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    serializer_class = NotificationSerializer
    queryset = Safety_observation_Form.objects.all()

    def list(self, request):
        if request.method == 'GET':
            user = request.user
            usersid = user.id
            usersname = user.full_name
            role = user.role
            company = list(get_user_model().objects.filter(id=usersid).values())
            company_id = ""
            for c in company:
                company_id = c['company_id_id']

            Coordinator_Notification_Form = Coordinator_Notification_Form_Due(usersname,company_id)
            queryset = Safety_observation_Form.objects.filter(hod_name=usersname)
            context = {'Notification':Coordinator_Notification_Form}
            return Response(context)


from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .Serializer import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

