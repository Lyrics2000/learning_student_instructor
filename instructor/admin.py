from django.contrib import admin

from .models import Quiz,Choises,QuizTopic
# Register your models here.


admin.site.register(QuizTopic)
admin.site.register(Quiz)
admin.site.register(Choises)
