from django.urls import path
from Basics import views
urlpatterns = [
    path('Sum/',views.Sum,name="Sum"),
    path('Calculator/',views.Calculator,name="Calculator"),
    path('LargestSmallest/',views.LargestSmallest,name="LargestSmallest")
]
