from django.db import models
class tbl_district(models.Model):
    district_name=models.CharField(max_length=60)
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
class tbl_type(models.Model):
    type_name=models.CharField(max_length=50)
class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    place_pin=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_subcategory(models.Model):
    sub_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
class tbl_model(models.Model):
    model_name=models.CharField(max_length=50)
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)
class tbl_scraprate(models.Model):
    scraprate_rate=models.IntegerField(null=True)
    scraprate_date=models.DateField(auto_now_add=True)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)