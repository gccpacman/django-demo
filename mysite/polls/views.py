from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   # template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_question_list':latest_question_list,
    })
    return render(request, 'index.html', context) 
  #  return HttpResponse(template.render(context))
    #output = ', '.join([str((p.question_text, p.pub_date)) for p in latest_question_list])
    #return HttpResponse(output)

def detail(request, poll_id):
    # try:
    #   question = Question.objects.get(pk=poll_id)
    # except Question.DoesNotExist:
    #   raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=poll_id)
    return render(request, 'detail.html', {'question': question})
    # return HttpResponse("You are looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse('You are looking at the result of poll %s' % poll_id)

def vote(request, poll_id):
    return HttpResponse('You are voting on poll %s' % poll_id)