from datetime import date,timedelta
import random
import datetime
import holidays
import calendar
from calendar import monthrange
import pandas as pd
from .models import *
from Company_Details.models import Department
from rest_framework import status,viewsets
from . import Serializer
#from .models import *
import time
from Company_Details.models import Company,User
from django.contrib.auth import get_user_model
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
#class Schedules_operation():
def add_months(sourcedate, months):
        month = sourcedate.month - 1 + months
        year = sourcedate.year + month // 12
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year,month)[1])
        return date(year, month, day)
def last_day_of_month(date_value):
        return date_value.replace(day = monthrange(date_value.year, date_value.month)[1])

def list_to_str(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1



def Shedules_operation(usersid):
    company_id = get_user_model().objects.filter(id=usersid).values_list('company_id_id',flat=True)
    for c in company_id:
        company_id=c
    names = []
    name = get_user_model().objects.filter(company_id_id=company_id,role__startswith="Observer").values()
    for n in name:
        names.append(n['full_name'])
    locations = []
    location = Department.objects.annotate(name=Concat('department',V('('),'locations_names',V(')'),output_field=CharField())).filter(companyid=company_id).values()
    for L in location:
        locations.append(L['name'])
    company = Scheduler.objects.all().filter(companyid=company_id)
    weekmask = ""
    choices = ""
    holidays = ""
    for c in company:
        weekmask = c.weekmask
        choices = c.holiday_types
        holidays = c.holidays
        observations_required = c.observations_required
        
    weekmask = weekmask
    choices = choices
    choices = list_to_str(choices)
    start = date.today().replace(day=25)
    end = add_months(start,1)
    start_dt = start.toordinal()
    end_dt = end.toordinal()
    stdt = end.replace(day=1)
    enddt = last_day_of_month(end)
    holidaysss = []
    hol = []
    holi = list(Scheduler.objects.values_list('holidays', flat=True))
    for h in holi:
        holi = datetime.datetime.strptime(str(h), '%d/%m/%Y').date()
        holidaysss.append(holi)

    previous_stdt = date.today().replace(day=1)
    previous_enddt = last_day_of_month(previous_stdt)
    previous_weekend = pd.date_range(start=previous_stdt, end=previous_enddt,freq='W-SAT').strftime('%d/%m/%Y').tolist()
    pre_sat = previous_weekend[3]
    pre_sat4 = datetime.datetime.strptime(str(pre_sat), '%d/%m/%Y').date()
    pre_sun4 = pre_sat4+ timedelta(days=1)


    present_weekend = pd.date_range(start=stdt, end=enddt,freq='W-SAT').strftime('%d/%m/%Y').tolist()
    sat1 = present_weekend[0]
    sat2 = present_weekend[1]
    sat3 = present_weekend[2]
    sat4 = present_weekend[3]
    sat1 = datetime.datetime.strptime(str(sat1), '%d/%m/%Y').date()
    sun1 = sat1+ timedelta(days=1)
    sat2 = datetime.datetime.strptime(str(sat2), '%d/%m/%Y').date()
    sun2 = sat2+ timedelta(days=1)
    sat3 = datetime.datetime.strptime(str(sat3), '%d/%m/%Y').date()
    sun3 = sat3+ timedelta(days=1)
    sat4 = datetime.datetime.strptime(str(sat4), '%d/%m/%Y').date()
    sun4 = sat4+ timedelta(days=1)
    first_third_weekend =[]
    second_fourth_weekend = []
    first_third_sunday = []
    second_fourth_sunday = []
    first_third_weekend.append(sat1)
    first_third_weekend.append(sun1)
    first_third_weekend.append(sat3)
    first_third_weekend.append(sun3)
    for i in holidaysss:
        first_third_weekend.append(i)


    second_fourth_weekend.append(sat2)
    second_fourth_weekend.append(sun2)
    second_fourth_weekend.append(sat4)
    second_fourth_weekend.append(sun4)
    second_fourth_weekend.append(pre_sat4)
    second_fourth_weekend.append(pre_sun4)
    for i in holidaysss:
        second_fourth_weekend.append(i)

    first_third_sunday.append(sun1)
    first_third_sunday.append(sun3)
    for i in holidaysss:
        first_third_sunday.append(i)


    second_fourth_sunday.append(sun2)
    second_fourth_sunday.append(sun4)
    second_fourth_sunday.append(pre_sun4)
    for i in holidaysss:
        second_fourth_sunday.append(i)


    def Option1(holidaysss):
        weekmask = 'Mon Tue Wed Thu Fri'
        working_days = pd.bdate_range(start=start,end=end,weekmask=weekmask,holidays=holidaysss,freq="C")
        working_days = [x.strftime('%d/%m/%Y') for x in working_days]
        for i in range(observations_required):
            for n in names:
                a =random.choice(names)
                b = random.choice(locations)
                random_day = random.choice(working_days)
                s = Schedules(name=n,date=random_day,location=b,companyid=company_id,status="Pending")
                s.save()


    def Option2():
        weekmask = 'Mon Tue Wed Thu Fri Sat Sun'
        working_days = pd.bdate_range(start=start,end=end,weekmask=weekmask,holidays=first_third_weekend,freq="C")
        working_days = [x.strftime('%d/%m/%Y') for x in working_days]
        name = str(names)
        for i in range(observations_required):
            for n in names:
                a =random.choice(names)
                b = random.choice(locations)
                random_day = random.choice(working_days)
                s = Schedules(name=n,date=random_day,location=b,companyid=company_id,status="Pending")
                s.save()
    def Option3():
        weekmask = 'Mon Tue Wed Thu Fri Sat Sun'
        working_days = pd.bdate_range(start=start,end=end,weekmask=weekmask,holidays=second_fourth_weekend,freq="C")
        working_days = [x.strftime('%d/%m/%Y') for x in working_days]
        name = str(names)
        for i in range(observations_required):
            for n in names:
                a =random.choice(names)
                b = random.choice(locations)
                random_day = random.choice(working_days)
                s = Schedules(name=n,date=random_day,location=b,companyid=company_id,status="Pending")
                s.save()


    def Option4():
        weekmask = 'Mon Tue Wed Thu Fri Sat Sun'
        working_days = pd.bdate_range(start=start,end=end,weekmask=weekmask,holidays=first_third_sunday,freq="C")
        working_days = [x.strftime('%d/%m/%Y') for x in working_days]
        name = str(names)
        for i in range(observations_required):
            for n in names:
                a =random.choice(names)
                b = random.choice(locations)
                random_day = random.choice(working_days)
                s = Schedules(name=n,date=random_day,location=b,companyid=company_id,status="Pending")
                s.save()


    def Option5():
        weekmask = 'Mon Tue Wed Thu Fri Sat Sun'
        working_days = pd.bdate_range(start=start,end=end,weekmask=weekmask,holidays=second_fourth_sunday,freq="C")
        working_days = [x.strftime('%d/%m/%Y') for x in working_days]
        name = str(names)
        for i in range(observations_required):
            for n in names:
                a =random.choice(names)
                b = random.choice(locations)
                random_day = random.choice(working_days)
                s = Schedules(name=n,date=random_day,location=b,companyid=company_id,status="Pending")
                s.save()



    def Option6(weekmask,holidaysss):
        working_days = pd.bdate_range(start=start,end=end,weekmask=weekmask,holidays=holidaysss,freq="C")
        working_days = [x.strftime('%d/%m/%Y') for x in working_days]
        name = str(names)
        for i in range(observations_required):
            for n in names:
                a =random.choice(names)
                b = random.choice(locations)
                random_day = random.choice(working_days)
                s = Schedules(name=n,date=random_day,location=b,companyid=company_id,status="Pending")
                s.save()


    if choices == 'Every Weekends':
        Option1(holidaysss)
    elif choices == 'First Third Weekend':
        Option2()
    elif choices == 'Secound Fourth Weekend':
        Option3()
    elif choices == 'First Third Sunday':
        Option4()
    elif choices == 'Secound Fourth Sunday':
        Option5()
    elif choices == 'None':
        Option6(weekmask,holidaysss)
