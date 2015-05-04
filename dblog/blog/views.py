from blog.models import Article, Tag, Classification, Author
from django.shortcuts import render_to_response
from django.template import RequestContext
            
def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    return render_to_response('index.html', {"blogs": blogs}, context_instance=RequestContext(request))


def blog_detail(request):
    if request.method == 'GET':
        id = request.GET.get('id', '');
        try:
            blog = Article.objects.get(id=id)
        except Article.DoesNotExist:
            raise Http404
        return render_to_response("detail.html", {"blog": blog}, context_instance=RequestContext(request))
    else:
        raise Http404