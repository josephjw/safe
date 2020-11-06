# Generated by Django 3.1.2 on 2020-11-05 05:20

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Safety_observation_Form',
            fields=[
                ('observer', models.CharField(max_length=50)),
                ('ticket_no', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('total_hours', models.PositiveIntegerField(null=True)),
                ('department', models.CharField(max_length=20, null=True)),
                ('superviser_name', models.CharField(max_length=50, null=True)),
                ('excution_department', models.CharField(max_length=200, null=True)),
                ('issue', models.CharField(choices=[('RP', 'RP'), ('PP', 'PP'), ('PPE', 'PPE'), ('TE', 'TE'), ('PRO', 'PRO'), ('RP', 'RP'), ('HK', 'HK'), ('Others', 'Others')], default='RP', max_length=20, null=True)),
                ('descrption', models.TextField()),
                ('discussion_held', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=3, null=True)),
                ('agreement', models.CharField(choices=[('Agreed', 'Agreed'), ('Disagreed', 'Disagreed')], max_length=10, null=True)),
                ('types', models.CharField(choices=[('UA', 'UA'), ('UC', 'UC'), ('SA', 'SA'), ('SC', 'SC')], max_length=2, null=True)),
                ('injury_potential', models.CharField(choices=[('Fatality', 'Fatality'), ('Serious', 'Serious'), ('Minor', 'Minor')], max_length=10, null=True)),
                ('observation_status', models.CharField(choices=[('Open', 'Open'), ('Close', 'Close'), ('Under progress', 'Under Progress'), ('Overdue', 'Overdue')], max_length=50, null=True)),
                ('image', models.CharField(max_length=200)),
                ('created_by', models.CharField(max_length=100)),
                ('persons_involved', models.CharField(max_length=100)),
                ('safe_situation', models.BooleanField(default=False, null=True)),
                ('companyid', models.CharField(max_length=50)),
                ('verified_hod', models.BooleanField(default=False, null=True)),
                ('hod_name', models.CharField(max_length=50)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('remarks', models.TextField()),
                ('closing_request', models.BooleanField(default=False)),
                ('closing_descrption', models.TextField()),
                ('closing_image', models.CharField(max_length=500, null=True)),
                ('closed_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyid', models.CharField(max_length=50)),
                ('holidays', models.CharField(help_text='Please Enter the Dates in DD/MM/YYYY Format', max_length=500)),
                ('weekmask', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tueday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=55, null=True)),
                ('holiday_types', models.CharField(choices=[('Every Weekends', 'Every Weekends'), ('First Third Weekend', 'First Third Weekend'), ('Secound Fourth Weekend', 'Secound Fourth Weekend'), ('First Third Sunday', 'First Third Sunday'), ('Secound Fourth Sunday', 'Secound Fourth Sunday')], max_length=50, null=True)),
                ('observations_required', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('reschedule_date', models.DateField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Missed', 'Missed')], max_length=30, null=True)),
            ],
        ),
    ]
