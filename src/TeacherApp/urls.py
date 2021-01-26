from django.conf.urls import url
from TeacherApp import views
from django.conf.urls.static import static
from django.conf import settings

# app_name = 'TeacherApp'
urlpatterns = [
                url(r'', views.homepage),
                url(r'url_filter', views.filterTeacherByLastName),
                url(r'url_filter_subject', views.filterTeacherBySubject),


  # url(r'', views.readCSVFile),
                # url(r'^teacher/$', views.teacherApi),
                # url(r'^teacher/([0-9]+)$', views.teacherApi),
                # url(r'^subject/$', views.subjectApi),

                url(r'^saveFile$', views.SaveFile)

              ]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
