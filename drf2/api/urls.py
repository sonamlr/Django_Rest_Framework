from django.urls import path
from . import views
urlpatterns = [
    # function based view url 
    path('studentapi/', views.student_api),
    path('studentapi/<int:pk>', views.student_api),

    # class  based view url
    path('cstudentapi/', views.StudentAPI.as_view()),
    path('cstudentapi/<int:pk>', views.StudentAPI.as_view()),

    #generic view api url
    path('gstudentapi/', views.GPStudentAPI.as_view()),
    path('gstudentapi/<int:pk>', views.PDStudentAPI.as_view()),
]
