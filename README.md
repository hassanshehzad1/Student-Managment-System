<h1>Student Managment System </h1>
This project is built in python with help of Tkinter GUI toolkit. It is designed to manage and display student-related data, including courses ,results, and reports.Below is a simplifed explaination of how to use and understand the system.

<h2>Features</h2>
Course Managment: ADD, UPDATE AND DELETE and Search for COURSES
Student Managment: Manage Student Details, including enrollment, contact, and personal details.
Result Managment:Record and Display student results.
Dashboard:Display statsitcs on the total number of courses ,students,and results.
Report generation:View and Manage student reports.
Logina and register the user.
logout the user

<h2>Installation Requirements</h2>
python 3.x:Ensure Python is installed
Pillow Library:For handling images,install using
<strong>pip install pillow</strong>

Tkinter:It comes pre-installed with pyhton
Sqlite3:Used as database


<h2>How to run the system</h2>
Clone or downlod the project files.
Run the script create_db() to set up the necessary database
python your_script_name.py

<h2>Modules overview</h2>
Purpose:Manage course details such as name, duration, changes and description.
Actions:
 Add:Enter course details and click save.
 Update:Select a course form the list, modify,delete and click update.
 Delete:Select a course form the list,Click delete.
 Clear:Reset the form fields.

 <h2>Student Managment System</h2>
 Purpose:Record and maintain student details.
 Actions:Similar to course managment, allowing adding updating deleting and clearing student data.
 
 <h2>Result Managment System</h2>
 Purpose:Store and view student's performance
 Actions:Add or update marks of the students based on their courses.
 
 <h2>Dashboard</h2>
 Purpose:Display the total number of
  Courses
  Students
  Results
Updates dyanamically


<h2>Buttons and their features</h2>
Course:Opens the course managment system
Student:Opens the student managment system
Result:Opens the result managment system
View result:Display a deatil reports od results
logout:logs out the system
Exit:Close the application


<h2>Database Structure</h2>
The system uses SQLite3 to store data:

course Table:

cid: Course ID (Primary Key)
name: Course name
duration: Duration of the course
charges: Course charges
description: Course description
student Table:

roll: Roll number (Primary Key)
name: Student name
email: Email address
gender: Gender
dob: Date of Birth
contact: Contact number
admission: Admission date
course: Enrolled course
state: State of residence
city: City of residence
pin: PIN code
address: Address
result Table:

rid: Result ID (Primary Key)
roll: Student roll number
name: Student name
course: Enrolled course
marks_ob: Marks obtained
full_marks: Full marks
per: Percentage
employee Table:

eid: Employee ID (Primary Key)
f_name: First name
l_name: Last name
contact: Contact number
email: Email
question: Security question
answer: Security answer
password: Password



<h2>Known Issues</h2>
Ensure unique course names to avoid duplicates
Handle database connections errors gracefully
Keep backup of rms.db





