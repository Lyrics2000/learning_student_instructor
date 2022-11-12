from django.shortcuts import render

# Create your views here.


def instructor(request):
    return render(request,'instructor-dashboard.html')
