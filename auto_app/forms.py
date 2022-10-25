import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Login, Worksmanager, Customer, AppointmentSchedule, Request, Complaints, Chat


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2',)


class WorksmanagerRegister(forms.ModelForm):


    class Meta:
        model = Worksmanager
        fields = "__all__"
        exclude = ("user",)

#
class CustomerRegister(forms.ModelForm):

    class Meta:
        model = Customer
        field = "__all__"
        exclude = ("user",)

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class ScheduleAdd(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    start_time = forms.TimeField(widget=TimeInput,)
    end_time = forms.TimeField(widget=TimeInput, )

    class Meta:
        model = AppointmentSchedule
        fields = ('date', 'start_time', 'end_time')

def clean(self):
    cleaned_data = super().clean()
    start = cleaned_data.get("start_time")
    end = cleaned_data.get("end_time")
    date = cleaned_data.get("date")
    if start > end:
        raise forms.ValidationError("End Time should be greater than start Time.")

    if date < datetime.date.today():
        raise forms.ValidationError("Date can't be in the past")
    return cleaned_data

class RequestForm(forms.ModelForm):
    # customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    # worksmanager = forms.ModelChoiceField(queryset=Worksmanager.objects.all())

    class Meta:
        model=Request
        fields=['category','vehicle_no','vehicle_name','vehicle_model','vehicle_brand','problem_description','cost','customer','worksmanager','status']
        widgets = {
        'problem_description':forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Complaints
        fields = ('feedback',)

# class AdminRequestForm(forms.ModelForm):
#     #to_field_name value will be stored when form is submitted.....__str__ method of customer model will be shown there in html
#     customer=forms.ModelChoiceField(queryset=Customer.objects.all(),empty_label="Customer Name",to_field_name='id')
#     mechanic=forms.ModelChoiceField(queryset=Worksmanager.objects.all(),empty_label="manager Name",to_field_name='id')
#     cost=forms.IntegerField()

class ChatcontentForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['from_id','to_id','content']