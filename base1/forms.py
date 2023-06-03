from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Professor, Note, Assignment, QuestionPaper

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1', 'password2']


class ProfessorProfileForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        widgets = {'user' : forms.HiddenInput()}



class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'sub_code', 'ideal_index', 'note', 'prof'] 
        widgets = {
            'prof' : forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class' : 'model-text'}),
            # 'sub_code': forms.Select(attrs={'class' : 'model-select'}),
            'ideal_index': forms.NumberInput(attrs={'class' : 'model-number', 'multiple' : True}),
            'note': forms.FileInput(attrs={'class' : 'model-file'}),
            }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['name', 'sub_code', 'length', 'l_submission', 'assignment'] 
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'model-text'}),
            'length': forms.NumberInput(attrs={'class' : 'model-number'}),
            'assignment': forms.FileInput(attrs={'class' : 'model-file'}),
            'l_submission': forms.DateTimeInput(attrs={'class' : 'model-dateTime'})

            }
class QuestionPaperForm(forms.ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ['name', 'sub_code', 'date', 'questionPaper'] 
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'model-text'}),
            'date': forms.DateInput(attrs={'class' : 'model-dateTime'}),
            'questionPaper': forms.FileInput(attrs={'class' : 'model-file'})
            }
