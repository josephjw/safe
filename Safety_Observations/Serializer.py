from rest_framework import serializers
from .models import *
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
# from .Scheduler import Schedules_operation
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from Company_Details.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class Safety_FormSerializer(serializers.ModelSerializer):
    class Meta():
        model = Safety_observation_Form
        fields= '__all__'



class Safety_observation_FormSerializer(serializers.ModelSerializer):
    class Meta():
        model = Safety_observation_Form
        exclude = ('issue','observer','companyid','created_by','hod_name','due_date','remarks','closing_request','closing_descrption','closing_image','closed_date','verified_hod')


class Others_FormsSerializer(serializers.ModelSerializer):

    class Meta():
        model = Safety_observation_Form
        exclude = ('issue','companyid','discussion_held','agreement','types','injury_potential','observation_status','hod_name','due_date','remarks','closing_request','closing_descrption','closing_image','closed_date','verified_hod')

class Safe_situationSerializer(serializers.ModelSerializer):

    class Meta():
        model = Safety_observation_Form
        fields = ('total_hours','department','location','superviser_name','excution_department','safe_situation')

class Forward_issueSerializer(serializers.ModelSerializer):

    class Meta():
        model = Safety_observation_Form
        fields = ('hod_name',)

class Get_Forward_issueSerializer(serializers.ModelSerializer):

    class Meta():
        model = Safety_observation_Form
        exclude = ('companyid',)

class Assign_due_dateSerializer(serializers.ModelSerializer):

    class Meta():
        model = Safety_observation_Form
        fields = ('due_date','remarks','observation_status')

class Closing_RequestSerializer(serializers.ModelSerializer):

    class Meta():
        model = Safety_observation_Form
        fields = ('closing_descrption','closing_image',)

class Get_Close_RequestSerializer(serializers.ModelSerializer):

    class Meta():
        model = Safety_observation_Form
        fields = ('ticket_no','closing_descrption','closing_image',)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        data.update({'user': self.user.email})
        data.update({'role': self.user.role})
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.role
        return token


class SchedulesSerializer(serializers.ModelSerializer):

    class Meta():
        model = Schedules
        fields = '__all__'

class SchedulerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Scheduler
        fields = ('holidays','weekmask','holiday_types','observations_required',)


class OpenissuesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Safety_observation_Form
        fields = '__all__'

class CloseissuesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Safety_observation_Form
        fields = '__all__'

class Close_RequestSerializer(serializers.ModelSerializer):

    class Meta():
        model = Safety_observation_Form
        fields = ('observation_status',)


class Schedules_userSerializer(serializers.ModelSerializer):

    class Meta():
        model = Schedules
        fields = '__all__'

class ReschedulerSerializer(serializers.ModelSerializer):
    class Meta():
        model = Schedules
        fields = ('date','reschedule_date','reason_reschedule')

class Start_workSerializer(serializers.ModelSerializer):
    class Meta():
        model = Schedules
        fields = ('date',)


class CountSerializer(serializers.ModelSerializer):
    class Meta():
        model = Count
        fields = ('count',)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta():
        model = Notification
        fields = ('notification',)

