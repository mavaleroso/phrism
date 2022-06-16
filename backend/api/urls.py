from django.urls import path
from api import views

urlpatterns = [
     path('position_list', views.getPosition),
     path('division_list', views.getDivision),
     path('section_list', views.getSection),
     path('employee_detail', views.employeeDetail),
]
