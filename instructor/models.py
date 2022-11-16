from django.db import models
from accounts.models import UserTable

# Create your models here.


class QuizTopic(models.Model):
    user = models.ForeignKey(UserTable,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    attempts = models.PositiveBigIntegerField(default=0)
    passed = models.PositiveBigIntegerField(default=0)
    failed = models.PositiveBigIntegerField(default=0)


    def __str__(self) -> str:
        return self.title



class Quiz(models.Model):
    topic = models.ForeignKey(QuizTopic,on_delete=models.CASCADE,blank=True,null=True)
    quiz = models.CharField(max_length=255)
    



    def __str__(self) -> str:
        return self.quiz
    


class Choises(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    choise = models.CharField(max_length=255)
    answer = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.choise)


    
