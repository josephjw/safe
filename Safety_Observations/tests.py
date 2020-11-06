from django.test import TestCase
from datetime import date,timedelta
from .models  import Schedules,Safety_observation_Form
import datetime
# Create your tests here.


def Missed_Schedule(due_date,company_id):
    datess = []
    for h in due_date:
        d = datetime.datetime.strptime(str(h), '%d/%m/%Y').date()
        datess.append(d)
    today = datetime.date.today().strftime('%d/%m/%Y')
    toda = datetime.datetime.strptime(today, '%d/%m/%Y').date()
    due = toda + timedelta(days=1)
    due_dated = due.strftime('%d/%m/%Y')
    due  = datetime.datetime.strptime(due_dated, '%d/%m/%Y').date()
    datess = [x.strftime('%d/%m/%Y') for x in datess]
    for data in datess:
        final_date = datetime.datetime.strptime(data, '%d/%m/%Y').date()
        if final_date < due:
            update_date = final_date.strftime('%d/%m/%Y')
            Missed = Schedules.objects.filter(companyid=company_id,date=update_date,status="Pending").update(status="Missed")
            dues = datetime.datetime.strptime(update_date, '%d/%m/%Y').date()
            Missed = Schedules.objects.filter(companyid=company_id,reschedule_date=dues,status="Pending").update(status="Missed")
        else:
            pass

def Overdue_check(due_date,company_id):
    today = datetime.date.today()
    due_test = due_date
    for data in due_test:
        if data > today:
            updating = Safety_observation_Form.objects.filter(companyid=company_id, due_date=data,observation_status="Open").update(observation_status="Overdue")
            updating = Safety_observation_Form.objects.filter(companyid=company_id, due_date=data,observation_status="Under progress").update(observation_status="Overdue")
        else:
            pass

from django.db.models import Q

def Observer_Notification_Form(usersname,company_id):
    today = datetime.date.today()
    pervious_days = today - timedelta(days=2)


    form_count = Safety_observation_Form.objects.filter(companyid=company_id,created_by=usersname).filter(Q(date__gte=pervious_days)).count()

    if form_count > 0:
        Form_Notify = (usersname ,"You have created",+form_count,  "new Safety Observation form in past two days ")
        return Form_Notify
    else:
        pass

    #return (Form_Notify)


def Observer_Notification_Schedule_Next(usersname, company_id):
    today = datetime.date.today()
    pervious_days = today + timedelta(days=2)

    schedule_count = Schedules.objects.filter(name=usersname,companyid=company_id,status="Pending").filter(date__gte=pervious_days).count()

    if schedule_count > 0:
        Schedule_Notify_Next = (usersname, "You have ", +schedule_count, "Schedules pending")
        return Schedule_Notify_Next
    else:
        pass
    #return (Schedule_Notify_Next)

def Observer_Notification_Schedule_Previous_completed(usersname, company_id):
    today = datetime.date.today()
    previous_days = today - timedelta(days=2)

    schedule_count = Schedules.objects.filter(name=usersname,companyid=company_id,status="Completed").filter(date__gte=previous_days).count()

    if schedule_count > 0:
        Schedule_Notify_Previous = (usersname, "You have completed", +schedule_count, "in previous two days")
        return Schedule_Notify_Previous
    else:
        pass
    #return (Schedule_Notify_Previous)

def Observer_Notification_Schedule_Previous_missed(usersname, company_id):
    today = datetime.date.today()
    previous_days = today - timedelta(days=2)

    schedule_count = Schedules.objects.filter(name=usersname,companyid=company_id,status="Missed").filter(date__gte=previous_days).count()

    if schedule_count > 0:
        Schedule_Notify_Previous = (usersname, "You have completed", +schedule_count, "in previous two days")
        return Schedule_Notify_Previous
    else:
        pass
    #return (Schedule_Notify_Previous)

def Hod_Notification_Form(usersname,company_id):
    today = datetime.date.today()
    next_days = today + timedelta(days=2)


    form_count = Safety_observation_Form.objects.filter(companyid=company_id,hod_name=usersname).filter(Q(due_date__lte=next_days)).count()

    if form_count > 0:
        Form_Notify = (usersname, "You have ",+form_count,  "Safety Observation due date in next two days ")
        return Form_Notify
    else:
        pass

    #return (Form_Notify)

def Coordinator_Notification_Form_New(usersname,company_id):
    today = datetime.date.today()
    previous_days = today - timedelta(days=2)


    form_count = Safety_observation_Form.objects.filter(companyid=company_id).filter(Q(date__gte=previous_days)).count()

    if form_count > 0:
        Form_Notify = (usersname, "You have ",+form_count,  "new Safety Observation created in past two days ")
        return Form_Notify
    else:
        pass

    #return (Form_Notify)

def Coordinator_Notification_Schedule(usersname,company_id):
    today = datetime.date.today()
    previous_days = today - timedelta(days=3)


    form_count = Schedules.objects.filter(companyid=company_id,status="Missed").filter(Q(date__gte=previous_days)).count()
    if form_count > 0:
        Form_Notify = (usersname, +form_count,"Observers have missed the schedules in  past two days ")
        return Form_Notify
    else:
        pass

    #return (Form_Notify)

def Coordinator_Notification_Form_Due(usersname,company_id):
    today = datetime.date.today()
    next_days = today + timedelta(days=2)


    form_count = Safety_observation_Form.objects.filter(companyid=company_id).filter(Q(due_date__lte=next_days)).count()

    if form_count > 0:
        Form_Notify = (usersname, "You have ",+form_count,  "Safety Observation due date in next two days ")
        return Form_Notify
    else:
        pass

    #return (Form_Notify)