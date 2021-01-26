from django.db import models


# Create your models here.

class Subjects(models.Model):
  SubjectsId = models.AutoField(primary_key=True)
  SubjectsName = models.CharField(max_length=100)

class Teacher(models.Model):
  TeacherId = models.AutoField(primary_key=True)
  TeacherFName = models.CharField(max_length=100)
  TeacherLName = models.CharField(max_length=100)
  TeacherEmail = models.CharField(max_length=100)
  TeacherPhone = models.CharField(max_length=100)
  TeacherRoomNo = models.CharField(max_length=100)
  TeacherSubjectsTaught = models.CharField(max_length=100)
  PhotoFileName = models.ImageField(upload_to='resources',default='21744.jpg')
  # image = models.ImageField(upload_to='images')

  def first_letter(self):
    return self.TeacherLName and self.TeacherLName[0] or ''
