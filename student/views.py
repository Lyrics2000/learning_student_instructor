from django.shortcuts import render

# Create your views here.


def studentDashboard(request):
    return render(request,'student-dashboard.html')

def quiz(request):
    return render(request,'quiz.html')