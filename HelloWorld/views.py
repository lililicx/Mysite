
#coding:utf-8
from django.http import HttpResponse
def index(request):
      # return HttpResponse(u“Hello World!大家好！”)
Return render(request,”index.html”,)

