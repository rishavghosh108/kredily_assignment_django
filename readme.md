This is a HRMS(human resorce management system) base assignment.

    start server:=>
        1. step 1, unzip the file (rishavghosh147@gmail.com.zip)
        2. step 2, run 'cd kredily_assignment_in_django'
        3. step 3, run 'pip install -r requirements.txt'
        4. step 4, run 'python manage.py runserver'


        ** some data already feeded **

    reset database:=>
        1. run 'rm -r db.sqlite3' from 'kredily_assignment_in_django/' path  or delete 'db.sqlite3' directly
        2. run 'python manage.py migrate'


    feature:=>

        1. add new employee . (duplicate data can't be store)
        2. get all employees .
        3. mark attendance .
        4. get attendance details of a employee.
        5. get department details.(the count of employees in each department.)



        1: for add new emplyee  =>
            go to 'localhost:8000/' or 'localhost:8000/employees/' route to add a new employee.

        2: for get all the employees  =>
            got 'localhost:8000/' or 'localhost:8000/employees/'(access or hit the post method) route to get all employees.

        3: for mark attendance  =>
            go to 'localhost:8000/' give attendance on attendance section or 'localhost:8000/attendance/' and use post method to add record.

        4: get attendance details of a  employee  =>
            go to 'localhost:/8000/' and fill the 'employee id' field and press 'employee_details' button.

        5: for get department details  =>
            go to 'localhost:8000/'  and click on 'department-report' button or 'localhost:8000/department-report/ route to depatment details.



    DATABASE:=>
    

        Table:  
            1. Employee
            2. Attendance

            1:  'Employee' table  stores
                (i). the name of employee on "name" field 
                (ii). department of the employee on "department" field 
                (iii). designation of the employee on "designation" field
                (iv). date of joining on "doj" field.

            2: 'Attendance' table stores
                (i). id of empleyee on "user" field
                (ii). date of attendance on "date" field
                (iii). attendance on "status" field (it takes only 'Absent' or 'Present')

    Data Validation:=>

        1. Employee Schema
        2. Attendance Schema

        1: 'Employee Schema' have 4 fields 
            (i). name . (It takes String only)
            (ii). department . (It takes String only)
            (iii). designation . (It takes String only)
            (iv). doj (date of joining) . (It takes date only with 'yyyy-mm--dd' format)

        2: 'Attendance Schema' have 3 fields
            (i). user .(It is a foreignkey with id in Employee table (auto created employee id))
            (ii). status . (It takes only 'Present' or 'Absent' as value)
            (iii). date . (It takes date only with 'yyyy-mm--dd' format)
