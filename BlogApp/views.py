

from pickle import FALSE
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm

from .models import Category, Post


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
   # ye wala jo jo view me likhoge usme dropdowm menu appear hoga jaisa
   # abhi homeview me toh sirf homeview me dropdowm ayega
   # if you add in some another view it will appera in those view
   # bas yahi wala code copy kr den hai uar view k anme change kr dena bas

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)

        staff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = staff.total_likes()

        liked = False
        if staff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    #fields = '__all__'


def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cats': cats, 'category_post': category_post})


class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add-cat.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = {'title', 'title_tag', 'category', 'body'}


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
