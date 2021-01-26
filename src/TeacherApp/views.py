from django.shortcuts import render
import requests

# Create your views here.
from django.shortcuts import render
import os
from django.core.files.base import ContentFile
from base64 import b64decode

import cv2
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#
from TeacherApp.models import Subjects, Teacher
# from TeacherApp.serializer import TeacherSerializer, SubjectSerializer
#
from django.core.files.storage import default_storage
import pandas as pd
from TeacherApp.models import Teacher
from PIL import Image
from io import BytesIO


def filterTeacherByLastName(request):
  query = request.GET.get("q", '')
  teachers = Teacher.Objects.filter(TeacherLName__startswith=query)
  return teachers


def homepage(request):
  # username = request.POST.get('username', '')
  # password = request.POST.get('password', '')
  query = request.GET.get('q', '')
  teach = Teacher.objects.filter(TeacherLName__startswith=query)
  # teach = Teacher.objects.all()

  TeacherList = teach

  # if (teacher is not None):
  #
  #   con = teacher
  # else:
  # readCSVFile(request)

  return render(request, 'home.html', {'TeacherList': TeacherList})


#

def readCSVFile(request):
  # upload_file = request.FILES['upload_file']
  # data_read = upload_file.read()

  data = pd.read_csv("Teachers.csv")
  # data = pd.read_csv(data_read)

  for index, row in data.iterrows():
    # print(index,
    #       row['First Name'],
    #       row['Last Name'],
    #       row['Profile picture'],
    #       row["Email Address"],
    #       row["Phone Number"],
    #       row["Room Number"],
    #       row["Subjects taught"])

    import PIL

    folder = "teachers"
    if row['Profile picture'] is None:
      response = requests.get("https://devnote.in/wp-content/uploads/2020/04/devnote.png")
      file = open("sample_image.png", "wb")
      file.write(response.content)
      print(response.content)
      row['Profile picture'] = response.content
    for filename in os.listdir(folder):
      if filename == row['Profile picture']:
        print('filename ', filename)
        default_storage.save(row['Profile picture'], ContentFile(filename))

    teacher = Teacher(TeacherFName=row['First Name'],
                      TeacherLName=row['Last Name'],
                      PhotoFileName=row["Profile picture"],
                      TeacherEmail=row["Email Address"],
                      TeacherPhone=row["Phone Number"],
                      TeacherRoomNo=row["Room Number"],
                      TeacherSubjectsTaught=row["Subjects taught"])

    teacher.save()


# @csrf_exempt
# def load_images_from_folder(folder):
#   images = []
#   for filename in os.listdir(folder):
#     img = cv2.imread(os.path.join(folder, filename))
#     if img is not None:
#       images.append(img)
#   return images


def SaveFile(request):
  file = request.FILES['uploadedFile']
  file_name = default_storage.save(file.name, file)
  return JsonResponse(file_name, safe=False)

# TeacherFName = Teacher.objects.values('TeacherFName')
# TeacherLName = Teacher.objects.values('TeacherLName')
# TeacherEmail = Teacher.objects.values('TeacherEmail')
# TeacherPhone = Teacher.objects.values('TeacherPhone')
# TeacherRoomNo = Teacher.objects.values('TeacherRoomNo')
# PhotoFileName = Teacher.objects.values('PhotoFileName')

# teach = Subjects.objects.all()


# import PIL

# img = cv2.imread(os.path.join(folder, filename))
# print('images ', img)
# print('img', img)
# img = Image.open(img)
# with open(filename) as file:
# return file.read().strip().split(sep)

# if img is not None:
#   # if row['Profile picture'] == img:
#   file = Image.open(BytesIO(img))
#   print('file', file)
#   default_storage.save(file.name, file)

# creating a image object (main image)
# if row['Profile picture'] in
# im1 = Image.open(r"C:\Users\System-Pc\Desktop\flower1.jpg")

# save a image using extension
# im1 = im1.save("geeks.jpg")


# IMG_DIR = 'directory'
# if row['Profile picture'] in os.listdir(IMG_DIR):
#   img_array = cv2.imread(os.path.join(IMG_DIR, row['Profile picture']))
#   img_array = (img_array.flatten())
#   img_array = img_array.reshape(-1, 1).T
#   print(img_array)
#
# # creating a image object (main image)
#  if row['Profile picture'] in
#  im1 = Image.open(r"C:\Users\System-Pc\Desktop\flower1.jpg")
#
#
# # save a image using extension
# im1 = im1.save("geeks.jpg")
#
#
# default_storage.save(im1.name, im1)

# @csrf_exempt
# def subjectApi(request, id=0):
#   if request.method == 'GET':
#     sub = Subjects.objects.all()
#     department_serializer = SubjectSerializer(sub, many=True)
#     return JsonResponse(department_serializer.data, safe=False)
#
#   elif request.method == 'POST':
#     department_data = JSONParser().parse(request)
#     department_serializer = SubjectSerializer(data=department_data)
#     if department_serializer.is_valid():
#       department_serializer.save()
#       return JsonResponse("Added Successfully", safe=False)
#     print("Not Done")
#     return JsonResponse("Failer to Add", safe=False)
#
#   elif request.method == 'PUT':
#     department_data = JSONParser().parse(request)
#     departments = Teacher.objects.get(DepartmentId=department_data['SubjectsId'])
#     department_serializer = SubjectSerializer(departments, data=department_data)
#     if department_serializer.is_valid():
#       department_serializer.save()
#       return JsonResponse("Updated Successfully", safe=False)
#     return JsonResponse("Failer to Update", safe=False)
#
#   elif request.method == 'DELETE':
#     departments = Teacher.objects.get(SubjectsId=id)
#     departments.delete()
#     return JsonResponse("Deleted Successfully", safe=False)
#
#
# @csrf_exempt
# def teacherApi(request, id=0):
#   if request.method == 'GET':
#     departments = Teacher.objects.all()
#     department_serializer = TeacherSerializer(departments, many=True)
#     return JsonResponse(department_serializer.data, safe=False)
#
#   elif request.method == 'POST':
#     department_data = JSONParser().parse(request)
#     department_serializer = TeacherSerializer(data=department_data)
#     if department_serializer.is_valid():
#       department_serializer.save()
#       return JsonResponse("Added Successfully", safe=False)
#     return JsonResponse("Failer to Add", safe=False)
#
#   elif request.method == 'PUT':
#     department_data = JSONParser().parse(request)
#     departments = Teacher.objects.get(TeacherId=department_data['TeacherId'])
#     department_serializer = TeacherSerializer(departments, data=department_data)
#     if department_serializer.is_valid():
#       department_serializer.save()
#       return JsonResponse("Updated Successfully", safe=False)
#     return JsonResponse("Failer to Update", safe=False)
#
#   elif request.method == 'DELETE':
#     departments = Teacher.objects.get(TeacherId=id)
#     departments.delete()
#     return JsonResponse("Deleted Successfully", safe=False)
#
#
