from django.db import models

#新建table 命名为Costco， 在数据库里名字实际显示为app_Costco
class Costco(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=32)

#新建table 命名为Costco， 在数据库里名字实际显示为app_Walmart
class Walmart(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=32)