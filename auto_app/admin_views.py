from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from . import models, forms
from .forms import LoginRegister, WorksmanagerRegister, ScheduleAdd, RequestForm
from .models import Worksmanager, AppointmentSchedule, Request, Complaints, Customer


@login_required(login_url='login_view')
def worksmanager_add(request):
    form1=LoginRegister()
    form2=WorksmanagerRegister()
    if request.method =='POST':
         form1 = LoginRegister(request.POST)
         form2 = WorksmanagerRegister(request.POST,request.FILES)

         if form1.is_valid() and form2.is_valid():
                user = form1.save(commit=False)
                user.is_worksmanager = True
                user.save()
                user1 = form2.save(commit=False)
                user1.user = user
                user1.save()
                return redirect('aaaAdmin')

    return render(request, 'admin/worksmanager_add.html', {'form1': form1, 'form2': form2})

@login_required(login_url='login_view')
def worksmanager_view(request):
    data=Worksmanager.objects.all()
    return render(request,"admin/view_manager.html",{'data':data})

#delete worksmanager

def delete_wmmanager_view(request,user_id):
    wm=models.Worksmanager.objects.get(user_id=user_id)
    wm.delete()
    return redirect('worksmanager_view')

# def update_mechanic_view(request,pk):
#     wm=models.Worksmanager.objects.get(id=pk)
#
#     userForm=forms.MechanicUserForm(instance=user)
#     mechanicForm=forms.MechanicForm(request.FILES,instance=mechanic)
#     mydict={'userForm':userForm,'mechanicForm':mechanicForm}
#     if request.method=='POST':
#         userForm=forms.MechanicUserForm(request.POST,instance=user)
#         mechanicForm=forms.MechanicForm(request.POST,request.FILES,instance=mechanic)
#         if userForm.is_valid() and mechanicForm.is_valid():
#             user=userForm.save()
#             user.set_password(user.password)
#             user.save()
#             mechanicForm.save()
#             return redirect('admin-view-mechanic')
#     return render(request,'vehicle/update_mechanic.html',context=mydict)

@login_required(login_url='login_view')
def wm_update(request, user_id):
    n = Worksmanager.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = WorksmanagerRegister(request.POST , request.FILES or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('worksmanager_view')
    else:
        form = WorksmanagerRegister(instance=n)
    return render(request, 'admin/wm_update.html', {'form': form})

@login_required(login_url='login_view')
def schedule_add(request):
    form = ScheduleAdd()
    if request.method == 'POST':
        form = ScheduleAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, ' Schedule Added Successfully')
            return redirect('schedule_view')
    else:
        form = ScheduleAdd()
    return render(request, 'admin/schedule_add.html', {'form': form})

@login_required(login_url='login_view')
def schedule(request):
    n = AppointmentSchedule.objects.all()
    # scheduleFilter = ScheduleFilter(request.GET, queryset=n)
    # n = scheduleFilter.qs
    context = {
        'schedule': n,
        # 'scheduleFilter': scheduleFilter,
    }
    return render(request, 'admin/schedule_view.html', context)

#
@login_required(login_url='login_view')
def schedule_delete(request, id):
    n = AppointmentSchedule.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, 'Schedule Deleted Successfully')
        return redirect('schedule_view')

@login_required(login_url='login_view')
def works(request):
    form1=RequestForm()
    # form2=AdminRequestForm()
    if request.method =='POST':
         form1 = RequestForm(request.POST)
         # form2 = AdminRequestForm(request.POST)

         if form1.is_valid():
             form1.save()
         # if form2.is_valid():
         #     form2.save()
         return redirect('aaaAdmin')


    return render(request, 'admin/admin_add_work.html', {'form1': form1})

@login_required(login_url='login_view')
def works_view(request):
    data = Request.objects.all()
    return render(request, 'admin/works_view.html', {'data': data})


def works_delete(request,id):
    data = Request.objects.get(id=id)
    if request.method == 'POST':
          data.delete()
          return redirect('works_view')

@login_required(login_url='login_view')
def reply_feedback(request, id):
    feedback = Complaints.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('feedbacks')
    return render(request, 'admin/admin_feedback.html', {'feedback': feedback})

@login_required(login_url='login_view')
def feedbacks(request):
    n = Complaints.objects.all()
    return render(request,'admin/feedbacks.html',{'feedbacks':n})

def customerview(request):
    p=Customer.objects.all()
    return render(request,'admin/customerview.html',{'view':p})

@login_required(login_url='login_view')
def customer_delete(request, user_id):
        n = Customer.objects.get(user_id=user_id)
        if request.method == 'POST':
            n.delete()
            return redirect('customerview')
        else:
            return redirect('customerview')