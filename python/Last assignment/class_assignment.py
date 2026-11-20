# Project: Student Management System Build a menu-driven
# Student Management System using Python OOP.
# The application should allow the user to manage multiple
# students through a simple console interface.

# Functional Requirements
# 1. Student Class: Create a Student class with Student ID, Name, Age, Course, and Marks.
# 2. Constructor: Use __init__() to initialize student data. 
# 3. Display: Create display_student() to show complete student information. 
# 4. Grade: Create calculate_grade() to calculate and display the student's grade from marks.
# 5. Multiple Students: Store and manage multiple Student objects using a list.
# 6. Search: Search for a student using Student ID. 
# 7. Update: Update a student's details or marks.
# 8. Delete: Delete a student from the system.

# Required Menu
# 1. Add Student 
# 2. View All Students 
# 3. Search Student 
# 4. Update Student 
# 5. Delete Student 
# 6. Exit

# Student ID, Name, Age, Course, and Marks.
class Student:
    def __init__(self,id,name,age,course,marks):
        self.studentID=  id
        self.studentname=  name
        self.studentage=  age
        self.studentcourse=  course
        self.studentmarks= marks

    def display(self):
        print(f"This is data of {self.studentname}")
        print("student ID is",self.studentID) 
        print("stdudent name is",self.studentname)
        print("student age is",self.studentage)
        print("student course is",self.studentcourse)
        print("student marks are",self.studentmarks)

    def grade(self):
        if self.studentmarks >= 90:
            print(f"{self.studentname} => Grade: A")
            
        elif self.studentmarks >= 80:
            print(f"{self.studentname}Grade: B")

        elif self.studentmarks >= 70:
            print(f"{self.studentname}Grade: C")

        elif self.studentmarks >= 60:
            print(f"{self.studentname}Grade: D")

        else:
            print(f"{self.studentname}Grade: F")

            


studentlist=[]
choice=''
while choice != 7:
    print("You have 7 options")
    print("1)You can add a Student")
    print("2)You can view all students{If you have entered multiple studsents}")
    print("3)You can see students grade")
    print("4)You can search student with ID")  
    print("5)You can update student data")
    print("6)You can delete a student")
    print("7)You can exit the program")
    choice=int(input("Enter your choice in numbers"))


    if choice==1:
        ID1= len(studentlist) + 1
        name1=input("Enter student Name")
        age1=input("Enter student age")
        course1=input("Enter student course")
        marks1=int(input("Enter student marks from 0 to 100"))
        student1=Student(ID1,name1,age1,course1,marks1)
        print("Stdudent is added")
        student1.display()
        studentlist.append(student1)
        
    if choice==2:
        for item2 in studentlist:
            item2.display()
            
    if choice==3:
        for item3 in studentlist:
            item3.grade()
            

    if choice==4:
        ID4=int(input("Enter student ID"))
        for item4 in studentlist:
            if item4.studentID == ID4:
                item4.display()
                break

    if choice==5:
        var5=int(input("Enter student  ID"))
        for item5 in studentlist:
            if item5.studentID == var5:
                name5=input("Enter new name")   
                age5=input("Enter new age")   
                course5=input("Enter new course")   
                marks5=int(input("Enter new marks"))
                item5.studentname=name5
                item5.studentage=age5
                item5.studentcourse=course5
                item5.studentmarks=marks5   
                item5.display()
                break


    if choice==6:
        var6=input("Enter student ID of student you want to delete")
        for item6 in studentlist:
            if item6.studentID == var5:
                studentlist.remove(item6)
                print(f"Student is deleted")
                for item000 in studentlist:
                    item000.display()
                    break
