from django.shortcuts import redirect, render
from django.views.generic import DetailView
from blog.models import Post
from blog.forms import PostForm


def index(request):
    return render(request, 'blog/index.html')


def post_list(request):
    post_list = Post.objects.all()
    params = {'post_list': post_list}
    return render(request, 'blog/post_list.html', params)
    

'''
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    params = {'post': post}
    return render(request, 'blog/post_detail.html', params)
'''


class PostDetailView(DetailView):
    def get_object(self, queryset=None):
        #self.kwargs : year, month, day, pk
        #self.kwargs['year']
        return Post.objects.get(pk=self.kwargs['pk'])

# post_detail = DetailView.as_view(model=Post)
post_detail = PostDetailView.as_view()


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('blog.views.post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
        })

