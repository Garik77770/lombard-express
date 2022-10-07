from django.shortcuts import render, redirect
from blog.forms import FormsForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/blog/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    context = {
        'title': 'about page'
    }
    return render(request, 'blog/about.html', context)


def equipment(request):
    contex = {'title': 'about'}
    return render(request, 'blog/equipment.html', contex)


def price_list(request):
    return render(request, 'blog/price_list.html')


def auto_price(request):
    return render(request, 'blog/auto_price.html')


def modal(request):
    return render(request, 'blog/modal.html')


def homepage(request):
    return render(request, "blog/home.html")


def appliances(request):
    return render(request, "blog/appliances.html")


def forms(request):
    if request.method == 'POST':
        form = FormsForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            try:
                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("main:homepage")

    form = FormsForm()
    return render(request, "users/cart.html", {'form': form})
