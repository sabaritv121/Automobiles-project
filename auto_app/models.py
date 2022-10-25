from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.



class Login(AbstractUser):
    is_worksmanager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)








class Customer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE,related_name='customer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

    @property
    def get_id(self):
        return self.user.id


class Worksmanager(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="worksmanager")
    name = models.CharField(max_length=100)
    profile_pic= models.FileField(upload_to='profilepic/')
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    email = models.EmailField()

    # @property
    # def get_name(self):
    #     return self.user.first_name+" "+self.user.last_name
    # @property
    # def get_id(self):
    #     return self.user.id
    def __str__(self):
        return self.name
    # #
class Request(models.Model):
    cat=(('two wheeler with gear','two wheeler with gear'),('two wheeler without gear','two wheeler without gear'),('three wheeler','three wheeler'),('four wheeler','four wheeler'))
    category=models.CharField(max_length=50,choices=cat)

    vehicle_no=models.PositiveIntegerField(null=False)
    vehicle_name = models.CharField(max_length=40,null=False)
    vehicle_model = models.CharField(max_length=40,null=False)
    vehicle_brand = models.CharField(max_length=40,null=False)

    problem_description = models.CharField(max_length=500,null=False)
    date=models.DateField(auto_now=True)
    cost=models.PositiveIntegerField(null=True)

    customer=models.ForeignKey('Customer', on_delete=models.DO_NOTHING,null=True)
    worksmanager=models.ForeignKey('Worksmanager',on_delete=models.DO_NOTHING,null=True)

    stat=(('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)

    def __str__(self):
        return self.problem_description


class AppointmentSchedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Appointment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='appointment')
    schedule = models.ForeignKey(AppointmentSchedule, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class Complaints(models.Model):
    user = models.ForeignKey(Login, on_delete=models.DO_NOTHING)
    feedback = models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True, blank=True)

