from django.urls import path
from Scrapcenter import views
app_name='Scrapcenter'
urlpatterns = [
    path('Home/',views.Home,name="Home"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('Complaint/',views.Complaint,name="Complaint"),
    path('delcmpt/<int:did>/',views.delcmpt,name="delcmpt"),
    path('editcmpt/<int:sid>/',views.editcmpt,name="editcmpt"),
    path('ViewVehicles/',views.ViewVehicles,name="ViewVehicles"),
    path('Request/<int:vid>/',views.Request,name="Request"),
    path('MyRequest/',views.MyRequest,name="MyRequest"),
    path('ViewRequest/',views.ViewRequest,name="ViewRequest"),
    path('RequestReply/<int:rid>/',views.RequestReply,name="RequestReply"),
]