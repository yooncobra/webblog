from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
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
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    params = {'post': post}
    return render(request, 'blog/post_detail.html', params)
'''


class PostDetailView(DetailView):
    def get_object(self, queryset=None):
        # self.kwargs : year, month, day, pk
        # self.kwargs['year']
        # try:
        #     return Post.objects.get(pk=self.kwargs['pk'])
        # except Post.DoesNotExist:
        #     raise Http404

        return get_object_or_404(Post, pk=self.kwargs['pk'])

# post_detail = DetailView.as_view(model=Post)
post_detail = PostDetailView.as_view()


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


@login_required
def post_edit(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


@login_required
def comment_new(request, post_pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            # comment.post = Post.objects.get(pk=post_pk)
            comment.post = get_object_or_404(Post, pk=post_pk)
            comment.save()
            messages.info(request, '새로운 댓글을 등록했습니다.')
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form': form,
    })


@login_required
def comment_edit(request, post_pk, pk):
    # comment = Comment.objects.get(pk=pk)
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {
        'form': form,
        })