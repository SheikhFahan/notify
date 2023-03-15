from django.contrib import admin

# Register your models here.

from .models import Professor, Assignment, Note, QuestionPaper, SubCode

admin.site.register(Professor)
admin.site.register(Assignment)
admin.site.register(Note)
admin.site.register(QuestionPaper)
admin.site.register(SubCode)