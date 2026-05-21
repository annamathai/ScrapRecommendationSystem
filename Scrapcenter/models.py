from django.db import models
from User.models import*
class tbl_request(models.Model):
    request_date=models.DateField(auto_now_add=True)
    request_status=models.IntegerField(default=0)
    request_amount=models.CharField(max_length=50,null=True)
    request_remark=models.CharField(max_length=50,null=True)
    vehicle=models.ForeignKey(tbl_addvehicle,on_delete=models.CASCADE)
    scrapcenter=models.ForeignKey(tbl_scrapcenter,on_delete=models.CASCADE)

