#if you need to enter A 100 names you will need 100 unique names and a lot of time and
#the data will be stored in a random order not in a list
#to solve this problem python gives us list or aray
#to use this we put []
studentnames = ["hamza", "abdullah", "qasim", "huzaifa", "zuhaib"]
#to get a specific name from list we use the index that ram gives to the names it goes as 0,1,2,3,4
#if we needd zuhaib we,ll use
print(studentnames[0]) #well get hamza
#studentnames is variable name and all the data enterd in the array is ram indexing
#if we do something like print(studentnames[10]) this will give error
#array is also a data type
# we can also do print(studentnames[-1]) this will give "zuhaib" similarly if we do print(studentnames[-2]) well get "huzaifa"
print(studentnames[-3]) #well get "qasim"
#now how could we update the enteries in the list like what if we needed to change "abdullah" to "ahmad"
studentnames[1]="ahmad" 
print(studentnames[1]) #this will now give ahmad
#this way we can only update the indexes already existing


#if we need to add another entery in array we cannot add like this studentnames[5]="asim" this is wrong it will give error
#that is done by built in functions
studentnames.append("asim")#this function "append" can add new enteries on the END of the list 
#syntax is as given above
#we can only give one append value at a time
#the append functin doesnt return any value only adds the entery in the list if we do
output= studentnames.append("asim")
print("output", output) #this will give none this means that it only add entery in list
print(studentnames) #this gives also the appended name now list is updated


#now to upadate an entire list to another list we use "extend"
nums=[10,20,30]
#now i wanna add nums to studentnames we use extend like
output1=studentnames.extend(nums)
print(studentnames) #this gives nums included in the studentnames
#this also returns no value like
print("output", output1) #it gives none


#there is a function known as "pop" this deletes enteries/indexes in the array and also returns whats deleted
test= studentnames.pop()#this will delete the last value of the studentnames
print(test) #this returned the value pop deleted
print(studentnames)#this deleted the last index


#now what if we needed to delete specific index
#first we need to find length of the list like len[]
#pop deletes data by index but theres a new function for when i need to delete by name/value for example i need to delete hamza
#then we use remove function 
test2= studentnames.remove("hamza")#this will delete hamza
#this also doesnt return value
print(studentnames)#we see hamza is deleted from list
#also remove function deletes 1st names if there are duplicate names

#there is also a function to find index of any value of a list
Test3=studentnames.index("huzaifa")#this will give us the index of huzaifa in the list
print(Test3) #this shows that index is 2 of huzaifa

len[studentnames]