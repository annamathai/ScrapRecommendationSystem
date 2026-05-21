from django.shortcuts import render,redirect
from Guest.models import*
from User.models import*
from Administrator.models import*
from Scrapcenter.models import* 

#ml import
import os
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib

MODEL_PATH = os.path.join("Assets", "Model", "vehicle_weight_model.pkl")
loaded_pipeline = joblib.load(MODEL_PATH)

def Priceprediction(request):
    brandadata=tbl_brand.objects.all()
    typedata=tbl_type.objects.all()
    if 'uid' in request.session:
        if request.method=='POST':
            brand=request.POST.get('SelectBrand')
            brand=tbl_brand.objects.get(id=brand)
            brand=brand.brand_name

            typed=request.POST.get('SelectType')
            typed=tbl_type.objects.get(id=typed)
            typed=typed.type_name

            model=request.POST.get('SelectModel')
            model=tbl_vehiclemodels.objects.get(id=model)
            model=model.model_name

            fuel=request.POST.get('SelectFuelType')

            sample = pd.DataFrame([{
                "vehicle_type": typed,
                "brand": brand,
                "vehicle_name": model,
                "fuel_type": fuel
            }])
            predicted_weight = loaded_pipeline.predict(sample)
            weight = round(float(predicted_weight[0]), 2)
            price=weight*30
            return render(request, 'User/Priceprediction.html',{'bname':brand,'mname':model,'predicted_weight':weight,'price':price,'brand':brandadata,'type':typedata})
        else:
            return render(request, 'User/Priceprediction.html',{'brand':brandadata,'type':typedata})
    else:
        return redirect("Guest:Login")


def HomePage(request):
    return render(request,'User/HomePage.html')
def EditProfile(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        userdata.user_name=name
        userdata.user_email=email
        userdata.user_contact=contact
        userdata.user_address=address
        userdata.save()
        return render(request,'User/EditProfile.html',{"msg":"Data updated"})
    else:
        return render(request,'User/EditProfile.html',{'userdata':userdata})
def MyProfile(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    return render(request,'User/MyProfile.html',{'userdata':userdata})
def ChangePassword(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        opassword=request.POST.get("txt_opassword")
        npassword=request.POST.get("txt_npassword")
        cpassword=request.POST.get("txt_cpassword")
        if opassword==userdata.user_password:
            if npassword==cpassword:
                userdata.user_password=cpassword
                userdata.save()
                return render(request,'User/ChangePassword.html',{"msg":"Password Changed"})
            else:
                return render(request,'User/ChangePassword.html',{"msg":"Password Mismatch"})
        else:
            return render(request,'User/ChangePassword.html',{"msg":"Password Incorrect"})
    return render(request,'User/ChangePassword.html',{'userdata':userdata})
def Complaint(request):
    userid=tbl_user.objects.get(id=request.session["uid"])
    cmptdata=tbl_complaint.objects.filter(user=userid)
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        tbl_complaint.objects.create(
            cmpt_title=title,
            cmpt_content=content,
            user=userid
        )
        return render(request,'User/Complaint.html',{"msg":"Data inserted"})
    else:
        return render(request,'User/Complaint.html',{'cmptdata':cmptdata})
def delcmpt(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request,'User/Complaint.html',{"msg":"Data deleted"})
def editcmpt(request,did):
    editdata=tbl_complaint.objects.get(id=did)
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        editdata.cmpt_title=title
        editdata.cmpt_content=content
        editdata.save()
        return render(request,'User/Complaint.html',{"msg":"Data updated"})
    else:
        return render(request,'User/Complaint.html',{'editdata':editdata})
def Feedback(request):
    fbdata=tbl_feedback.objects.all()
    userid=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        content=request.POST.get("txt_feedback")
        tbl_feedback.objects.create(
        fb_content=content,
        user=userid
        )
        return render(request,'User/Feedback.html',{"msg":"Data inserted"})
    else:
        return render(request,'User/Feedback.html',{'fbdata':fbdata})
def delfb(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return render(request,'User/Feedback.html',{"msg":"Data deleted"})
def editfb(request,did):
    editdata=tbl_feedback.objects.get(id=did)
    if request.method=="POST":
        content=request.POST.get("txt_feedback")
        editdata.fb_content=content
        editdata.save()
        return render(request,'User/Feedback.html',{"msg":"Data updated"})
    else:
        return render(request,'User/Feedback.html',{'editdata':editdata})
def AddVehicle(request):
    avdata=tbl_addvehicle.objects.all()
    categorydata=tbl_category.objects.all()
    userid=tbl_user.objects.get(id=request.session["uid"])
    branddata=tbl_brand.objects.all()
    modeldata=tbl_model.objects.all()
    if request.method=="POST":
        transmission=request.POST.get("txt_transmission")
        mileage=request.POST.get("txt_mileage")
        fuel=request.POST.get("txt_fuel")
        condition=request.POST.get("txt_condition")
        availability=request.POST.get("availability")
        insurance=request.POST.get("Insurance")
        description=request.POST.get("txt_description")
        yr=request.POST.get("txt_year")
        modelid=tbl_model.objects.get(id=request.POST.get("model"))
        tbl_addvehicle.objects.create(
            transmission_type=transmission,
            vehicle_mileage=mileage,
            fuel_type=fuel,
            vehicle_condition=condition,
            is_rc_available=availability,
            insurance_status=insurance,
            vehicle_description=description,
            manufacture_yr=yr,
            user=userid,
            model=modelid
        )
        return render(request,'User/AddVehicle.html',{"msg":"Data inserted"})
    else:
        return render(request,'User/AddVehicle.html',{'category':categorydata,'avdata':avdata,})
def AjaxModel(request):
    brand=request.GET.get("did")
    modeldata=tbl_model.objects.filter(brand=brand)
    return render(request,"User/AjaxModel.html",{'model':modeldata})
def AjaxBrand(request):
    category=request.GET.get("did")
    branddata=tbl_brand.objects.filter(category=category)
    return render(request,'User/AjaxBrand.html',{'brand': branddata})
def delav(request,did):
    tbl_addvehicle.objects.get(id=did).delete()
    return render(request,'User/AddVehicle.html',{"msg":"Data deleted"})
def Gallery(request,vid):
    vehicleid=tbl_addvehicle.objects.get(id=vid)
    galdata=tbl_gallery.objects.all()
    if request.method=="POST":
        image=request.FILES.get("txt_image")
        tbl_gallery.objects.create(
            gallery_file=image,
            vehicle=vehicleid
        )
        return render(request,'User/Gallery.html',{"msg":"Data inserted",'vid':vid})
    else:
        return render(request,'User/Gallery.html',{'galdata':galdata,'vid':vid})
def delgal(request,did,vid):
    tbl_gallery.objects.get(id=did).delete()
    return render(request,'User/Gallery.html',{"msg":"Data deleted",'vid':vid})
def ViewRequest(request):
    avdata=tbl_addvehicle.objects.all()
    reqdata=tbl_request.objects.all()
    scrapdata=tbl_scrapcenter.objects.all()
    galdata=tbl_gallery.objects.all()
    return render(request,'User/ViewRequest.html',{'avdata':avdata,'reqdata':reqdata,'scrapdata':scrapdata})
def reject(request,id):
    data = tbl_request.objects.get(id=id)
    data.request_status = 2
    data.save()
    return redirect("User:ViewRequest")
def accept(request,id):
    data = tbl_request.objects.get(id=id)
    data.request_status = 1
    data.save()
    return redirect("User:ViewRequest")
def ViewScrapcenter(request,vid):
    scrapdata=tbl_scrapcenter.objects.filter(scrapcenter_status=1)
    return render(request,'User/ViewScrapcenter.html',{'scrapdata':scrapdata,'vid':vid})

def Request(request,vid,sid):
    reqdata=tbl_sendrequest.objects.filter(vehicle__user=request.session['uid'])
    vehicleid=tbl_addvehicle.objects.get(id=vid)
    scrapid=tbl_scrapcenter.objects.get(id=sid)
    tbl_sendrequest.objects.create(
        scrapcenter=scrapid,
        vehicle=vehicleid
    )
    return redirect("User:MyRequest")

def MyRequest(request):
    avdata=tbl_addvehicle.objects.all()
    reqdata=tbl_sendrequest.objects.filter(vehicle__user=request.session['uid'])
    scrapdata=tbl_scrapcenter.objects.all()
    galdata=tbl_gallery.objects.all()
    return render(request,'User/MyRequest.html',{'avdata':avdata,'reqdata':reqdata,'scrapdata':scrapdata})

def ViewRequest(request): 
    reqdata=tbl_request.objects.filter(vehicle__user=request.session['uid'])
    return render(request,'User/ViewRequest.html',{'reqdata':reqdata})