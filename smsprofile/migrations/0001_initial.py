# Generated by Django 3.2.7 on 2021-09-02 09:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('level', models.CharField(choices=[('T', 'Teacher'), ('DI', 'Discipline Incharge'), ('SM', 'Sports Manager'), ('PM', 'Program Manger'), ('C', 'Coordinator'), ('P', 'Principal'), ('CM', 'Chairman'), ('H', 'Helper')], default=('T', 'Teacher'), max_length=20)),
                ('subject', models.CharField(choices=[('M', 'Math'), ('E', 'English'), ('S', 'Social'), ('Sc', 'Science'), ('G', 'Grammar'), ('GK', 'General Knowledge'), ('EPH', 'Envronment Population and Health'), ('Com', 'Computer Science'), ('Ac', 'Accounting')], max_length=40)),
                ('post_status', models.CharField(choices=[('P', 'Permanent'), ('T', 'Temperory'), ('Tr', 'Trainee'), ('C', 'Contract')], default=('P', 'Permanent'), max_length=20)),
                ('joined_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('academic_level', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg', models.IntegerField()),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30)),
                ('DOB', models.DateTimeField()),
                ('joined_date', models.DateTimeField(null=True)),
                ('guardian_first_name', models.CharField(max_length=30)),
                ('guardian_middle_ame', models.CharField(max_length=30, null=True)),
                ('guardian_last_name', models.CharField(max_length=30)),
                ('guardian_contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('guardian_email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]