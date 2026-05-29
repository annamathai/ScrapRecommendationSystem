from django.shortcuts import render,redirect
from Guest.models import*
from User.models import*
from Scrapcenter.models import*

from django.db.models import Q
from datetime import datetime 

def Home(request):
    return render(request,'Scrapcenter/Home.html')

def MyProfile(request):
    if 'sid' not in request.session:
        return redirect('Guest:Login')
    scrapdata=tbl_scrapcenter.objects.get(id=request.session["sid"])
    return render(request,'Scrapcenter/MyProfile.html',{'scrapdata':scrapdata})

def EditProfile(request):
    if 'sid' not in request.session:
        return redirect('Guest:Login')
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
    if 'sid' not in request.session:
        return redirect('Guest:Login')
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
    if 'sid' not in request.session:
        return redirect('Guest:Login')
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
    if 'sid' not in request.session:
        return redirect('Guest:Login')
    tbl_complaint.objects.get(id=sid).delete()
    return render(request,'Scrapcenter/Complaint.html',{"msg":"Data deleted"})

def editcmpt(request,sid):
    if 'sid' not in request.session:
        return redirect('Guest:Login')
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
    if 'sid' not in request.session:
        return redirect('Guest:Login')
    userdata=tbl_user.objects.all()
    categorydata=tbl_category.objects.all()
    branddata=tbl_brand.objects.all()
    modeldata=tbl_model.objects.all()
    avdata=tbl_addvehicle.objects.filter(vehicle_status=0)
    galdata=tbl_gallery.objects.all()
    return render(request,'Scrapcenter/ViewVehicles.html',{'userdata':userdata,
                                                            'categorydata':categorydata,
                                                            'branddata':branddata,
                                                            'modeldata':modeldata,
                                                            'avdata':avdata})

def Request(request,vid):
    if 'sid' not in request.session:
        return redirect('Guest:Login')
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
    if 'sid' not in request.session:
        return redirect('Guest:Login')
    reqdata=tbl_request.objects.filter(scrapcenter=request.session["sid"])
    return render(request,'Scrapcenter/MyRequest.html',{'reqdata':reqdata})

def ViewRequest(request):
    if 'sid' not in request.session:
        return redirect('Guest:Login')
    reqdata=tbl_sendrequest.objects.filter(scrapcenter=request.session["sid"])
    userdata=tbl_user.objects.all()
    avdata=tbl_addvehicle.objects.all()
    galdata=tbl_gallery.objects.all()
    return render(request,'Scrapcenter/ViewRequest.html',{'reqdata':reqdata,'userdata':userdata,'avdata':avdata})

def RequestReply(request,rid): 
    if 'sid' not in request.session:
        return redirect('Guest:Login')
    data=tbl_sendrequest.objects.get(id=rid)
    if request.method=='POST':
        amount=request.POST.get("txt_amount")
        remark=request.POST.get("txt_remark")
        data.request_amount=amount
        data.request_remark=remark
        data.request_status=1
        data.save()
        return redirect('Scrapcenter:ViewRequest')
    else:
        return render(request,'Scrapcenter/Request.html')

def Logout(request):
    if 'sid' not in request.session:
        return redirect('Guest:Login')
    del request.session['sid']
    return redirect('Guest:Login')

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Scrapcenter/Chat.html",{"user":user})

def ajaxchat(request):
    from_scrapcenter = tbl_scrapcenter.objects.get(id=request.session["aid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),scrapcenter_from=from_scrapcenter,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Scrapcenter/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    scrapcenter = tbl_scrapcenter.objects.get(id=request.session["aid"])
    chat_data = tbl_chat.objects.filter((Q(scrapcenter_from=scrapcenter) | Q(scrapcenter_to=scrapcenter)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Scrapcenter/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(scrapcenter_from=request.session["aid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(scrapcenter_to=request.session["aid"]))).delete()
    return render(request,"Scrapcenter/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})
def Payment(request,id):
    requestdata = tbl_request.objects.get(id=id)
    vehicle = requestdata.vehicle
    if request.method == "POST":
        method = request.POST.get("payment_method")
        upi = request.POST.get("upi")
        card = request.POST.get("card_number")
        cvv = request.POST.get("cvv")
        expiry = request.POST.get("expiry")
        bank = request.POST.get("bank")
        vehicle.vehicle_status = 1
        requestdata.request_status=4
        vehicle.save()
        requestdata.save()
        return render(request,"Scrapcenter/Payment.html",{"msg":"Payment Successful"})
    else:
        return render(request,"Scrapcenter/Payment.html")

def SendPayment(request,id):
    requestdata = tbl_sendrequest.objects.get(id=id)
    vehicle = requestdata.vehicle
    if request.method == "POST":
        method = request.POST.get("payment_method")
        upi = request.POST.get("upi")
        card = request.POST.get("card_number")
        cvv = request.POST.get("cvv")
        expiry = request.POST.get("expiry")
        bank = request.POST.get("bank")
        vehicle.vehicle_status = 1
        requestdata.request_status=4
        requestdata.save()
        vehicle.save()
        return render(request,"Scrapcenter/Payment.html",{"msg":"Payment Successful"})
    else:
        return render(request,"Scrapcenter/Payment.html")