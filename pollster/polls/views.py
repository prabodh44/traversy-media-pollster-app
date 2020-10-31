from django.shortcuts import render

from .models import Question, Choice
# Create your views here.

# Get questions and display them
def index(request):
    # shows five questions in descending order of date
    # minus sign(-) signifies descending order
    latest_question_list = Question.objects.order_by('-pub_date')[:5] 
    context = {
        'latest_question_list':latest_question_list,
    }    
    return render(request, 'polls/index.html', context)


# show specific questions and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise http404("Question does not exist")
    return(render(request, "polls/details.html", {'question' : question}))
    

# get question and display results

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question' : question_id})

