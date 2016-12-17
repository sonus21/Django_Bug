from django.contrib.admin import ModelAdmin
from django.contrib.admin import TabularInline
from django.contrib.admin import register
from buggy.models import Explanation, Question


class ExplanationInline(TabularInline):
    model = Explanation
    extra = 1

@register(Question)
class QuestionAdmin(ModelAdmin):
    inlines = [
        ExplanationInline,
    ]
