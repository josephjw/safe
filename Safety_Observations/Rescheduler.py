from datetime import date,timedelta
import datetime
from .models import *


def update_next(schedule_id,reschedule_date):

    Schedules.objects.filter(id=schedule_id).update(reschedule_date=reschedule_date)
    print("updated")

def update_previous(shedule_id,reschedule_date):

    Schedules.objects.filter(id=schedule_id).update(reschedule_date=reschedule_date)
    print("updated1")

def reschedule(next_dayss,previous_dayss,user_id,date,reschedule_date,shedule_id):

    for i in next_dayss:
        print(i)
        if (reschedule_date==i):
            update_next(schedule_id,reschedule_date)
            break


    for reschedule in previous_dayss:
        if (reschedule_date==reschedule):
            update_previous(schedule_id,reschedule_date)
            break
    
    return("Done")

def listToString(s):
    str1 = " "
    for ele in s:  
        str1 += ele
    return str1



def rescheduler_operation(date,reschedule_date,user_id):
    next_dayss=[]
    previous_dayss=[]
    print(date)
    base = date
    print(type(base))
    date = datetime.datetime.strptime(str(date), '%d/%m/%Y').date()
    #base1 = datetime.datetime.strptime(base,'%d/%m/%Y').strftime('%d/%m/%Y')
    #base1 = datetime.datetime.strptime(base1, '%d/%m/%Y').date() 
    print(date)
    for x in range(1, 5):
        next_days = date + timedelta(days=x)
        #next_days=next_days.date()
        next_dayss.append(next_days)
    

    for x in range(1, 5):
        previous_days = date - timedelta(days=x)
        #previous_days = previous_days.date()
        previous_dayss.append(previous_days)

    print(next_dayss)  
    print(previous_dayss)  

    scheduled = list(Schedules.objects.filter(user_id=user_id,date=date).values())
    for schedule in scheduled:
        shedule_id = schedule['id']
        print(shedule_id)
        reschedule(next_dayss,previous_dayss,user_id,date,reschedule_date,shedule_id)


    


