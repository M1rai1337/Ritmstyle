from .utils import *
from .models import *
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View
from django.http import HttpResponseNotFound


def page_not_found(request, exception):
    return render(request, 'main/not_found.html', {'title': '404'})


class PageNotFound(Mixin, View):
    template_name = 'main/not_found.html'
    context = {
        'title': 'Error'
    }
    def get(self, request):
        return self.mixin_get(request, **self.context)

    def post(self, request):
        return self.mixin_post(request, **self.context)


class MainIndex(Mixin, View):
    template_name = 'main/index.html'
    context = {
        'title': 'RitmStyle',
        'services': Services.objects.all(),
        'reviews': Reviews.objects.all()
    }

    def get(self, request):
        return self.mixin_get(request, **self.context)

    def post(self, request):
        return self.mixin_post(request, **self.context)


class MainNews(Mixin, View):
    template_name = 'main/news.html'
    context = {
        'title': 'Новости',
        'news_from_db': News.objects.all().order_by('-news_date')
    }

    def get(self, request):
        return self.mixin_get(request, **self.context)

    def post(self, request):
        return self.mixin_post(request, **self.context)


class MainShowNews(Mixin, View):
    template_name = 'main/show_news.html'

    def get(self, request, news_slug):
        some_news = get_object_or_404(News, news_slug=news_slug)
        return self.mixin_get(
            request,
            title=some_news,
            some_news=some_news,
        )

    def post(self, request, news_slug):
        some_news = get_object_or_404(News, news_slug=news_slug)
        return self.mixin_post(
            request,
            title=some_news,
            some_news=some_news,
        )


class MainBlog(Mixin, View):
    template_name = 'main/blog.html'
    context = {
        'title': 'Блог',
        'posts': Blog.objects.all().order_by('-blog_date'),
    }

    def get(self, request):
        return self.mixin_get(request, **self.context)

    def post(self, request):
        return self.mixin_post(request, **self.context)


class MainShowBlogPost(Mixin, View):
    template_name = 'main/show_post.html'

    def get(self, request, blog_slug):
        blog_post = get_object_or_404(Blog, blog_slug=blog_slug)
        return self.mixin_get(
            request,
            title=blog_post,
            blog_post=blog_post,
        )

    def post(self, request, blog_slug):
        blog_post = get_object_or_404(Blog, blog_slug=blog_slug)
        return self.mixin_post(
            request,
            title=blog_post,
            blog_post=blog_post,
        )


class MainThanks(Mixin, View):
    template_name = 'main/thanks.html'
    context = {
        'title': 'Спасибо',
    }

    def get(self, request):
        return self.mixin_get(request, *self.context)

    def post(self, request):
        return self.mixin_post(request, *self.context)

