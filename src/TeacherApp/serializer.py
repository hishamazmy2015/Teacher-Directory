from rest_framework import serializers
from TeacherApp.models import Teacher, Subjects


class SubjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Subjects
    fields = ('SubjectsId',
              'SubjectsName',)


class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher

    fields = ('TeacherId',
              'TeacherFName',
              'TeacherLName',
              'TeacherEmail',
              'TeacherPhone',
              'TeacherRoomNo',
              'TeacherSubjectsTaught',
              'PhotoFileName',
              )
