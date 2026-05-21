from django.shortcuts import render,redirect
from Guest.models import*
from User.models import*
from Scrapcenter.models import*


def Home(request):
    return render(request,'Scrapcenter/Home.html')

def MyProfile(request):
    scrapdata=tbl_scrapcenter.objects.get(id=request.session["sid"])
    return render(request,'Scrapcenter/MyProfile.html',{'scrapdata':scrapdata})

def EditProfile(request):
    scrapdata=tbl_scrapcenter.objects.get(id=request.session["sid"])
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        scrapdata.scrapcenter_name=name
        scrapdata.scrapcenter_email=email
        scrapdata.scrapcenter_contact=contact
        scrapdata.scrapcenter_address=address
        scrapdata.save()
        return render(request,'Scrapcenter/EditProfile.html',{"msg":"Data updated"})
    else:
        return render(request,'Scrapcenter/EditProfile.html',{'scrapdata':scrapdata})

def ChangePassword(request):
    scrapdata=tbl_scrapcenter.objects.get(id=request.session["sid"])
    if request.method=="POST":
        opassword=request.POST.get("txt_opassword")
        npassword=request.POST.get("txt_npassword")
        cpassword=request.POST.get("txt_cpassword")
        if opassword==scrapdata.scrapcenter_password:
            if npassword==cpassword:
                scrapdata.scrapcenter_password=cpassword
                scrapdata.save()
                return render(request,'Scrapcenter/ChangePassword.html',{"msg":"Password Changed"})
            else:
                return render(request,'Scrapcenter/ChangePassword.html',{"msg":"Password Mismatch"})
        else:
            return render(request,'Scrapcenter/ChangePassword.html',{"msg":"Password Incorrect"})
    return render(request,'Scrapcenter/ChangePassword.html',{'scrapdata':scrapdata})

def Complaint(request):
    scrapid=tbl_scrapcenter.objects.get(id=request.session["sid"])
    cmptdata=tbl_complaint.objects.filter(scrap=scrapid)
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        tbl_complaint.objects.create(
            cmpt_title=title,
            cmpt_content=content,
            scrap=scrapid
        )
        return render(request,'Scrapcenter/Complaint.html',{"msg":"Data inserted"})
    else:
        return render(request,'Scrapcenter/Complaint.html',{'cmptdata':cmptdata})

def delcmpt(request,sid):
    tbl_complaint.objects.get(id=sid).delete()
    return render(request,'Scrapcenter/Complaint.html',{"msg":"Data deleted"})

def editcmpt(request,sid):
    editdata=tbl_complaint.objects.get(id=sid)
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        editdata.cmpt_title=title
        editdata.cmpt_content=content
        editdata.save()
        return render(request,'Scrapcenter/Complaint.html',{"msg":"Data updated"})
    else:
        return render(request,'Scrapcenter/Complaint.html',{'editdata':editdata})

def ViewVehicles(request):
    userdata=tbl_user.objects.all()
    categorydata=tbl_category.objects.all()
    branddata=tbl_brand.objects.all()
    modeldata=tbl_model.objects.all()
    avdata=tbl_addvehicle.objects.all()
    galdata=tbl_gallery.objects.all()
    return render(request,'Scrapcenter/ViewVehicles.html',{'userdata':userdata,
                                                            'categorydata':categorydata,
                                                            'branddata':branddata,
                                                            'modeldata':modeldata,
                                                            'avdata':avdata})

def Request(request,vid):
    reqdata=tbl_request.objects.all()
    vehicleid=tbl_addvehicle.objects.get(id=vid)
    scrapid=tbl_scrapcenter.objects.get(id=request.session["sid"])
    if request.method=="POST":
        amount=request.POST.get("txt_amount")
        remark=request.POST.get("txt_remark")
        tbl_request.objects.create(
            request_amount=amount,
            request_remark=remark,
            scrapcenter=scrapid,
            vehicle=vehicleid
        )
        return render(request,'Scrapcenter/Request.html',{"msg":"Data inserted",'vid':vid})
    else:
        return render(request,'Scrapcenter/Request.html',{'reqdata':reqdata,'vid':vid})

def MyRequest(request):
    reqdata=tbl_request.objects.filter(scrapcenter=request.session["sid"])
    return render(request,'Scrapcenter/MyRequest.html',{'reqdata':reqdata})

def ViewRequest(request):
    reqdata=tbl_sendrequest.objects.filter(scrapcenter=request.session["sid"])
    userdata=tbl_user.objects.all()
    avdata=tbl_addvehicle.objects.all()
    galdata=tbl_gallery.objects.all()
    return render(request,'Scrapcenter/ViewRequest.html',{'reqdata':reqdata,'userdata':userdata,'avdata':avdata})

def RequestReply(request,rid): 
    data=tbl_sendrequest.objects.get(id=rid)
    if request.method=='POST':
        amount=request.POST.get("txt_amount")
        remark=request.POST.get("txt_remark")
        data.request_amount=amount
        data.request_remark=remark
        data.save()
        return redirect('Scrapcenter:ViewRequest')
    else:
        return render(request,'Scrapcenter/Request.html')