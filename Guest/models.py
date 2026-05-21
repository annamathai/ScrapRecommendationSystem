from django.db import models
from Administrator.models import*
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_address=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='Assets/UserDocs/')
    user_gender=models.CharField(max_length=50)
    user_dob=models.DateField()
    user_proof=models.FileField(upload_to='Assets/UserDocs/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
class tbl_scrapcenter(models.Model):
    scrapcenter_name=models.CharField(max_length=50)
    scrapcenter_email=models.CharField(max_length=50)
    scrapcenter_contact=models.CharField(max_length=50)
    scrapcenter_address=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    scrapcenter_photo=models.FileField(upload_to='Assets/UserDocs/')
    scrapcenter_proof=models.FileField(upload_to='Assets/UserDocs/')
    scrapcenter_password=models.CharField(max_length=50)
    scrapcenter_status=models.IntegerField(default=0)
