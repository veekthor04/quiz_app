from django.shortcuts import render
from .models import Question, Passage, SiteConfiguration

# Create your views here.
def quiz_start(request):

    config = SiteConfiguration.objects.get()

    context ={
        'config': config
    }
    return render(request, "quiz/start.html", context)


def quiz_question(request):

    questions = Question.objects.all()
    passages = Passage.objects.all()
    config = SiteConfiguration.objects.get()

    context = {
        'questions': questions,
        'passages': passages,
        'config': config
    }

    return render(request, "quiz/question.html", context)


def quiz_result(request):
    score = 0
    correct_count = 0
    question_count = 0
    config = SiteConfiguration.objects.get()
    
    if request.method == 'POST':

        questions = Question.objects.all()

        for question in questions:

            if str(question.id) in request.POST:
                if request.POST[str(question.id)] == question.correct_option:
                    correct_count+= 1
        
            question_count+= 1

        score = correct_count / question_count * 100

        context ={
            'score': score
        }  

        return render(request, "quiz/result.html", context)

    context ={
        'score': score,
        'config': config
    }

    return render(request, "quiz/start.html", context)