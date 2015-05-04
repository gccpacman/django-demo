#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, Http404, HttpResponseRedirect
#from django.template import RequestContext, loader
#from django.core.urlresolvers import reverse

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """return the last five published questions"""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        )order_by('-pub_date')[:5]
    
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = "result.html"

def vote(request, poll_id):
    p = get_object_or_404(Question, pk = poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': p, 
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
   ## template = loader.get_template('index.html')
    #context = RequestContext(request, {
        #'latest_question_list':latest_question_list,
    #})
    #return render(request, 'index.html', context) 
  ##  return HttpResponse(template.render(context))
    ##output = ', '.join([str((p.question_text, p.pub_date)) for p in latest_question_list])
    ##return HttpResponse(output)

#def detail(request, poll_id):
    ## try:
    ##   question = Question.objects.get(pk=poll_id)
    ## except Question.DoesNotExist:
    ##   raise Http404("Question does not exist")
    #question = get_object_or_404(Question, pk=poll_id)
    #return render(request, 'detail.html', {'question': question})
    ## return HttpResponse("You are looking at poll %s." % poll_id)

#def results(request, poll_id):
    ## return HttpResponse('You are looking at the result of poll %s' % poll_id)
    #question = get_object_or_404(Question, pk = poll_id)
    #return render(request, 'result.html', {'question': question})

#def vote(request, poll_id):
    #p = get_object_or_404(Question, pk = poll_id)
    #try:
        #selected_choice = p.choice_set.get(pk=request.POST['choice'])
    #except (KeyError, Choice.DoesNotExist):
        #return render(request, 'polls/detail.html',{
            #'question': p, 
            #'error_message': "You didn't select a choice.",
        #})
    #else:
        #selected_choice.votes += 1
        #selected_choice.save()
        #return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    ## return HttpResponse('You are voting on poll %s' % poll_id)