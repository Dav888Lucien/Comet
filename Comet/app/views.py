from django.shortcuts import render, HttpResponse
from app import models
# Create your views here.
def homePage(req):
    #搜索框所抓取的搜索词条，存为searchItem
   # print(req.POST)  #查看post方法所传回来的数据

    searchItem = req.POST.get("searchItem")
    print(searchItem)
    q = models.AppCostco.objects.all()

    return render(req, "Homepage.html", {'q': q})


