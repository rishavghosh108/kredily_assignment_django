from rest_framework import serializers
from .models import Employee,Attendance

'''EmployeeSerializer have five fields. id field is only for serialization 
        (when return any employee details and while it use for deserialzation id field will not take none value).
name field take name of the employee, designation field take designation of the employee, 
department field take department of the employee and doj field take date of joinging of the employee in yyyy-mm-dd fomat
if any field is none then it return a data validation error massage.'''

class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)
    designation = serializers.CharField(max_length=100)
    doj = serializers.DateField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    

'''AttendanceSerializer have four fields. id field is only for serialization 
        (when return any attendance details and while it use for deserialzation id field will not take none value ).
user field take an instance of the employee, status field take status of attendance (it take only Present or Absent as an value if it recive an other), 
and date field take date of attendance in yyyy-mm-dd fomat
if any field is none then it return an data validation error massage.'''

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['user', 'status', 'date']

    def create(self, validated_data):
        validated_data['status']=validated_data['status'].capitalize()
        return Attendance.objects.create(**validated_data)
