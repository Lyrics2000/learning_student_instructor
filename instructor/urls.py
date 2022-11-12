from django.urls import path
from .views import instructor

app_name = "instructor"

urlpatterns = [
    path("",instructor,name="instructor"),
]
