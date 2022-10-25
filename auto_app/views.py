from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
import requests
from django.shortcuts import render, redirect


# Create your views here.
from auto_app import models
from auto_app.models import Customer


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def store(request):
    return render(request, 'store.html')

def index(request):
    return render(request, 'index.html')

def aaaAdmin(request):
    return render(request, 'aaaAdmin.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('aaaAdmin')
            elif user.is_worksmanager:
                return redirect('manager_home')
            elif user.is_customer:
                return redirect ('cus_home')

        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

def chatview(request):
    if request.method == 'POST':
        data=request.POST.get('sea')
        print(data)
        msg = Customer.objects.filter(user__icontains=data)
        return render(request, 'message_chat_box.html', {'data': msg})

    data = Customer.objects.filter(user_id=True)
    print(data)
    return render(request, 'message_chat_box.html',{'data': data})







# def statusiot(request)
# URL= "https://api.thingspeak.com/channels/1771037/feeds.json?api_key=E3F84Q8H2YL6TPB7&results=2"
#
# r=requests.get(url=URL)
# print(r.text['feeds'][1]['field1'])


from urllib.request import urlopen
#
import json
import time
#
#
READ_API_KEY = 'E3F84Q8H2YL6TPB7'
CHANNEL_ID = '1771037'
def index1(request):

    while True:
        TS = urlopen(
            "https://api.thingspeak.com/channels/1771037/feeds.json?api_key=E3F84Q8H2YL6TPB7&results=2".format(CHANNEL_ID,
                                                                                                               READ_API_KEY))

        response = TS.read()

        data = json.loads(response.decode('utf-8'))

        print(data)

        print(data["feeds"][1]["field1"])


        a = data["feeds"][1]["field1"]
        b = data['channel']['latitude']
        c = data['channel']['longitude']
        print(a)
        print(b)
        print(c)
        return render(request,'tst.html', {'a': a,'b':b,'c':c})
    # return a,b,c

        # if a=='50' :
        #     print("empty")
        #     break
        #
        # elif a=='30' :
        #     print("partially filled")
        #     break
        #
        # elif a=='10' :
        #     print("fully filled")
        #     break

        # TS.close()

    # def index1(request):
    #
    #     data=requests.get("https://api.thingspeak.com/channels/1771037/feeds.json?api_key=E3F84Q8H2YL6TPB7&results=2".format(CHANNEL_ID,
    #                                                                                                            READ_API_KEY)).json()
    #     # data = json.loads(json.decode('utf-8'))
    #     decoded_json = json.dumps(data)
    #     return render('tst.html', {'results': decoded_json})
    #     # return render(request,'tst.html',{'data':data})



