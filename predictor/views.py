from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User,auth
import datetime
import json,urllib
# Create your views here.

def predictor(request):
    return render(request,'home.html')

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')


def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or password')
            return redirect('signin')
    

    else:
        return render(request,'signin.html')



def signup(request):

    if request.method == 'POST':
        username=request.POST['username']
        first_name= request.POST['first_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken')
                return redirect('signup')
           
            else:    
                user = User.objects.create_user(username=username,name=first_name,email=email,password=password1)
                user.save()
                messages.info(request,'User Created')
                return redirect('signin')
        else:        
            messages.error(request,'Password not matching')
            return redirect('signup')
        return redirect('/')

    else:
      return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')



x = datetime.datetime.now()


def weathers(request):
    
    if request.method == 'POST': 
        city = request.POST['city'] 
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=fc55b08658db9fa4424173680994f3cb').read() 

        list_of_data = json.loads(source) 
        data = {
            
            'city':city,
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + ' °C', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
            
          
        } 
        print(data)
       
    else: 
        data ={} 
    return render(request, "weather.html", data) 