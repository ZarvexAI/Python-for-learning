# we have 3 types of string
#string'' simple string
usersingle='hello'

#string"" used when ' needed in string
userdouble="hii' my name is asim"

#string""" multiple line string
usertriple='''my
name is asim
'''

#string f'' to show variable value in text
age=18
namefstring="asim"
print(f"my name is {namefstring} and my age is {age}")


#length string
#used to get len of string
print(len(userdouble))

#srting(object)
#to convert number in string
nums=1000
# lets say i wanna make thiss into string to get len
print(len(str(nums)))

#string concatination
firstname="syed"
lastname="asim"
added=firstname+lastname
print(added)

#string multiplacation
output=lastname*4
print(output)

#string indexing
print(lastname[0])#first lettr of lastname 

#stringslicing
print(firstname[1:4])
#we can also put increament of 2 so aik aik chor kar print kary
print(added[1:6:2])

#stringlower
name="muhAMAD aLI"
print(name.lower())#converts all values into lowercase

#stringupper
print(name.upper())#converts all values into uppercase

#stringcapitalize
print(name.capitalize())#convert first letter of first word into upper case

#stringtitle
print(name.title())#converts all words first letters into capital

#stringstrip
namestrip="   asim  zaryab    "
print(namestrip.strip())#it removes spaces ffrom start and end of strings
print(namestrip.lstrip())#removes left spaces
print(namestrip.rstrip())#removes right spaces

#stringfind
print(added.find("asim"))#finds srings in strings nd gives starting index of the needed string
print(added.find("Asim"))#not found then  index -1

#stringindex
print(added.index("s"))#if not found then error

#stringcount
print(added.count('s'))#tells s kitni baar aya string mn

#stringreplace
print(added.replace("asim","hamza"))#replace first parameter with second parameter
#if first parameter not found then doesnt replace

#stringsplit
printoutput=(name.split(" "))#yeh aik list banata hy split karkarky on basis of what seperator we enter in parameter
print(printoutput)

#joinstring
list=["asim","banana","apple"]
output="-".join(list)#joins a list into a string on basis of wat you put into ""
print(output)
output="/".join(list)
print(output)

#stringstartswith
fullname="muhammad ali"
output=print(fullname.startswith('m'))#checks if any variable starts with something true if its true false if false
print(output)

#stringendswith
output=print(fullname.endswith('ali'))#checks if any variable ends with something true if its true false if false
print(output)

#stringisalpha
output=print(fullname.isalpha())#check karta hy if string alphabetic hy sirf alphabets hn true if whole string is alphabetic
#agar name mn spaceing ho toh pehly space khatam karien gy woth replace then alpha check karien gy
#stringreplace
#print(added.replace("asim","hamza"))#replace first parameter with second parameter
#if first parameter not found then doesnt replace
fullname.replace(" ","")
output=print(fullname.isalpha)

#stringisdigit
output=print(fullname.isdigit) #check karta hy if string digits hy sirf digits hn true if whole string digits
print(output)

#stringalphanum
output=print(fullname.isalnum)##check karta hy if string digits or alphabetic hy sirf digits or aplphabetic hn true if whole string digits or aplhabetic
print(output)

#stringisspace
output=print(fullname.isspace)
print(output)#true sirf tab dega when whole string is space agar kahin kahin space hy tho false
