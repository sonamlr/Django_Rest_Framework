from django.urls import path, include
from . import views
# viewsets
from rest_framework.routers import DefaultRouter
#Router object Created
router = DefaultRouter()
#Registed class with router
router.register('studentrouterapi', views.StudentViewSet, basename='student')
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
    
    path('ggstudentapi/', views.StudentListCreate.as_view()),
    path('ggstudentapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),

    # router include
    path('', include(router.urls))


]
