#Python Lists Assignment

#1. List Creation Objective: Practice Python Lists. Task: Ask user to enter 5 favorite fruits, 
#store in list, print list. Extension: Print first and last fruit.
Fruits=[]
Fruits.append(input("enter 1st fruit"))
Fruits.append(input("enter 2nd fruit"))
Fruits.append(input("enter 3rd fruit"))
Fruits.append(input("enter 4th fruit"))
Fruits.append(input("enter 5th fruit"))
print(Fruits)
print(Fruits[0])
print(Fruits[4])


#2. Student Marks Objective: Practice Python Lists. Task: Input marks of 5 subjects,
#store in list, print all. Extension: Print highest and lowest marks.
marks=[]
marks.append(input("enter marks of 1st subject"))
marks.append(input("enter marks of 2nd subject"))
marks.append(input("enter marks of 3rd subject"))
marks.append(input("enter marks of 4th subject"))
marks.append(input("enter marks of 5th subject"))
print(marks)
marks.sort()
print(marks[0])
print(marks[4])


#3. Sum of List Objective: Practice Python Lists. Task: Input 5 numbers,
#store and print sum. Extension: Print average.
nums=[]
nums.append(int(input("enter num 1st")))
nums.append(int(input("enter num 2nd")))
nums.append(int(input("enter num 3rd")))
nums.append(int(input("enter num 4th")))
nums.append(int(input("enter num 5th")))
print(nums)
sum=sum(nums)
print(sum)
average=sum/len(nums)
print(average)


#4. Find Maximum Objective: Practice Python Lists. Task: Input 6 numbers and
#display maximum. Extension: Display minimum too.
num4=[]
num4.append(int(input("enter num 1st")))
num4.append(int(input("enter num 2nd")))
num4.append(int(input("enter num 3rd")))
num4.append(int(input("enter num 4th")))
num4.append(int(input("enter num 5th")))
num4.append(int(input("enter num 6th")))
num4.sort()
print(num4)
print(num4[0])
print(num4[5])


#5. Search an Item Objective: Practice Python Lists. Task: Create list of
#5 cities and search a city. Extension: Print index if found.
citys=["Islamabad","Lahore","Faisalabad","Karachi","Quetta"]
"Islamabad" in citys
result1=citys.index("Islamabad")
print(result1)
"Lahore" in citys
result2=citys.index("Lahore")
print(result2)
"Faisalabad" in citys
result3=citys.index("Faisalabad")
print(result3)
"Karachi" in citys
result4=citys.index("Karachi")
print(result4)
"Quetta" in citys
result5=citys.index("Quetta")
print(result5)


#6. Even Numbers Objective: Practice Python Lists. Task: Input 10
#numbers and print even numbers. Extension: Print odd numbers too.
numbers=[]
evennums=[]
oddnums=[]
i=1
while i<=10:
    num6=int(input("Enter any number"))
    numbers.append(num6)
    if num6%2==0:
        evennums.append(num6)
    else:
        oddnums.append(num6)
    i+=1
print(numbers)
print(evennums)
print(oddnums)


#7. Reverse a List Objective: Practice Python Lists. Task: Input 5
#names and print reverse order. Extension: Print original and reversed.
names=[]
i=1
while i<=5:
    num7=(input("Enter any name"))
    names.append(num7)
    i+=1
print(names)
names.reverse()
print(names)


#8. Count an Element Objective: Practice Python Lists. Task:
#Count occurrences of a user-entered number. Extension: Show Not Found if absent.
number11=[]
i=1
while i<=5:
    num8=int((input("Enter any num from 1 to 5")))
    number11.append(num8)
    i+=1
print(number11)    
output=number11.count(1)
print("number 1 is found",output)
if output == 0:
    print("Not found")
output=number11.count(2)
print("number 2 is found",output)
if output == 0:
    print("Not found")
output=number11.count(3)
print("number 3 is found",output)
if output == 0:
    print("Not found")
output=number11.count(4)
print("number 4 is found",output)
if output == 0:
    print("Not found")
output=number11.count(5)
print("number 5 is found",output)
if output == 0:
    print("Not found")


#9. Remove an Item Objective: Practice Python Lists. Task:
#Remove a color from a list. Extension: Handle missing color.
colour=["red","yellow","blue","black","white"]
removal=input("enter which color to remove")
if removal in colour:
    colour.remove(removal)
else:
    print("colour not it list")


#10. Add an Item Objective: Practice Python Lists. Task:
#Add a programming language. Extension: Print total count.
programlanguages=["c++","python","java"]
userinput=input("enter any language")
if userinput in programlanguages:
    print("already exist")
else:
    programlanguages.append(userinput)
    output=len(programlanguages)
    print("there are",output,"programming languages")
    print(programlanguages)


#11. Sort Numbers Objective: Practice Python Lists.
#Task: Sort 8 numbers ascending. Extension: Also descending.
numbers11=[]
i=1
while i<=8:
    userinput=int(input("enter any number"))
    numbers11.append(userinput)
    i+=1
numbers11.sort()
print(numbers11)
numbers11.reverse()
print(numbers11)


#12. Duplicate Detection Objective: Practice Python Lists.
#Task: Print duplicate values. Extension: Print unique values.
numbers12=[]
duplicates=[]
uniques=[]
i=1
while i<=5:
    userinput=int(input("enter any number"))
    numbers12.append(userinput)
    i+=1
i=0
while i < len(numbers12):
    num=numbers12[i]
    if num > 1:
        if num not in duplicates:
            duplicates.append(num)
    else:
        uniques.append(num)
    i+=1
print("originial list is", numbers12)
print("duplicates are", duplicates)
print("uniques are", uniques)


#13. Merge Two Lists Objective: Practice Python Lists.
#Task: Merge two lists of 5 numbers. Extension: Sort merged list.
list1=[23,4,22,43,6]
list2=[12,55,33,21,22]
list1.extend(list2)
print(list1)
list1.sort()
print(list1)


#14. List Length Objective: Practice Python Lists.
#Task: Input 7 names and print total. Extension: Print names with indexes.
names=[]
i=1
while i<=7:
    name=input("enter any name")
    names.append(name)
    i+=1
print(names)
i=0
while i<len(names):
    print(i,names[i])
    i+=1


#15. Largest Word Objective: Practice Python Lists.
# Task: Input 5  and print longest. Extension: Print shortes
words=[]
i=1
while i<=5:
    word=input("enter any word")
    words.append(word)
    i+=1
print(words)
longest=words[0]
shortest=words[0]
i=1
while i<len(words):
    if len(words[i])>len(longest):
        longest=words[i]
    if len(words[i])<len(shortest):
        shortest=words[i]
    i+=1
print("longest words is",longest)
print("shortest words is", shortest)


#16. Positive & Negative Objective: Practice Python Lists.Task:
#Input 10 integers and print positives. Extension: Print negatives separately.
integers=[]
i=1
while i<=10:
    ints=int(input("enter any integers"))
    integers.append(ints)
    i+=1
positives=[]
negatives=[]
i=0
while i<len(integers):
    if integers[i]>=0:
        positives.append(integers[i])
    if integers[i]<0:
        negatives.append(integers[i])
    i+=1
print(positives)
print(negatives)


#17. Replace an Item Objective: Practice Python Lists.
#Task: Replace one subject with another. Extension: Handle missing subject.
subjects=["Maths","Physics","Chemistry","Biology"]
oldsubject=input("enter which subject you want replaced")
newsubject=input("enter new subject")
if oldsubject in subjects:
    wantedindex=subjects.index(oldsubject)
    subjects[wantedindex]=newsubject
else:
    print("subject not in list")
print(subjects)


#18. Second Largest Objective: Practice Python Lists. Task:
#Print second largest of 8 numbers. Extension: Print second smallest.
number=[]
i=1
while i <= 8:
    userinput=int(input("enter any number"))
    number.append(userinput)
    i+=1
number.sort()
print(number)
print("second largest number in list is", number[6])
print("second smallest number in list is", number[1])


#19. Multiplication Table Objective: Practice Python Lists. Task:
#Store table 1-10 of a number in list. Extension: Print in table format.
table=[]
resultnumber=int(input("enter your number"))
i=1
while i <= 10:
    result= resultnumber*i
    table.append(result)
    i+=1
print(table)
i=1
while i<=10:
    print(resultnumber,"X",i,"=",table[i-1])
    i+=1


#20. Shopping List Manager Objective: Practice Python Lists. Task:
#Create shopping list with 5 items. Extension: Remove one item and show updated list.
items=[]
i=1
while i<=5:
    item=input("enter your item")
    items.append(item)
    i+=1
print(items)
removalitem=input("enter which item you want removed")
if removalitem in items:
    items.remove(removalitem)
    print("updated list is below")
    print(items)
else:
    print("item not in list")