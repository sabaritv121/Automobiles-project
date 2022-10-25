from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from auto_app.forms import RequestForm
from auto_app.models import Appointment, Request


@login_required(login_url='login_view')
def manager_home(request):
    return render(request, 'worksmanager/manager_home.html')

@login_required(login_url='login_view')
def appointment_admin(request):
    p = Appointment.objects.all()   
    # placeFilter = PlaceFilter(request.GET, queryset=p)
    # p = placeFilter.qs
    context = {
        'appointment': p,
        # 'placeFilter': placeFilter,
    }
    return render(request, 'worksmanager/appointment.html', context)

@login_required(login_url='login_view')
def approve_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')

@login_required(login_url='login_view')
def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')

@login_required(login_url='login_view')
def works_view1(request):
    data = Request.objects.all()
    return render(request, 'worksmanager/works_view.html', {'data': data})

@login_required(login_url='login_view')
def wm_status(request,id):
    n = Request.objects.get(id=id)
    if request.method == 'POST':
        form = RequestForm(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('works_view1')
    else:
        form = RequestForm(instance=n)
    return render(request, 'worksmanager/wm_update1.html', {'form': form})
