from django.shortcuts import render,HttpResponse
from system.views import is_login
# Create your views here.

@is_login
def main_list(request):
    return render(request,'base.html')