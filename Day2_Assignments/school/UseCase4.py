import students as st
import teachers as te
import results as re

id=int(input("Enter the student id:"))
name=input("Enter the student name:")
print(st.addStudents(id,name))
print(st.viewStudents())

id=int(input("Enter the teacher id:"))
sub=input("Enter the name of subject:")
print(te.assignSubject(id,sub))
print(te.viewTeachersInfo())

marks=int(input("Enter the marks:"))
print(re.calculateGrade(marks))
