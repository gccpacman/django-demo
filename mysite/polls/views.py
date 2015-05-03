from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_question_list':latest_question_list,
    })
    return HttpResponse(template.render(context))
    #output = ', '.join([str((p.question_text, p.pub_date)) for p in latest_question_list])
    #return HttpResponse(output)

def detail(request, poll_id):
    return HttpResponse("You are looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse('You are looking at the result of poll %s' % poll_id)

def vote(request, poll_id):
    return HttpResponse('You are voting on poll %s' % poll_id)