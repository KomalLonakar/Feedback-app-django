from django.urls import path
from .views import *

urlpatterns = [
    
    path('',homepageview,name='homepage'),
    path('staff/',staffloginview,name = 'stafflogin'),
    path('validatestaff/',validatestaff,name='validatestaff'),
    path('staffhomepage/',staffhomepageview,name = "staffhomepage"),
    path('logoutstaff/',logoutstaff,name='logoutstaff'),
    path('addquestion/',addquestion,name='addquestion'),
    path('delete/question/<int:question_id>/',deletequestion),
    path('editquestion/',editquestion),
    path('faculty/',facultyview,name='facultypage'),
    path('faculty/delete/<int:faculty_id>/',deletefaculty),
    path('addfaculty/',addfaculty,name = "addfaculty"),
    path('staff/students/',studentslistview,name = "studentslistpage"),
    path('staff/feedback/<int:student_id>/',stafffeedbackview,name = "stafffeedbackpage"),
    # student

    path('student/',studentloginview,name = "studentlogin"),
    path('validatestudent/',validatestudent,name = "validatestudent"),
    path('student/signup/',studentsignupview,name = "studentsignuppage"),
    path('student/register/',registerstudent,name = "registerstudent"),
    path('student/feedback/',studentfeedbackview,name = "studentfeedbackpage"),
    path('student/logout/',studentlogout,name = "studentlogout"),
    path('student/<int:faculty_id>/givefeedback/',givefeedbackview,name = "givefeedbackpage"),
    path('student/savefeedback/',savefeedback,name = "savefeedback"),
    

]
