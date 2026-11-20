# Create a Student Management App in Python using a list of student records.
# Your program must include the following features:
# 1. Add 5 students by default when the program starts.
# 2. Allow the user to add a new student.
# 3. Allow the user to update an existing student.
# 4. Allow the user to delete a student.
# 5. Display all students' IDs and email addresses

students=[
          {"Name":"Ahmad","ID":"001","Email":"ahmad@gmail.com"},
          {"Name":"Hamza","ID":"002","Email":"hamza@gmail.com"},
          {"Name":"Asim","ID":"003","Email":"asim@gmail.com"},
          {"Name":"Sadaqat","ID":"004","Email":"sadaqat@gmail.com"},
          {"Name":"Haseeb","ID":"005","Email":"haseeb@gmail.com"}
          ]
choice=""
while choice != "7":
    print("There are 7 option to choose")
    print("1)You can add a Student")
    print("2)You can update a Student")
    print("3)You can delete a Student")
    print("4)You can display a Students Email and ID")
    print("5)You can display all students Email and ID")
    print("6)You can display compelete Student list")
    print("7)You can exit the program")
    choice=input("Enter your choice:")



    if choice=="1":
        newstudent={}
        name1=input("Enter student name")
        newstudent={"Name":name1}
        Id1=input("Enter students ID")
        newstudent["ID"]=Id1
        student_mail=input("Enter student email")
        newstudent["Email"]=student_mail
        students.append(newstudent)
        print("New student is added in the list",students)

    elif choice=="2":
        print("This is the existing list",students)
        nameupdatecheck=input("Enter the name of student you want to update")
        indexupdate = -1        
        for item in students:
            if item["Name"]== nameupdatecheck:
                indexupdate=students.index(item)
        if indexupdate == -1:
            print("Student is not in our list")
        else:
            nameupdate=input("Enter new name for student")
            students[indexupdate]["Name"]=nameupdate
            IDupdate=input("Enter new ID for student")
            students[indexupdate]["ID"]=IDupdate
            emailupdate=input("Enter new email for student")
            students[indexupdate]["Email"]=emailupdate
            print("Your updated student is now in the list", students)

    elif choice=="3":
        print("This is the existing list", students)
        namedelete=input("Enter then name of student you want to delete")
        indexdelete= -1
        for item3 in students:
            if item3["Name"]==namedelete:
               indexdelete=students.index(item3)
        if indexdelete == -1:
            print("Student not in the list")
        else:
            del students[indexdelete]
            print("Your student is deleted from the list", students)

    elif choice=="4":
        print("this is your existing list", students)
        mail_id=input("Enter the name of student whose data you want")
        indexmailid= -1
        for item4 in students:
            if item4["Name"]==mail_id:
                indexmailid=students.index(item4)
        if indexmailid == -1:
            print("Student is not in the list")
        else:
            print("ID is",students[indexmailid]["ID"])
            print("Email is",students[indexmailid]["Email"])

    elif choice=="5":
        for item5 in students:
            choice5=print("ID:",item5["ID"], "Email:",item5["Email"])

    elif choice=="6":
        print("The complete list is" ,students)

print("The program has ended")
