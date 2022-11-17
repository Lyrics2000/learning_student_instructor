from django.urls import path
from .views import instructor,createQuiz,createQestion,createQuizChoices,deleteQuiz

app_name = "instructor"

urlpatterns = [
    path("",instructor,name="instructor"),
    path("createQuiz/",createQuiz,name="createQuiz"),
    path("createQestion/",createQestion,name="createQestion"),
    path("createQuizChoices/",createQuizChoices,name="createQuizChoices"),
    path("deleteQuiz/<int:id>/",deleteQuiz,name="deleteQuiz")
]
