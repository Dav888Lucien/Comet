from django.db import models
#新建table 命名为Costco， 在数据库里名字实际显示为app_Costco
class AppCostco(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'app_costco'


class AppWalmart(models.Model):
    id = models.BigAutoField(primary_key=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'app_walmart'




