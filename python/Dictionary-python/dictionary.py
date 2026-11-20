#agar apky paas koi entity hy aur apny usky related koi data save karna hy toh ohit app list na use karien ap dictionary use karie
#it is shown by {}

car1=    {
    # property_name : propert_value,
    "name":"sonata",
    "model":"asd-2342",
    "color":"black"
    }
car2=    {
    # property_name : propert_value,
    "name":"suzuki",
    "model":"daf-2342",
    "color":"black"
    }

print(car1)
print(car1["name"])
print(car2["model"])
#now what if we want new property in the dictionary remember we studied append now we kinda do that
car1["rims"]="black"
print(car1)
#we can also update existing enteries
car1["name"]="honda"
print(car1)
#what if we want to delete some property
del car1["rims"]
print(car1)#see rims got deleted
#rule for data management
#CRUD[C is for create, R for read, U for update, D for delete]
#now lets make a list for 2 dictionary and in list you dint make new variable for dictionary instead we get indexes made by ram
car=[
    {
    # property_name : propert_value,
    "name":"sonata",
    "model":"asd-2342",
    "color":"black"
    },
    {
    # property_name : propert_value,
    "name":"suzuki",
    "model":"daf-2342",
    "color":"black"
    }
]
print(car[0])
print(car[0]["name"])#to read data from list and dictionary you put the indedx on which the
#dictionary is on and the property which you want
car[0]["color"]="blue"#this is how we update dictionary in list
print(car[0]["color"])
#now lets say i wanna delete both color from list car
for item in car:
    del item["color"]
print(car)
#what if we want to delete a full disctionary from list
del car[0]
print (car)
#what we want color from whole list in dictionary
for item in car:
    print(item["color"])



# Create a Student Management App in Python using a list of student records.
# Your program must include the following features:
# 1. Add 5 students by default when the program starts.
# 2. Allow the user to add a new student.
# 3. Allow the user to update an existing student.
# 4. Allow the user to delete a student.
# 5. Display all students' IDs and email addresses