from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_id', 'news_title', 'news_text', 'news_img', 'news_date')
    list_display_links = ('news_id', 'news_title')
    search_fields = ('news_title', 'news_text')
    prepopulated_fields = {"news_slug": ("news_title",)}


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_id', 'blog_title', 'blog_text', 'blog_img', 'blog_date')
    list_display_links = ('blog_id', 'blog_title')
    search_fields = ('blog_title', 'blog_text')
    prepopulated_fields = {"blog_slug": ("blog_title",)}


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('reviews_id', 'reviews_client', 'reviews_text')
    list_display_links = ('reviews_id', 'reviews_client')
    search_fields = ('reviews_client', 'reviews_text')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('services_id', 'services_name', 'services_price', 'services_description')
    list_display_links = ('services_id', 'services_name')
    search_fields = ('services_name', )


class AddressesAdmin(admin.ModelAdmin):
    list_display = ('addresses_id', 'addresses_name')
    list_display_links = ('addresses_name',)
    search_fields = ('addresses_name',)


class VisitAdmin(admin.ModelAdmin):
    list_display = (
        'visit_id',
        'visit_first_name',
        'visit_last_name',
        'visit_patronymic',
        'visit_email',
        'visit_phone',
        'visit_time',
        'visit_is_happened',
        'services_id',
        'addresses_id'
    )
    list_display_links = ('visit_email', 'visit_phone')
    search_fields = ('visit_email', 'visit_phone')


admin.site.register(News, NewsAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Addresses, AddressesAdmin)
admin.site.register(Visit, VisitAdmin)
