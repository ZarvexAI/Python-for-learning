#For loop ==> sirf list py hi lagta hy
#used when lists come/ while is not better for lists loop
#list ky ilawa jahan marzi loop toh while
usernames=["ahmad","ali","asim","hamza","umar"]
#syntax
for item in usernames:#for is keyword, item is a variable for loop to store list enteries, in is membership operator to check list, usernames is list name
    print(item)
    #list ka 0 index iska starting point and ending point last index
    #yeh hamesha 1 ky icreament sy chalta hy
    #yeh list ka first entery item ko dega print karega then next entery and so on


#to check index through for loop we use a function of enumerate to use this we need 2 variables
for index, value in enumerate (usernames):
    print(index, value)#first variablle mn index and second mn entery
#now we also get index stored in index


#and if we want to put mr. with even indexes
for index, value in enumerate (usernames):
    if index % 2 == 0:
        print("mr"+value)


#writte a program to search asim uisernames if asim found then print asim and break loop
usernames=["ahmad","ali","asim","hamza","umar"]
for item in usernames:
    if item == "asim":
        print(item)
        break#this function will now end the loop so that it doesnt check further after asim is found
    else:
        print("asim not found")

mylist= list(range(1,10,1))#range is function 1st value is starting point 2nd is ending point 3rd is increament
#and default steps is one and ending point is alsways one more than actual execution
print(mylist)


#to use for like while like to print counting
#we use range 
for item in range(1,11):
    print(item)#this prints counting


#what if we wanna update enteries in list
usernames=["ahmad","ali","asim","hamza","umar"]
newlist=[]
for item in usernames:
    newlist.append("mr."+item)
usernames=newlist
print(usernames)#we see that usernames is updated now
#iski wajah sy new list ban jati hy hamien yeh ni chahiye hamien bas update karna hy


#thre is also a function in python with no name called lambda
#iska syntax yeh hy ky no name, no paranthesis needed for parameter, no return needed, no multilines, 
#lambda value: "mister"+value
#yeh same kaam kary ga jo aik simple function karta hy example iski map ky saath hogi


#first map loop
usernames=["ahmad","ali","asim","hamza","umar"]
def mapfunc(value):
    return "mister"+value
usernames=list(map(mapfunc,usernames))#pehly  parametr my koi functon banao dusra parameter mn wo list jo chaly gi
print(usernames)
#jo list de rahy hn wo one by one value pick kakrky wo us function mn pass kardega
#map new list banata hy aur index same rehta jo real list ka tha yeh uski length kam ni karsakta
#ab wo karien gy lambda sy
usernames=list(map(lambda value: "misterlamba"+value,usernames))
print(usernames)#same kaam huwa without def function


#Now for filter loop
nums = [12,33,22,54,66,54,52,33,67]
def filterfunc(value):
    if value % 2 == 0:
        return value
output=list(filter(filterfunc,nums))
print(output)#see isny length kam karky new list 
#we can do same with lambda function
output=list(filter(lambda value: value % 2 == 0,nums))
print(output)#same kaanm huwa but with less code


#map loop and filter loop==> filter len kam karsakta hy but update ni karsakta but map update karsakta hy lekin length kam ni karsakta
#lets say mn yeh filter wala kaam map sy karna chahun toh kya hoga lets see
nums=list(map(lambda value: value % 2 == 0,nums))
print(nums)#see isny kam karny ki bajaye condition sab index par laga di
#ab filter ko map wali example par laga kar dekhty hn
usernames=["ahmad","ali","asim","hamza","umar"]
usernames=list(filter(lambda value: "misterlamba"+value,usernames))
print(usernames)#isny list update ni ki
