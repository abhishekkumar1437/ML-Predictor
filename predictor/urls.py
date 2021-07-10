from django.urls import path
from . import views

urlpatterns = [

       path('',views.predictor, name='predictor'),
       path('signup',views.signup,name='signup'),
       path('signin',views.signin,name='signin'),
       path("logout",views.logout,name="logout"),
       path("weathers",views.weathers,name='weathers'),
       path('breast',views.breast,name='breast')
]
