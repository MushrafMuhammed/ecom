from django.shortcuts import render

def commonfun(request) :
    return render(request, 'common_temp/common.html')

# Create your views here.
    