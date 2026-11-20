#Insert function
studentnames=["ahmad","zuhaib","asim","zaryab"]
studentnames.insert(0,"sadaqat")  #the paranthesis contains two things 1st is index and second is what to add
print(studentnames)
#if we need to put it in centre
output =studentnames.insert(int(len(studentnames)/2),"zarnab")  #we take int bcs if 2.5 ajaye then float error ayega int mn yeh ni hoga
print(studentnames)
print(output) #it returns none


#Count function
#it checks ky koi cheez array mn kitni baar ayi hy
output=studentnames.count("ahmad")
print(output) #it returns 1 bcs ahmad list mn 1 baar aya


#Sort function
#yeh list ko alphabetically bana deta hy a sy z tak pehly upercase ko acsending order mn then lowercase ko
output=studentnames.sort()
print(studentnames)
print(output) #it returns none


#Reverse function
#puri list ghuma dega like ulta kardega
output=studentnames.reverse()
print(studentnames) #puri list ko ulta kardega
print(output) #returns none


#Clear function
#it clears the compelete list
output=studentnames.clear()
print(studentnames)
print(output)
studentnames=["ahmad","zuhaib","asim","zaryab"]


#Copy function
#it copies the compelete list and returns the same list
output=studentnames.copy() #copy will be stored in "output"
print(output) #returns the copy
print(studentnames) 


#Membership operator
#checks ky koi cheez kisi array mn hy ky ni
print("ahmad" in studentnames) #true bcs ahmad list mn hy


#Identity operator 
#checks if two things are same
print("zuhaib" is studentnames) #false bcs not same
print(studentnames is studentnames) #true bcs true


#Repitition
#if we multiply a list by a number it add the same list that number of times
studentnames=studentnames*2
print(studentnames)


#Concatation
#adding two lists into 1
nums=[1,2,3]
output=studentnames+nums 
print(output)