from django.shortcuts import render , redirect
from .forms import CreateUserForm, ProfessorProfileForm, NotesForm, AssignmentForm, QuestionPaperForm
from django.contrib.auth import authenticate, logout , login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import Professor, Note, Assignment, QuestionPaper
from .filters import NotesFilter, AssignmentFilter, QuestionPaperFilter
from .decorators import unauthenticated_user , allowed_users
from django.contrib import messages

# used to restict access to pages 

# Create your views here.


def indexPage(request):
    # form = SubCodeForm()
    # if request.method == 'POST':
    #     form = SubCodeForm(request.POST):
    # context = {'form' : form}
    return render(request, 'base1/index.html')

def aboutUs(request):
    return render(request, 'base1/about_us.html')

@unauthenticated_user
def loginPage(request):
    # call this login page and not login cause login is a method
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # this takes the username and password from the login form 
        
        user = authenticate(request, username = username , password = password)
        # this uses the authenticate function to authenticate (from django.contrib.auth)
        if user is not None:
            # if user is there
            login(request, user)
            return redirect('/')
        messages.error(request, "invalid username or password")
    return render(request, 'base1/login.html')
@login_required(login_url = 'login')
def logoutPage(request):
    logout(request)
    return redirect('login')

@allowed_users(allowed_roles = ['admin'])
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form  = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name = 'professors')
            user.groups.add(group
            )
            print(form.errors)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'base1/register.html', context)

@allowed_users(allowed_roles = ['professors'])
@login_required(login_url = 'login')
def profile(request):
    ppk = request.user.professor.id
    professor = Professor.objects.get(id = ppk) 
    form = ProfessorProfileForm(instance  = professor)
    if request.method == 'POST':
        form = ProfessorProfileForm(request.POST, request.FILES, instance = professor)
        if form.is_valid():
            form.save()
            print("this is saving it")
        # else:
        #     return redirect('index')
    context = {'form' : form}
    return render(request, 'base1/profile_page.html', context)

@allowed_users(allowed_roles = ['professors'])
@login_required(login_url = 'login')
def profileView(request):
    prof = request.user.professor
    context = {'prof' : prof}
    return render(request, 'base1/profile.html', context)

#for the uploding of documents
#
@allowed_users(allowed_roles = ['professors'])
@login_required(login_url = 'login')
def uploadNote(request):
    initial_data = {'prof' : request.user.professor} 
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES, initial = initial_data)
        # request.session['prof'] = request.user.professor
        # the above line was useless
        if form.is_valid():
            if (form.cleaned_data['prof'] != request.user.professor):
                 form.add_error('prof', 'You cannot change this value.')
                 print("don't edit via inspect mode")
            else:
              #  form.cleaned_data['prof'] = request.user.professor
                form.save()
                print("successful upload by", request.user.professor)
    else:
        form = NotesForm(initial = initial_data)
        
    context  = {
        'form' : form
    }
    return render(request, 'base1/upload_page.html', context)

@allowed_users(allowed_roles = ['professors'])
@login_required(login_url = 'login')
def uploadAssignment(request):
    form = AssignmentForm(initial = {'prof' : request.user.professor})
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context  = {
        'form' : form
    }
    return render(request, 'base1/upload_page.html', context)

@allowed_users(allowed_roles = ['professors'])
@login_required(login_url = 'login')
def uploadQuestion(request):
    form = QuestionPaperForm()
    if request.method == 'POST':
        form = QuestionPaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context  = {
        'form' : form
    }
    return render(request, 'base1/upload_page.html', context)

#for the retrival of documents
#
def viewNotes(request):
    pdfs = Note.objects.all()
    my_filter = NotesFilter(request.GET, queryset = pdfs)
    pdfs = my_filter.qs
    context = {'pdfs' : pdfs, 'my_filter': my_filter}
    return render(request , 'base1/view_notes.html', context)


def viewAssignments(request):
    pdfs = Assignment.objects.all()
    my_filter = AssignmentFilter(request.GET, queryset = pdfs)
    pdfs = my_filter.qs
    context = {'pdfs' : pdfs, 'my_filter': my_filter}
    return render(request , 'base1/view_assignments.html', context)


def viewQuestions(request):
    pdfs = QuestionPaper.objects.all()
    my_filter = QuestionPaperFilter(request.GET, queryset = pdfs)
    pdfs = my_filter.qs
    context = {'pdfs' : pdfs, 'my_filter': my_filter}
    return render(request , 'base1/view_qp.html', context)

#for the searching of documents
#
def pdfSearch(request, pk):
    notes = Note.objects.filter(sub_code = pk)
    assignments = Assignment.objects.filter(sub_code = pk)
    qPapers =  QuestionPaper.objects.filter(sub_code = pk)

    context = {'notes' : notes, 'assignments' : assignments, 'qPapers'  :qPapers, 'sub_code': pk}

    return render(request, 'base1/search_resources.html', context)


#for deletion of documents
#
def deleteNote(request, pk):
    pdf = Note.objects.get(id = pk)
    if request.method  == 'POST':
        pdf.delete()
        print("delete successful")
        return redirect('viewNotes')
    context = {'pdf' : pdf}
    return render(request , 'base1/delete.html', context)

def deleteAssignment(request, pk):
    pdfs = Assignment.objects.all()
    if request.method  == 'POST':
        pdf.delete()
        print("delete successful")
        return redirect('viewAssignments')
    context = {'pdfs' : pdfs}
    return render(request , 'base1/delete.html', context)

def deleteQuestion  (request, pk):
    pdfs = QuestionPaper.objects.all()
    if request.method  == 'POST':
        pdf.delete()
        print("delete successful")
        return redirect('viewQuestions')
    context = {'pdfs' : pdfs}
    return render(request , 'base1/delete.html', context)

#resources:'(

def resources(request):
    # page for notes assignment and question papers
    return render(request, 'base1/resources.html')
