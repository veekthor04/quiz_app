from django.shortcuts import render, redirect
from .models import Question, Passage, SiteConfiguration

# Create your views here.
def quiz_start(request):
    # This opens start.html 

    config = SiteConfiguration.objects.get()

    context ={
        'config': config
    }

    return render(request, "quiz/start.html", context)


def quiz_question(request):
    # renders the question.html or redirects user to quiz_start function
    
    questions = Question.objects.all()
    passages = Passage.objects.all()
    config = SiteConfiguration.objects.get()

    if config.attempt == 0 and config.retake_status == False:
        # checks if the attempt left is zero and redirects user

        return redirect(quiz_start)

    if config.retake_status == False and config.attempt > 0:
        # reduces the attempt left by one

        config.attempt -= 1
        config.save()

    context = {
        'questions': questions,
        'passages': passages,
        'config': config
    }

    return render(request, "quiz/question.html", context)


def quiz_result(request):
    # calculates the user's score and renders the result.html or redirects user to quiz_start function
    
    correct_count = 0
    question_count = 0
    config = SiteConfiguration.objects.get()
    
    if request.method == 'POST':

        questions = Question.objects.all()

        for question in questions:
        # gets the number of questions available and the number of correct options gotten by the user
            
            if str(question.id) in request.POST:

                if request.POST[str(question.id)] == question.correct_option:
                    # compares options provided with the correct options in the model
                    
                    correct_count+= 1
        
            question_count+= 1

        score = correct_count / question_count * 100

        context ={
            'score': score,
            'config': config
        }  

        return render(request, "quiz/result.html", context)
    
    # redirects user to quiz_start function if a get request is made
    return redirect(quiz_start)