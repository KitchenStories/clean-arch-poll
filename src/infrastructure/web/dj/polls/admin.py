from django.contrib import admin

from infrastructure.web.dj.polls import models


class QuestionAdmin(admin.ModelAdmin):
    fields = ['name', 'text']


class ChoiceAdmin(admin.ModelAdmin):
    fields = ['name', 'text', 'votes', 'question']


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice, ChoiceAdmin)
