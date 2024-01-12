from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setcookie(request):
   res=HttpResponse('cookie is set')
   res.set_cookie('apponix','dhanush')
   return res

def getcookie(request):
   cd=request.COOKIES.get('apponix','nocookie')
   return HttpResponse('the cookie data is '+cd)

def deletecookie(request):
    res=HttpResponse('cookie is deleted')
    res.delete_cookie('apponix')
    return res