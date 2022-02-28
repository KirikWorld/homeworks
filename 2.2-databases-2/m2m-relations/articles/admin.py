from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, ArticleChapter, Chapter


class ArticleChaptersInlineFormset(BaseInlineFormSet):
    def clean(self):
        tags = []
        for form in self.forms:
            tag = form.cleaned_data.get('main')
            if tag in tags:
                raise ValidationError('Основной раздел может быть только одним')
            tags.append(tag)
        return super().clean()


class ArticleChaptersInline(admin.TabularInline):
    model = ArticleChapter
    extra = 0
    formset = ArticleChaptersInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleChaptersInline, )


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = (ArticleChaptersInline, )
