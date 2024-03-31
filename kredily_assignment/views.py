import datetime
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.http import HttpResponse
from .serializer import EmployeeSerializer,AttendanceSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Count


'''ManageEmployee class is linked with /employees/ route. this class have two method one is get and another one is post.
get method give the list of all employees. it don't take any argument as input.
post method takes name,designation,department and date of joining arguments as input. 
if the employee is already exist it return a error message ({"error":"user already exist !!!"}),
 otherwise it store the data into database and gives a successful message with the instance the the employee.'''

class ManageEmployee(APIView):
    def get(self,request):
        data=Employee.objects.all()
        sd=EmployeeSerializer(data,many=True)
        return Response({'successful':sd.data})
    
    def post(self,request):
        sd=EmployeeSerializer(data=request.data)
        if sd.is_valid() is False:
            return Response(sd.errors, status=400)
        
        employee_data=sd.validated_data

        employee_data['name']=employee_data['name'].lower()
        employee_data['designation']=employee_data['designation'].lower()
        employee_data['department']=employee_data['department'].lower()

        check=Employee.objects.filter(name=employee_data['name'],designation=employee_data.get('designation'),department=employee_data.get('department'),doj=employee_data.get('doj')).first()
        if  check is not None:
            return Response({"error":"user already exist !!!"}, status=404)
        
        sd.save()
        return Response({'successful': sd.data}, status=201)
            
''' EmployeeAtterndance class is linked with /attendance/ route. this class have one method named post.
post method takes employee id, attendance status and date of attendance . if the employee does not exist with the employee id it will return an error message like "user": ["Invalid pk \"3\" - object does not exist."] .
if the entry already recorded then it will return an error message like {"error":"this entry already recorded !!!"} otherwise attendance will be recorded. '''

class EmployeeAttendance(APIView):
    # def get(self, request,employee_id):                    this alternative api to get employee attendance
    #     try:
    #         employee = Employee.objects.get(id=employee_id)
    #     except Employee.DoesNotExist:
    #         return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
    #     attendance_records = Attendance.objects.filter(user=employee)
    #     serializer = AttendanceSerializer(attendance_records, many=True)
        
    #     return Response(serializer.data)
    
    def post(self,request):
        sd=AttendanceSerializer(data=request.data)
        if sd.is_valid():
            data=sd.validated_data
            check=Attendance.objects.filter(user=data['user'],date=data['date']).first()
            if check is not None:
                return Response({"error":"this entry already recorded !!!"})
            sd.save()
            return Response({'successful': 'Attendance marked successfully'}, status=201)
        else:
            return Response(sd.errors, status=400)



'''Home method is linked with / route. this is a MVT bais route that render a html page, and this method pass the employee list into the html page. '''

def Home(request):
        employees = Employee.objects.all()
        return render(request, 'home.html', {'employees': employees,'message':'Welcome to Employee Management System'})
    


'''employee_details method is linked with /employee/ route. This is a MVT bais route that render a html page,
 and this method pass the employee details and attendance details into the html page that has been queryed. '''

def employee_details(request):
    employee_id=request.GET.get('employee_id')
    employee = get_object_or_404(Employee, pk=employee_id)
    attendance=Attendance.objects.filter(user=employee)
    return render(request, 'employee_details.html', {'employee': employee,"attendance":attendance})



'''department_report method is linked with /department-report/ route. This is a MVT bais route that render a html page,
and this method pass the department details into the html page.'''

def department_report(request):
    departments = Employee.objects.values('department').annotate(employee_count=Count('id'))
    return render(request, 'department_report.html', {'departments': departments})