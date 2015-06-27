from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from trips.models import Post

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {'post_list':post_list})

def hello_world(request):
    return render(request, "hello_world.html", {'current_time':datetime.now()})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})

# def hello_world(request):
#    output = """
#        <!DOCTYPE html>
#        <html>
#            <head>
#            </head>
#            <body>
#                Hello World! <em style="color:LightSeaGreen,">{current_time}</em>
#            </body>
#        </html>
#     """.format(current_time=datetime.now())
# # vim comment multiply lines --- ctrl+v choose line, <I>, <some content like:#>,
# # <ESC>
#    return HttpResponse(output)
