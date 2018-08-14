from django.shortcuts import render, get_object_or_404, redirect
import json
from django_ajax.decorators import ajax
# Create your views here.
from .models import Post, Category
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import LoginRequiredMixin

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from . import forms
from posts.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.forms import modelformset_factory
import datetime
from django.utils import timezone
class AllPostList(ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 4
# def post_list(request):
#     post_list = Post.objects.all()
#     return render(request, 'posts/post_list.html', {'post_list': post_list})

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'posts/detail.html'


def post_detail(request, pk):
    # post = get_object_or_404(Post, pk=post,status='date')
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    print(comments)

    # comments = post.comments.filter(active=True)
    # print (comments)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
        # Assign the current post to the comment
        new_comment.post = post
        # Save the comment to the database
        new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'posts/detail.html', {'post': post,'comments': comments, 'comment_form': comment_form})

# class PostCreateView(LoginRequiredMixin, CreateView):
#     form_class = forms.TweetModelForm
#     model = Post
#     # fields = '__all__'
#     template_name = 'posts/post_create.html'

@login_required
def new_post(request):
    if request.method == 'POST':
        form = TweetModelForm(request.user, request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:all')
    else:
        form = TweetModelForm(request.user)
    return render(request, 'posts/post_create.html', {'form': form})





@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = TweetModelForm(request.user, request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.date = timezone.now()
            post.save()
            return redirect('posts:detail', pk=post.pk)
    else:
        form = TweetModelForm(request.user, instance=post)

    return render(request, 'posts/post_edit.html', {'form': form})





# class PostEditView(UpdateView):
#     model = Post
#     form_class = forms.TweetModelForm
#     template_name = 'posts/post_edit.html'
class PostDeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy("posts:all")


# def posts(request):
#     all_posts = Post.objects.all()
#     paginator = Paginator(all_posts, posts_NUM_PAGES)
#     posts = paginator.page(1)
#     # likers = Post.get_likers()
#     from_Post = -1
#     if posts:
#         from_Post = posts[0].id

#     return render(request, 'posts/posts.html', {
#         'posts': posts,
#         'from_Post': from_Post,
#         'page': 1
#         # 'likers': likers
#         })


def post(request, pk):
    Post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/Post.html', {'post': post})


