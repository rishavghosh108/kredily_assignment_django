"""
URL configuration for kredily_assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import ManageEmployee,EmployeeAttendance,Home,employee_details,department_report

urlpatterns = [
    path('admin/', admin.site.urls),   #### this end point is previously given.

    path('employees/',ManageEmployee.as_view(),name="add_employee"),   ####  this end point is a rest api. this api is use to add a new employee using post method and get the list of the employees using get method.
    path('attendance/',EmployeeAttendance.as_view(),name="attendance"),  #### this end point is a rest api. this api is use to mark attendance using post method.

    path('',Home, name='home'),  #### this end point is a MVT base route. on this end point gives to the ui base design to perform add employee, mark attendance , to go employee page to get employee details , to go department-report page to get departmet details.
    path('employee/', employee_details, name='employee_details'),  #### this end point is a MVT base route. it show you the details of any employee.
    path('department-report/', department_report, name='department-report')   #### this end point is a MVT base route. it show you the details of all department.
]
