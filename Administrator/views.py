from django.shortcuts import render,redirect
from Administrator.models import*
from Guest.models import*
from User.models import*
def District(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        districtname=request.POST.get("txt_district")
        tbl_district.objects.create(
            district_name=districtname)
        return render(request,'Administrator/District.html',{"msg":"Data inserted"})
    else:
        return render(request,'Administrator/District.html',{'districtdata':districtdata})
def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    # return redirect('Administrator:District')
    return render(request,'Administrator/District.html',{"msg":"Data Deleted"})
def editdistrict(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt_district")
        editdata.district_name=name
        editdata.save()
        return render(request,'Administrator/District.html',{"msg":"Data updated"})
    else:
        return render(request,'Administrator/District.html',{'editdata':editdata})
def AdminRegistration(request):
    admindata=tbl_admin.objects.all()
    if request.method=="POST":
        adminname=request.POST.get("txt_name")
        adminemail=request.POST.get("txt_email")
        admincontact=request.POST.get("txt_contact")
        adminpassword=request.POST.get("txt_password")
        tbl_admin.objects.create(
            admin_name=adminname,
            admin_email=adminemail,
            admin_contact=admincontact,
            admin_password=adminpassword)
        return render(request,'Administrator/AdminRegistration.html',{"msg":"data inserted"})
    else:
        return render(request,'Administrator/AdminRegistration.html',{'admindata':admindata})
def deladmin(request,aid):
    tbl_admin.objects.get(id=aid).delete()
    return render(request,'Administrator/AdminRegistration.html',{"msg":"data deleted"})
def editadmin(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        editdata.admin_name=name
        editdata.admin_contact=contact
        editdata.admin_email=email
        editdata.admin_password=password
        editdata.save()
        return render(request,'Administrator/AdminRegistration.html',{"msg":"Data updated"})
    else:
        return render(request,'Administrator/AdminRegistration.html',{'editdata':editdata})
def Category(request):
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        categoryname=request.POST.get("txt_category")
        tbl_category.objects.create(
            category_name=categoryname)
        return render(request,'Administrator/Category.html',{"msg":"data inserted"})
    else:
        return render(request,'Administrator/Category.html',{'categorydata':categorydata})
def delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return render(request,'Administrator/Category.html',{"msg":"data deleted"})
def editcategory(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt_category")
        editdata.category_name=name
        editdata.save()
        return render(request,'Administrator/Category.html',{"msg":"Data updated"})
    else:
        return render(request,'Administrator/Category.html',{'editdata':editdata})
def Place(request):
    placedata=tbl_place.objects.all()
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        placename=request.POST.get("txt_place")
        placepin=request.POST.get("txt_pin")
        districtid=tbl_district.objects.get(id=request.POST.get("District"))
        tbl_place.objects.create(
            place_name=placename,
            district=districtid,
            place_pin=placepin
        )
        return render(request,'Administrator/Place.html',{"msg":"Data inserted"})
    else:
        return render(request,'Administrator/Place.html',{'districts':districtdata,'places':placedata})
def delplace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return render(request,'Administrator/Place.html',{"msg":"Data deleted"})
def editplace(request,pid):
    district=tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=pid)
    if request.method=="POST":
        name=request.POST.get("txt_place")
        editdata.place_name=name
        pin=request.POST.get("txt_pin")
        editdata.place_pin=pin
        editdata.district=tbl_district.objects.get(id=request.POST.get("District"))
        editdata.save()
        return render(request,'Administrator/Place.html',{"msg":"Data updated"})
    else:
        return render(request,'Administrator/Place.html',{'editdata':editdata,'district':district})
def SubCategory(request):
    subdata=tbl_subcategory.objects.all()
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        subname=request.POST.get("txt_sub")
        categoryid=tbl_category.objects.get(id=request.POST.get("Category"))
        tbl_subcategory.objects.create(
            sub_name=subname,
            category=categoryid
        )
        return render(request,'Administrator/SubCategory.html',{'msg':"Data inserted"})
    else:
        return render(request,'Administrator/SubCategory.html',{'categories':categorydata,'subcategories':subdata})
def delsub(request,sid):
    tbl_subcategory.objects.get(id=sid).delete()
    return render(request,'Administrator/SubCategory.html',{"msg":"Data deleted"})
def editsub(request,sid):
    category=tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=sid)
    if request.method=="POST":
        name=request.POST.get("txt_sub")
        editdata.sub_name=name
        editdata.category=tbl_category.objects.get(id=request.POST.get("Category"))
        editdata.save()
        return render(request,'Administrator/SubCategory.html',{"msg":"Data updated"})
    else:
        return render(request,'Administrator/SubCategory.html',{'editdata':editdata,'categories':category})
def Product(request):
    return render(request,'Administrator/Product.html')
def Brand(request):
    branddata=tbl_brand.objects.all()
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        categoryid=tbl_category.objects.get(id=request.POST.get("Category"))
        brandname=request.POST.get("txt_brand")
        tbl_brand.objects.create(
            brand_name=brandname,
            category=categoryid
        )
        return render(request,'Administrator/Brand.html',{"msg":"Data inserted"})
    else:
        return render(request,'Administrator/Brand.html',{'branddata':branddata,'categories':categorydata})
def delbrand(request,bid):
    tbl_brand.objects.get(id=bid).delete()
    return render(request,'Administrator/Brand.html',{"msg":"Data deleted"})
def editbrand(request,eid):
    editdata=tbl_brand.objects.get(id=eid)
    category=tbl_category.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_brand")
        editdata.brand_name=name
        editdata.save()
        return render(request,'Administrator/Brand.html',{"msg":"Data updated"})
    else:
        return render(request,'Administrator/Brand.html',{'editdata':editdata,'categories':category})
def Type(request):
    typedata=tbl_type.objects.all()
    if request.method=="POST":
        typename=request.POST.get("txt_type")
        tbl_type.objects.create(
            type_name=typename
        )
        return render(request,'Administrator/Type.html',{"msg":"Data inserted"})
    else:
        return render(request,'Administrator/Type.html',{'typedata':typedata})
def deltype(request,tid):
    tbl_type.objects.get(id=tid).delete()
    return render(request,'Administrator/Type.html',{"msg":"Data deleted"})
def edittype(request,eid):
    editdata=tbl_type.objects.get(id=eid)
    if request.method=="POST":
        name=request.POST.get("txt_type")
        editdata.type_name=name
        editdata.save()
        return render(request,'Administrator/Type.html',{"msg":"Data updated"})
    else:
        return render(request,'Administrator/Type.html',{'editdata':editdata})
def UserList(request):
    userdata=tbl_user.objects.all()
    return render(request,'Administrator/UserList.html',{'userdata':userdata})
def Home(request):
    admin=request.session["aname"]
    return render(request,'Administrator/Home.html',{'name':admin})
def ViewComplaint(request):
    ucdata=tbl_complaint.objects.filter(user__isnull=False)
    scdata=tbl_complaint.objects.filter(scrap__isnull=False)
    return render(request,'Administrator/ViewComplaint.html',{'ucdata':ucdata,'scdata':scdata})
def Reply(request,did):
    cmptdata=tbl_complaint.objects.get(id=did)
    if request.method=="POST":
        reply_data=request.POST.get("txt_reply")
        cmptdata.cmpt_reply=reply_data
        cmptdata.cmpt_status=1
        cmptdata.save()
        return redirect('Administrator:ViewComplaint')
    else:
        return render(request,'Administrator/Reply.html')
def ViewFeedback(request):
    vfdata=tbl_feedback.objects.all()
    return render(request,'Administrator/ViewFeedback.html',{'vfdata':vfdata})
def ScrapcenterList(request):
    scdata=tbl_scrapcenter.objects.all()
    return render(request,'Administrator/ScrapcenterList.html',{'scdata':scdata})
def accept(request,did):
    data=tbl_scrapcenter.objects.get(id=did)
    data.scrapcenter_status=1
    data.save()
    return render(request,'Administrator/ScrapcenterList.html',{"msg":"Verified"})
def reject(request,did):
    data=tbl_scrapcenter.objects.get(id=did)
    data.scrapcenter_status=2
    data.save()
    return render(request,'Administrator/ScrapcenterList.html',{"msg":"Rejected"})
def Model(request):
    modeldata=tbl_model.objects.all()
    category=tbl_category.objects.all()
    branddata=tbl_brand.objects.all()
    if request.method=="POST":
        brandid=tbl_brand.objects.get(id=request.POST.get("brand"))
        modelname=request.POST.get("txt_model")
        tbl_model.objects.create(
            brand=brandid,
            model_name=modelname
        )
        return render(request,'Administrator/Model.html',{"msg":"Data inserted"})
    else:
        return render(request,'Administrator/Model.html',{'modeldata':modeldata,'branddata':branddata,'category':category})
def delmodel(request,did):
    tbl_model.objects.get(id=did).delete()
    return render(request,'Administrator/Model.html',{"msg":"Data deleted"})
def editmodel(request,did):
    editdata=tbl_model.objects.get(id=did)
    editcategory=editdata.brand.category.id
    category=tbl_category.objects.all()
    brand=tbl_brand.objects.filter(category=editcategory)
    if request.method=="POST":
        brandname=tbl_brand.objects.get(id=request.POST.get("brand"))
        name=request.POST.get("txt_model")
        editdata.model_name=name
        editdata.brand=brandname
        editdata.save()
        return render(request,'Administrator/Model.html',{"msg":"Data updated"})
    else:
        return render(request,'Administrator/Model.html',{'editdata':editdata,'category':category,'brand':brand})
def AjaxBrand(request):
    category=request.GET.get("did")
    branddata=tbl_brand.objects.filter(category=category)
    return render(request,"Administrator/AjaxBrand.html",{'brand':branddata})
def ScrapRate(request):
    category=tbl_category.objects.all()
    ratedata=tbl_scraprate.objects.all()
    if request.method=="POST":
        categoryid=tbl_category.objects.get(id=request.POST.get("category"))
        rate=request.POST.get("txt_rate")
        tbl_scraprate.objects.create(
            category=categoryid,
            scraprate_rate=rate
        )
        return render(request,'Administrator/ScrapRate.html',{"msg":"Data inserted"})
    else:
        return render(request,'Administrator/ScrapRate.html',{'ratedata':ratedata,'category':category})
def delrate(request,did):
    tbl_scraprate.objects.get(id=did).delete()
    return render(request,'Administrator/ScrapRate.html',{"msg":"Data deleted"})
def editrate(request,did):
    category=tbl_category.objects.all()
    editdata=tbl_scraprate.objects.get(id=did)
    if request.method=="POST":
        rate=request.POST.get("txt_rate")
        editdata.scraprate_rate=rate
        editdata.category=tbl_category.objects.get(id=request.POST.get("category"))
        editdata.save()
        return render(request,'Administrator/ScrapRate.html',{"msg":"Data updated"})
    else:
        return render(request,'Administrator/ScrapRate.html',{'editdata':editdata,'category':category})