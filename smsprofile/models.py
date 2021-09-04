from django.db import models
from django.utils import timezone
class Staff(models.Model):
    STAFF_POSTS=(
        ('T','Teacher'),
        ('DI','Discipline Incharge'),
        ('SM','Sports Manager'),
        ('PM','Program Manger'),
        ('C','Coordinator'),
        ('P','Principal'),
        ('CM','Chairman'),
        ('H','Helper')
    )
    SUBJECTS=(
        ('M','Math'),
        ('E','English'),
        ('S','Social'),
        ('Sc','Science'),
        ('G','Grammar'),
        ('GK','General Knowledge'),
        ('EPH','Envronment Population and Health'),
        ('Com','Computer Science'),
        ('Ac','Accounting')
    )
    POST_STATUS=(
        ('P','Permanent'),
        ('T','Temperory'),
        ('Tr','Trainee'),
        ('C','Contract')
    )
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)
    level = models.CharField(max_length=20,choices=STAFF_POSTS, default=STAFF_POSTS[0])
    subject = models.CharField(max_length=40, choices=SUBJECTS, null=False)
    post_status = models.CharField(max_length=20,choices=POST_STATUS, default=POST_STATUS[0])
    joined_date = models.DateTimeField(default=timezone.now)
    academic_level = models.CharField(max_length=50,null=False)
    # citizenship_id=models.CharField(max_length=15, null=True, blank=True)
    # sallery_multiplier = models.FloatField(default=1.0, null=True)
    contact = models.IntegerField()
    # address = models.CharField(max_length=100)

    def __str__(self):
        middle_name = '' if self.middle_name is None else self.middle_name
        return f'{self.first_name} {middle_name} {self.last_name}'

class Guardian(models.Model):
    father_first_name=models.CharField(max_length=30,null=True)
    father_middle_name=models.CharField(max_length=30,null=True)
    father_last_name=models.CharField(max_length=30,null=True)
    father_email = models.EmailField(null=True)
    father_contact=models.IntegerField(null=True)
    father_address_district=models.CharField(max_length=40,null=True)
    father_address_municipality = models.CharField(max_length=40,null=True)
    father_address_tole=models.CharField(max_length=40,null=True)

    mother_first_name=models.CharField(max_length=30,null=True)
    mother_middle_name=models.CharField(max_length=30,null=True)
    mother_last_name=models.CharField(max_length=30,null=True)
    mother_email = models.EmailField(null=True)
    mother_contact=models.IntegerField(null=True)
    mother_address_district=models.CharField(max_length=40,null=True)
    mother_address_municipality = models.CharField(max_length=40,null=True)
    mother_address_tole=models.CharField(max_length=40,null=True)

    guardian_first_name=models.CharField(max_length=30)
    guardian_middle_name=models.CharField(max_length=30)
    guardian_last_name=models.CharField(max_length=30)
    relation=models.CharField(max_length=30)
    guardian_email = models.EmailField()
    guardian_contact=models.IntegerField()
    guardian_address_district=models.CharField(max_length=40)
    guardian_address_municipality = models.CharField(max_length=40)
    guardian_address_tole=models.CharField(max_length=40)
    

class Student(models.Model):
    reg = models.IntegerField(null=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)
    DOB = models.DateTimeField(null=False)
    gender = models.CharField(max_length=10)
    joined_date = models.DateTimeField(null=True)
    address_district=models.CharField(max_length=40)
    address_municipality = models.CharField(max_length=40)
    address_tole=models.CharField(max_length=40)
    email = models.EmailField(null=True)
    guardian = models.ForeignKey('Guardian', on_delete = models.SET_NULL, null=True)

    def __str__(self):
        middle_name = '' if self.middle_name is None else self.middle_name
        return f'{self.first_name} {middle_name} {self.last_name}'
