from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

### CBV 방식 (Class 방식)
class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/single_post_page.html'

### FBV 방식 (Function 방식)
#def index(request) :
#    #posts = Post.objects.all() # 데이터베이스에 쿼리를 날려 Post 관련 데이터를 가져온다.
#    posts = Post.objects.all().order_by('-pk')  # 최신 정보부터 가져오기

#    return render(
#        request,
#        'blog/index.html',
#        {
#            'posts': posts,
#        }
#    )

#def single_post_page(request, pk) :
#    post = Post.objects.get(pk=pk)

#    return render (
#        request,
#        'blog/single_post_page.html',
#        {
#           'post': post,
#        }
#    )