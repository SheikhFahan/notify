from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Professor(models.Model):
    # store information about the uploader i.e professor  
    sex = [
        ('male' , 'male'),
        ('female' , 'female'),
        ('other' , 'other')
    ]
    #id = models.AutoField(primary_key = True, blank  = False , null = False, unique = True)//this field is automatifally added
    user = models.OneToOneField(User,on_delete=models.CASCADE, null = True)  
    profile_pic = models.ImageField(null = False, upload_to='images/', default = 'images/gux+cat.svg')
    fname = models.CharField(null = False , blank = False , max_length=50) 
    lname = models.CharField(null = False , max_length=50) 
    gender = models.CharField(null = False , choices = sex, max_length = 10 )
    email = models.EmailField(null = False, max_length=254)
    description = models.TextField(null = True , blank = True)

    def __str__(self):
        return self.fname
    

# class Student :
#     fname = models.CharField(null = False , blank = False , max_length=50) 
#     lname = models.CharField(null = False , blank = False , max_length=50) 
#     gender = models.CharField(null = False , blank = False, choices = sex, max_length = 10 )
#     email = models.EmailField(null = False, blank = False, max_length=254, True = False)


class SubCode(models.Model):
    sch = (
        ('18th SCHEME','18th SCHEME' ),
        ('16th SCHEME','16th SCHEME'),
        ('21th SCHEME', '21th SCHEME')
    )
    
    sub_code = models.CharField(max_length=10, primary_key = True)
    sub_name = models.CharField(null = True, max_length=50)
    sem = models.PositiveIntegerField(null = True, validators = [MaxValueValidator(8), MinValueValidator(1)])
    scheme = models.CharField(null = True, choices = sch, max_length=50)
    # this is the scheme the subcode is from 
    
    def __str__(self):
        return self.sub_code
    


class Assignment(models.Model):

    name = models.CharField(null = False , blank = False, max_length=50)
    prof= models.ForeignKey(Professor, null = True, on_delete=models.SET_NULL)
    sub_code = models.ForeignKey(SubCode, null = True, on_delete = models.SET_NULL)
    length = models.IntegerField(null = True, blank = True )
    # the length of assignmenet in words
    l_submission = models.DateTimeField( null = True, blank = True, auto_now=False, auto_now_add=False)
    assignment = models.FileField(null = True, upload_to='pdf/assignments/', max_length=100, verbose_name = 'Pdf')

    # last date of submission 


    def __str__(self):
        return self.name
    

class Note(models.Model):
    name = models.CharField(null = False , blank = False, max_length=50)
    prof= models.ForeignKey(Professor, null = False, on_delete=models.CASCADE, blank = False )
    sub_code = models.ForeignKey(SubCode, null = True, on_delete = models.SET_NULL)

    ideal_index = models.IntegerField(null = True, blank = True)
    # says when should this be studied ideally
    upload_date = models.DateField(null = True, blank = True,  auto_now=False, auto_now_add=True)
    note = models.FileField(null = True, upload_to='pdf/notes/', max_length=100, verbose_name = 'Pdf')

    def prof_name(self):
        return str(self.prof)

    def __str__(self):
        return self.name


    
class QuestionPaper(models.Model):
    sub_code = models.ForeignKey(SubCode, null = True, on_delete = models.SET_NULL)
    name = models.CharField(null = True , blank = False, max_length=50)
    date = models.DateField( null = True, blank = False)
    questionPaper = models.FileField(null = True, upload_to='pdf/question_papers/', max_length=100, verbose_name = 'Pdf')

    # date at which the question paper was asked
    
    def __str__(self):
        return self.name
    