from django.contrib import admin
from .models import Article, Comment
from django_summernote.admin import SummernoteModelAdmin

# Credits - code is adapted from the CI LMS Django
# blog lessons and is fully accredited & acknowledged


@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    """
    Register the Article model in the Administration area
    with all appropriate fields included
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Register the Comment model in the Administration area
    with all appropriate fields included and an approve method
    """
    list_display = ('name', 'body', 'article', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

# Register your models here.
