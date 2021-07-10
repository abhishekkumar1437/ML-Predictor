from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseBadRequest, request
from django.contrib.auth.models import User,auth
import datetime
import json,urllib
import pickle 
# Create your views here.

def predictor(request):
    return render(request,'home.html')


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

from django.http import HttpResponse

def breasts(id,radius_mean, texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se,compactness_se ,concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,radius_worst,texture_worst, perimeter_worst, area_worst,smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst):
 
           breast_cancer=pickle.load(open('breast_cancer.pkl','rb'))

           prediction =breast_cancer.predict([[id,radius_mean, texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se,compactness_se ,concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,radius_worst,texture_worst, perimeter_worst, area_worst,smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])
           print(prediction)

           return prediction
              
def breast(request):
    if request.method == "POST":
           id=request.POST['id']
          
           radius_mean= request.POST['radius_mean']
           texture_mean= request.POST['texture_mean']
           perimeter_mean= request.POST['perimeter_mean']
           area_mean= request.POST['area_mean']
           smoothness_mean= request.POST['smoothness_mean']
           compactness_mean= request.POST['compactness_mean']
           concavity_mean= request.POST['concavity_mean']
           concave_points_mean= request.POST['concave_points_mean']
           symmetry_mean= request.POST['symmetry_mean']
           fractal_dimension_mean= request.POST['fractal_dimension_mean']
           radius_se= request.POST['radius_se']
           texture_se= request.POST['texture_se']
           perimeter_se= request.POST['perimeter_se']
           area_se= request.POST['area_se']
           smoothness_se= request.POST['smoothness_se']
           compactness_se= request.POST['compactness_se']
           concavity_se= request.POST['concavity_se']
           concave_points_se= request.POST['concave_points_se']
           symmetry_se= request.POST['symmetry_se']
           fractal_dimension_se= request.POST['fractal_dimension_se']
           radius_worst= request.POST['radius_worst']
           texture_worst= request.POST['texture_worst']
           perimeter_worst= request.POST['perimeter_worst']
           area_worst= request.POST['area_worst']
           smoothness_worst= request.POST['smoothness_worst']
           compactness_worst= request.POST['compactness_worst']
           concavity_worst= request.POST['concavity_worst']
           concave_points_worst= request.POST['concave_points_worst']
           symmetry_worst= request.POST['symmetry_worst']
           fractal_dimension_worst= request.POST['fractal_dimension_worst']
           
        
           results= breasts(id,radius_mean, texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean, concave_points_mean,symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se,compactness_se ,concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,radius_worst,texture_worst, perimeter_worst, area_worst,smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst) 
           print(results)
           return render(request,'breast.html',{'results':results})

    return render(request,'breast.html')      
