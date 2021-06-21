from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    question = models.TextField()

class FacultyModel(models.Model):
    name = models.TextField()

class StudentModel(models.Model):
    studentid = models.TextField()
    feedback = models.TextField()
    facultyname = models.TextField()



