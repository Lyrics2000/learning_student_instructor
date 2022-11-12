from django.urls import path
from .views import studentDashboard,quiz

app_name = "student"

urlpatterns = [
    path("",studentDashboard,name="studentDashboard"),
    path("quiz/",quiz,name="quiz")
   
]
