from django.contrib import messages
from .models import *
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def homepageview(request):
    return redirect('studentlogin')

def staffloginview(request):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            questions = QuestionModel.objects.all()
            context = {'questions':questions}
            return render(request, 'feedbackapp/staffhomepage.html',context)
            
    return render(request, 'feedbackapp/stafflogin.html')

def validatestaff(request):
    username = request.POST['username']
    password = request.POST['password']
    user =authenticate(username = username,password = password)
    if user is not None:
        if user.is_superuser:
            login(request,user)
            return redirect('staffhomepage')
    messages.add_message(request, messages.ERROR, 'invalid credentials')
    return redirect(request.META["HTTP_REFERER"])

def staffhomepageview(request):
    
    if request.user.is_superuser:
        if request.user.is_authenticated:
             questions = QuestionModel.objects.all()
             context = {'questions':questions}
             return render(request, 'feedbackapp/staffhomepage.html',context)
    return redirect('stafflogin')
def logoutstaff(request):
    logout(request)
    return redirect('stafflogin')

def addquestion(request):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            question = request.POST['question']
            QuestionModel(question = question).save()
            return redirect(request.META["HTTP_REFERER"])

def deletequestion(request,question_id):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            question = QuestionModel(id = question_id)
            question.delete()
            return redirect(request.META["HTTP_REFERER"])
def editquestion(request):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            question = QuestionModel(id = request.POST["questionId"])
            question.question = request.POST["question"]
            question.save()
            return redirect(request.META["HTTP_REFERER"])
  
def facultyview(request):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            context = {'faculties' : FacultyModel.objects.all()}
            return render(request,"feedbackapp/faculty.html",context)

def addfaculty(request):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            faculty = request.POST["faculty"]
            FacultyModel(name = faculty).save()
            return redirect(request.META["HTTP_REFERER"])

def deletefaculty(request,faculty_id):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            FacultyModel.objects.filter(id = faculty_id).delete()
            return redirect(request.META["HTTP_REFERER"])

def studentslistview(request):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            for user in User.objects.all():
                print(user)
            students = [student for student in User.objects.all() if not student.is_superuser]

            context = {"students": students}
            return render(request,"feedbackapp/students.html",context)
import json
def stafffeedbackview(request,student_id):
    if request.user.is_superuser:
        if request.user.is_authenticated:
            feedbacks = [] 
            for feedback in  StudentModel.objects.filter(studentid = student_id):
                feedbacks.append(feedback)
            context = {"feedbacks": feedbacks}
            return render(request,"feedbackapp/stafffeedback.html",context)


# student

def studentloginview(request):
    return render(request,"feedbackapp/studentlogin.html")

def validatestudent(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username,password = password)

    if user is not None:

        login(request,user)

        return redirect("studentfeedbackpage")
    else:
        messages.add_message(request,messages.ERROR,"invalid credentials")
        return redirect(request.META["HTTP_REFERER"])
def studentsignupview(request):
    return render(request,"feedbackapp/studentsignup.html")
def registerstudent(request):
    username = request.POST["username"]
    password = request.POST["password"]
    repassword = request.POST["repassword"]
    if not User.objects.filter(username = username).exists():
        if password==repassword:
            User.objects.create_user(username = username,password=password).save()
            messages.add_message(request, messages.SUCCESS, 'user succesfully created')
        else:
            messages.add_message(request, messages.ERROR, 'passwords didnt match')
            return redirect(request.META["HTTP_REFERER"])
    else:
        messages.add_message(request, messages.ERROR, 'user already exists')
        return redirect(request.META["HTTP_REFERER"])
    # create user

    
    return redirect(request.META["HTTP_REFERER"])

def studentfeedbackview(request):
    if request.user.is_authenticated:
        context = {'faculties' : FacultyModel.objects.all()}
        return render(request,"feedbackapp/feedback.html",context)
    else:
        return redirect('studentlogin')

def studentlogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('homepage')
    return redirect('homepage')

def givefeedbackview(request,faculty_id):
    if request.user.is_authenticated:
        faculty =FacultyModel.objects.filter(id=faculty_id)[0]

        questions = QuestionModel.objects.all()
        context = {'faculty' : faculty,'questions' : questions}
        return render(request,"feedbackapp/givefeedback.html",context)

def savefeedback(request):
    if request.user.is_authenticated:
        d = dict()
        facultyid = request.POST.get('faculty')
        faculty = FacultyModel.objects.filter(id = facultyid)[0]
        print(faculty.name)
        for question in QuestionModel.objects.all():
            d[question.question] = request.POST[str(question.id)+'flexRadioDefault']
        if StudentModel.objects.filter(studentid = request.user.id,facultyname = faculty.name).exists():
            messages.add_message(request, messages.ERROR,'duplicate feedbacks not allowed')
            return redirect('studentfeedbackpage')
        StudentModel(studentid = request.user.id,feedback = str(d),facultyname = faculty.name).save()
        messages.add_message(request, messages.SUCCESS,'feedback succesfully saved')
        return redirect('studentfeedbackpage')
