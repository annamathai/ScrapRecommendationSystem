from django.db import models
from Guest.models import*
class tbl_complaint(models.Model):
    cmpt_title=models.CharField(max_length=50)
    cmpt_content=models.CharField(max_length=50)
    cmpt_date=models.DateField(auto_now_add=True)
    cmpt_status=models.IntegerField(default=0)
    cmpt_reply=models.CharField(max_length=50,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    scrap=models.ForeignKey(tbl_scrapcenter,on_delete=models.CASCADE,null=True)
class tbl_feedback(models.Model):
    fb_content=models.CharField(max_length=50)
    fb_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
class tbl_addvehicle(models.Model):
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    model=models.ForeignKey(tbl_model,on_delete=models.CASCADE)
    manufacture_yr=models.IntegerField(null=True)
    fuel_type=models.CharField(max_length=50)
    transmission_type=models.CharField(max_length=50)
    vehicle_mileage=models.IntegerField(null=True)
    vehicle_condition=models.CharField(max_length=50)
    is_rc_available=models.BooleanField()
    insurance_status=models.BooleanField()
    vehicle_description=models.TextField(max_length=50)
    vehicle_status=models.IntegerField(null=True)
    created_date=models.DateField(auto_now_add=True)
class tbl_gallery(models.Model):
    gallery_file=models.FileField(upload_to='Assets/UserDocs/')
    vehicle=models.ForeignKey(tbl_addvehicle,on_delete=models.CASCADE)

class tbl_sendrequest(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_status=models.IntegerField(default=0)
    request_amount=models.CharField(max_length=50,null=True)
    request_remark=models.CharField(max_length=50,null=True)
    vehicle=models.ForeignKey(tbl_addvehicle,on_delete=models.CASCADE)
    scrapcenter=models.ForeignKey(tbl_scrapcenter,on_delete=models.CASCADE)