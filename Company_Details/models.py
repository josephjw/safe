from django.db import models



class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    purchased_modules = models.CharField(max_length=255)

roles_choices = (
    ('Observer','Observer'),
    ('Coordinator','Coordinator'),
    ('Hod','Hod'),

)

class Department(models.Model):
    
    department =  models.CharField(max_length=50)
    hod_name = models.CharField(max_length=50)
    locations_names = models.CharField(max_length=50)
    companyid = models.CharField(max_length=50)


from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        #extra_fields.setdefault('is_staff', False)
        #extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50)
    role = models.CharField(max_length=50,choices=roles_choices,default='Hod')
    department = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=30,unique=True)
    mobile_number = models.CharField(max_length=15,unique=True)
    date_of_birth = models.DateField()
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

