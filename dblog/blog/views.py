from blog.models import Article, Tag, Classification, Author
from django.shortcuts import render_to_response
from django.template import RequestContext
            
def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    return render_to_response('index.html', {"blogs": blogs}, context_instance=RequestContext(request))