from django.shortcuts import render,redirect
from django.db.models import Sum
from .form import (
    QuestionForm,
    QuestionCreate
)

from .models import (
    QuizTopic,
    Quiz,
    Choises
)

# Create your views here.


def instructor(request):
    all_topics = QuizTopic.objects.filter(user =  request.user)


    context = {
        'topics' : all_topics,
        'total_quiz' : len(all_topics),
        'passed':QuizTopic.objects.filter(user =  request.user).aggregate(Sum('passed'))['passed__sum'],
        'failed':QuizTopic.objects.filter(user =  request.user).aggregate(Sum('failed'))['failed__sum'],
        
    }



    return render(request,'instructor-dashboard.html',context)


def createQuiz(request):

    bb = request.session['topic'] 



    login_form = QuestionForm(request.POST,None)
    question = QuestionCreate(request.POST,None)

    if bb is not None:

        jui = QuizTopic.objects.get(id = int(bb))
        qqy = Quiz.objects.filter(topic = jui)

        context = {
        'question' : login_form,
        "topic" : jui.title,
        "quiz":question,
        "all_quizes" : qqy
        }

        if request.method == "POST":
            obj = QuizTopic.objects.create (
                user = request.user,
                title = request.POST.get("question")
            )

            if obj is not None:
                request.session['topic'] = obj.id

                context = {
                    'question' : login_form,
                    "topic" : obj.title,
                    "quiz":question,
                     "all_quizes" : qqy
                }
                return render(request,'createQuiz.html',context)


        return render(request,'createQuiz.html',context)



    else:

        context = {
        'question' : login_form,
        "topic" : jui.title,
        "quiz":question,
        "all_quizes" : []
    }



    
    
        if request.method == "POST":
            obj = QuizTopic.objects.create (
                user = request.user,
                title = request.POST.get("question")
            )

            
            

            if obj is not None:
                request.session['topic'] = obj.id
                qqy = Quiz.objects.filter(topic = obj)

                context = {
                    'question' : login_form,
                    "topic" : obj.title,
                    "quiz":question,
                    "all_quizes" : qqy
                }
                return render(request,'createQuiz.html',context)


        return render(request,'createQuiz.html',context)



def createQestion(request):
    if request.method == "POST":

        bb = request.session['topic'] 

        if bb is not None:
            jui = QuizTopic.objects.get(id = int(bb))

            ss = Quiz.objects.create(
                topic = jui,
                quiz = request.POST.get("quiz")
            )

            if ss is not None:
                return redirect("instructor:createQuiz")



def createQuizChoices(request):
    if request.method == "POST":
        quiz_number = request.POST.get("quiz_number")
        input_ = request.POST.get("input")

        get_q = Quiz.objects.get(id = int(quiz_number))
        choise = Choises.objects.create(
            quiz = get_q,
            choise = input_
        )

        if choise is not None:
            return redirect("instructor:createQuiz")

        return redirect("instructor:createQuiz")

        
        

