from django.contrib import admin

from .models import Location, Category, Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    empty_value_display = 'Не задано'
    list_display = (
        'title',
        'text',
        'category',
        'created_at',
        'is_published',
        'author',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    inlines = [
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Comment)
