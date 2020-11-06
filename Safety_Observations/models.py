from django.db import models
from django.utils import *
from Company_Details.models import Company,User
from multiselectfield import MultiSelectField
from rest_framework_simplejwt.tokens import RefreshToken
import time
import datetime
from Safety_Works import settings


discussion_held_choices = (
    ('YES','YES'),
    ('NO','NO'),
)

agreement_choices = (
    ('Agreed','Agreed'),
    ('Disagreed','Disagreed'),
)

types_choices = (
    ('UA','UA'),
    ('UC','UC'),
    ('SA','SA'),
    ('SC','SC'),
)

injury_potential_choices = (
    ('Fatality','Fatality'),
    ('Serious','Serious'),
    ('Minor','Minor'),

)

observation_status_choices = (
    ('Open','Open'),
    ('Close','Close'),
    ('Under progress','Under Progress'),
    ('Overdue','Overdue'),
)


issue_choice = (
    ('RP','RP'),
    ('PP','PP'),
    ('PPE','PPE'),
    ('TE','TE'),
    ('PRO','PRO'),
    ('RP','RP'),
    ('HK','HK'),
    ('Others','Others'),

)

weekmask_choices = (
    ('Monday','Monday'),
    ('Tueday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
)

holiday_type =(
    ('Every Weekends','Every Weekends'),
    ('First Third Weekend','First Third Weekend'),
    ('Secound Fourth Weekend','Secound Fourth Weekend'),
    ('First Third Sunday','First Third Sunday'),
    ('Secound Fourth Sunday','Secound Fourth Sunday'),
)

class Safety_observation_Form(models.Model):
    observer = models.CharField(max_length=50)
    ticket_no = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    total_hours = models.PositiveIntegerField(null=True)
    department = models.CharField(max_length=20,null=True )
    superviser_name = models.CharField(max_length=50,null=True )
    location = models.CharField(max_length=50,null=True )
    excution_department = models.CharField(max_length=200,null=True)

    issue = models.CharField(max_length=20,null=True, choices= issue_choice ,default='RP')

    descrption = models.TextField()
    discussion_held = models.CharField(max_length=3, choices=discussion_held_choices,null=True )
    agreement = models.CharField(max_length=10, choices=agreement_choices, null=True )
    types = models.CharField(max_length=2, choices=types_choices, null=True )
    injury_potential = models.CharField(max_length=10, choices=injury_potential_choices, null=True )
    observation_status = models.CharField(max_length=50, choices=observation_status_choices,null=True )
    image = models.CharField(max_length=200)
    created_by = models.CharField(max_length=100)
    persons_involved = models.CharField(max_length=100)
    safe_situation = models.BooleanField(null=True,default=False)


    companyid = models.CharField(max_length=50)
    verified_hod = models.BooleanField(null=True,default=False)
    hod_name = models.CharField(max_length=50)
    due_date = models.DateField(null=True,blank=True)
    remarks = models.TextField()
    closing_request = models.BooleanField(default=False)
    closing_descrption = models.TextField()
    closing_image = models.CharField(max_length=500,null=True)
    closed_date = models.DateField(null=True,blank=True)


class Scheduler(models.Model):
    companyid = models.CharField(max_length=50)
    holidays = models.CharField(max_length=500,help_text='Please Enter the Dates in DD/MM/YYYY Format')
    weekmask = MultiSelectField(choices=weekmask_choices,null=True)
    holiday_types = models.CharField(max_length=50,choices=holiday_type,null=True)
    observations_required =  models.PositiveIntegerField(null=False)

status_choices=(
    ('Pending','Pending'),
    ('Completed','Completed'),
    ('Missed','Missed')
)


class Schedules(models.Model):
    companyid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    reschedule_date = models.DateField(null=True)
    status = models.CharField(max_length=30,choices=status_choices,null=True)
    reason_reschedule = models.TextField(null=True)


class Count(models.Model):
    count = models.PositiveIntegerField()

class Notification(models.Model):
    notification = models.CharField(max_length=100000)