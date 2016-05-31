from django.shortcuts import redirect, render
from django.views.generic import DetailView
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm


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


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if forms.is_valid():
            post = form.save()
            return redirect('blog.views.post_detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
        })


def comment_new(request, post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('blog.views.post_detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form': form,
        })


def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog.views.post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {
        'form': form,
        })
