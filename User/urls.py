from django.urls import path
from User import views
app_name='User'
urlpatterns = [
     path('HomePage/',views.HomePage,name="HomePage"),
     path('EditProfile/',views.EditProfile,name="EditProfile"),
     path('MyProfile/',views.MyProfile,name="MyProfile"),
     path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
     path('Complaint/',views.Complaint,name="Complaint"),
     path('delcmpt/<int:did>/',views.delcmpt,name="delcmpt"),
     path('editcmpt/<int:did>/',views.editcmpt,name="editcmpt"),
     path('Feedback/',views.Feedback,name="Feedback"),
     path('delfb/<int:did>/',views.delfb,name="delfb"),
     path('editfb/<int:did>/',views.editfb,name="editfb"),
     path('AddVehicle/',views.AddVehicle,name="AddVehicle"),
     path('AjaxModel/',views.AjaxModel,name="AjaxModel"),
     path('AjaxBrand/', views.AjaxBrand, name="AjaxBrand"),
     path('delav/<int:did>/',views.delav,name="delav"),
     path('Gallery/<int:vid>/',views.Gallery,name="Gallery"),
     path('delgal/<int:did>/<int:vid>/',views.delgal,name="delgal"),
     path('ViewRequest/',views.ViewRequest,name="ViewRequest"),
     path('accept/<int:id>/', views.accept, name='accept'),
     path('reject/<int:id>/', views.reject, name='reject'),
     path('ViewScrapcenter/<int:vid>/',views.ViewScrapcenter,name="ViewScrapcenter"),
     path('Request/<int:vid>/<int:sid>/',views.Request,name="Request"),
     path('MyRequest/',views.MyRequest,name="MyRequest"),
     path('Priceprediction/',views.Priceprediction,name="Priceprediction"),
     path('Logout/',views.Logout,name="Logout"),
]

