from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, TagsNews, Scope
from django.forms import BaseInlineFormSet


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ScopeInline]

@admin.register(TagsNews)
class TagNewsAdmin(admin.ModelAdmin):
    pass