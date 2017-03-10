from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts': posts})
def post_add(request):
    if request.method == 'POST':
        data = request.POST
        title = data['input_title']
        content = data['input_content']
        author = User.object.get(id=1)
        print(title, content, author)

        p = Post(title=title,content=content, author=author)
        p.save()
        return redirect('post_list')
    else:
        return render(request, 'blog/post-add.html')
# Create your views here.

































