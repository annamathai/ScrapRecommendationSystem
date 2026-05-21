from django.shortcuts import render,redirect
from Administrator.models import*
from Guest.models import*

def index(request):
    return render(request,"Guest/index.html")

def Login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        appcount=tbl_scrapcenter.objects.filter(scrapcenter_email=email,scrapcenter_password=password).count()
        if usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session["uid"]=userdata.id
            return redirect("User:HomePage")
        elif admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session["aid"]=admindata.id
            request.session["aname"]=admindata.admin_name
            return redirect("Administrator:Home")
        elif appcount>0:
            scrapdata=tbl_scrapcenter.objects.get(scrapcenter_email=email,scrapcenter_password=password)
            request.session["sid"]=scrapdata.id
            return redirect("Scrapcenter:Home")
        else:
            return render(request,"Guest/Login.html",{'msg':"Invalid email or password"})
    else:
        return render(request,'Guest/Login.html')

def NewUser(request):
    userdata=tbl_user.objects.all()
    placedata=tbl_place.objects.all()
    district= tbl_district.objects.all()
    if request.method=="POST":
        userphoto=request.FILES.get("user_photo")
        username=request.POST.get("txt_name")
        usercontact=request.POST.get("txt_contact")
        useremail=request.POST.get("txt_email")
        userpassword=request.POST.get("txt_password")
        useraddress=request.POST.get("txt_address")
        usercpassword=request.POST.get("txt_cpassword")
        userdob=request.POST.get("DOB")
        usergender=request.POST.get("Gender")
        userproof=request.FILES.get("user_proof")
        placeid=tbl_place.objects.get(id=request.POST.get("sel_place"))
        if userpassword==usercpassword :
            tbl_user.objects.create(
                user_name=username,
                user_contact=usercontact,
                user_email=useremail,
                user_password=userpassword,
                user_address=useraddress,
                user_photo=userphoto,
                user_proof=userproof,
                user_gender=usergender,
                user_dob=userdob,
                place=placeid
            )
            return render(request,'Guest/NewUser.html',{"msg":"data inserted"})
        else:
            return render(request,'Guest/NewUser.html',{"msg":"password mismatch"})
    else:
        return render(request,'Guest/NewUser.html',{"district":district})

def AjaxPlace(request):
    district=request.GET.get("did")
    placedata=tbl_place.objects.filter(district=district)
    return render(request,"Guest/AjaxPlace.html",{'Places':placedata})

def ScrapcenterRegistration(request):
    placedata=tbl_place.objects.all()
    district=tbl_district.objects.all()
    scrapdata=tbl_scrapcenter.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        district=request.POST.get("txt_district")
        place=request.POST.get("txt_place")
        photo=request.FILES.get("txt_photo")
        proof=request.FILES.get("txt_proof")
        password=request.POST.get("txt_password")
        placeid=tbl_place.objects.get(id=request.POST.get("place"))
        tbl_scrapcenter.objects.create(
            scrapcenter_name=name,
            scrapcenter_email=email,
            scrapcenter_contact=contact,
            scrapcenter_address=address,
            scrapcenter_photo=photo,
            scrapcenter_proof=proof,
            scrapcenter_password=password,
            place=placeid
        )
        return render(request,'Guest/ScrapcenterRegistration.html',{"msg":"Data inserted"})
    else:
        return render(request,'Guest/ScrapcenterRegistration.html',{'scrapdata':scrapdata,'district':district})