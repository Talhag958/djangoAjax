from django.shortcuts import render
from .models import Blog
from django.http import JsonResponse

# Create your views here.
def createPost(request):
    blogs = Blog.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
        title = request.POST.get('title')
        description = request.POST.get('description')
        response_data['title'] = title
        response_data['description'] = description

        Blog.objects.create(
            title = title,
            description = description,
            )
        return JsonResponse(response_data) 
    return render(request, 'createBlog.html', {'blogs':blogs})            

