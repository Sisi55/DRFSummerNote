from django.contrib import admin
from help.models import Question

class HelpAdmin(admin.ModelAdmin):
    list_display = ('title','created_at')

admin.site.register(Question, HelpAdmin)