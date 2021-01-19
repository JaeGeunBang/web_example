from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
# Create your views here.

### CBV 방식 (Class 방식)
class PostList(ListView):
    model = Post
    #template_name = 'blog/index.html' # 'blog/index.html' 지우고 post_list.html로 수정
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post
    #template_name = 'blog/post_detail.html' #'blog/post_detail.html' 지우고 post_datail.html로 수정

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    if slug =='no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
        }
    )

### FBV 방식 (Function 방식)
#def index(request) :
#    #posts = Post.objects.all() # 데이터베이스에 쿼리를 날려 Post 관련 데이터를 가져온다.
#    posts = Post.objects.all().order_by('-pk')  # 최신 정보부터 가져오기

#    return render(
#        request,
#        'blog/post_list.html',
#        {
#            'posts': posts,
#        }
#    )

#def single_post_page(request, pk) :
#    post = Post.objects.get(pk=pk)

#    return render (
#        request,
#        'blog/post_detail.html',
#        {
#           'post': post,
#        }
#    )