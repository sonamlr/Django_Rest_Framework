from django.urls import path
from . import views
urlpatterns = [
    path('stuInfo/<int:pk>', views.student_detail, name='student_detail'),
    path('stu/', views.student_list, name='student_list'),
    path('stucreate/', views.student_create, name='create'),
    path('studentapi/', views.student_api, name='api')

    

]