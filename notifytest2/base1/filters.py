import django_filters

from .models import Note, Assignment, QuestionPaper

class NotesFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['note']


class AssignmentFilter(django_filters.FilterSet):
    class Meta:
        model = Assignment
        fields = '__all__'
        exclude = ['assignment']

class QuestionPaperFilter(django_filters.FilterSet):
    class Meta:
        model = QuestionPaper
        fields = '__all__'
        exclude = ['questionPaper']