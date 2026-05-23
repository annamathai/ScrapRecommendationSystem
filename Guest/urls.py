from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
     path('Login/',views.Login,name="Login"),
     path('index/',views.index,name="index"),
     path('NewUser/',views.NewUser,name="NewUser"),
     path('AjaxPlace/',views.AjaxPlace,name="AjaxPlace"),
     path('ScrapcenterRegistration/',views.ScrapcenterRegistration,name="ScrapcenterRegistration"),
     path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
     path('otp/',views.otp,name="otp"),
     path('newpass/',views.newpass,name="newpass"),
]