from django.db import models

'''Employee table contant total five fields. one of them is id that created by default. 
All of this fileld can't be none. name field store name of the employee, designation field store designation of the employee, 
department field store department of the employee and doj field store date of joinging of the employee in yyyy-mm-dd fomat'''
class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    doj = models.DateField()


'''Attendance table contant total four fields. one of the is id that created by default.
 all of this field can't be none. user field is foreign key that takes instance of employee.
 date field store the date of attendance and status take the status of attendance (it take only Absent or Present)'''
class Attendance(models.Model):
    user = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'present'), ('Absent', 'absent')])
