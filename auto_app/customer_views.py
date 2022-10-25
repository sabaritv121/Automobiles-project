from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import redirect, render

from auto_app import models
from auto_app.filters import StatusFilter
from auto_app.forms import LoginRegister, CustomerRegister, FeedbackForm
from auto_app.models import Customer, AppointmentSchedule, Appointment, Request, Complaints


def customer_reg(request):
    form1=LoginRegister()
    form2=CustomerRegister()
    if request.method =='POST':
         form1 = LoginRegister(request.POST)
         form2 = CustomerRegister(request.POST)

         if form1.is_valid() and form2.is_valid():
                user = form1.save(commit=False)
                user.is_customer = True
                user.save()
                user1 = form2.save(commit=False)
                user1.user = user
                user1.save()
                return redirect('home')

    return render(request, 'customer/register.html', {'form1': form1, 'form2': form2})


# def customer_profile_view(request,id):
#     customer=Customer.objects.get(id=id)
#     return render(request,'customer/customerprofile.html',{'customer':customer})
@login_required(login_url='login_view')
def cus_home(request):
    return render(request, 'customer/cus_home.html')

@login_required(login_url='login_view')
def schedule_cus(request):
    s = AppointmentSchedule.objects.all()
    # scheduleFilter = ScheduleFilter(request.GET, queryset=s)
    # s = scheduleFilter.qs
    context = {
        'schedule': s,
        # 'scheduleFilter': scheduleFilter,
    }
    return render(request, 'customer/cus_schedule.html', context)

@login_required(login_url='login_view')
def take_appointment(request, id):
    schedule = AppointmentSchedule.objects.get(id=id)
    u = Customer.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u , schedule=schedule)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect("schedule_cus")
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('appointments')
    return render(request, 'customer/take_appointment.html', {'schedule': schedule})

@login_required(login_url='login_view')
def appointments(request):
    u = Customer.objects.get(user=request.user)
    a = Appointment.objects.filter(user=u)
    return render(request, 'customer/cus_appointment.html', {'appointment': a})

@login_required(login_url='login_view')
def status(request):

    p = Request.objects.all()
    statusFilter = StatusFilter(request.GET, queryset=p)
    p = statusFilter.qs
    context = {
        'data': p,
        'statusFilter': statusFilter,
    }
    return render(request, 'customer/statt.html', context)

@login_required(login_url='login_view')
def feedback(request):
    form=FeedbackForm
    u= request.user

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request,"thank you for your feedback...!!!")
            return redirect('feedback_view')
    else:
        form = FeedbackForm()
    return render(request,'customer/feedback.html',{'form':form})


@login_required(login_url='login_view')
def feedback_view(request):
    u = Complaints.objects.filter(user=request.user)
    return render(request,"customer/fb_view.html",{'feedback':u})

