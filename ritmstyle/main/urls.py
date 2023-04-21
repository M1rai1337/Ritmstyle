from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainIndex.as_view(), name='main'),
    path('news/', views.MainNews.as_view(), name='news'),
    path('news/<slug:news_slug>/', views.MainShowNews.as_view(), name='show_news'),
    path('blog/', views.MainBlog.as_view(), name='blog'),
    path('blog/<slug:blog_slug>/', views.MainShowBlogPost.as_view(), name='show_blog_post'),
    path('thanks/', views.MainThanks.as_view(), name='thanks')
]

