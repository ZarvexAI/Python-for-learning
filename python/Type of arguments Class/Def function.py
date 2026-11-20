# def add(num1=5 ,num2=4):
#     result = num1 + num2
#     print(result)
# add(12,7)

#types of arguments
#positonal or required arguments are sequential like num1 and num2 are positional arguments
#we can also give default value in parameter so when or if user does not pass value default value is used
#you can use it as def add(num1 = 9, num2) here num1 has a default value where num2 doesnt
#first value always goes to num1 so what if we wanna pass it to num2 but use num1 as default how?
#we use parameter name like add(num2=5) now num1 is default but num2 is given...this is called keyword arguments
#add(num2=5 , num1=5) this is also valid
#now positional only arguments
#means 1st num in 1st only
#to use this use "/"
#all the parameter before / will become positional only arguments so if you use keyword arguments here it 
#will give error because you cant change places
#like def add(num=3 , num2=4 , /) now the 1st two variables as in before / will never be used with keyword arguments
#now you cant say num2=4 , num1=3 this is false only (4, 5)  this will store 4 in num1 and 5 in num2


# def add(num1= 4, / , num2=5):
#     result = num1 + num2
#     print(result)
# add (4 , num2= 1 ) #this is good but num1=anything and the not specifying num2 is wrong   

#then there are keyword only
#to use them put "*" at the start of variables
# def test2 (*, num3 = 5 , num4 = 5):
#     result2 = num3 + num4
#     print(result2)
# test2(num3= 5, num4= 2)    

#pehly ham declration my print karahy thy value but agar print bahhir likhien toh none dyga

# def add (num1, num2):
#     result = num1 + num2 #now i will not put print buti want output
# print(add(4,6))    #now this gives none as output
#to solve this put return keyword in declaration like  
# def add (num1, num2):
#     result = num1 + num2 
#     return result
# output= add(30,21)
# print (output)

#we can also use functions within fucntions like

def multiply(a, b):
    multi= a * b
    return multi


def add(num1, num2):
    result= multiply(num1, num2)
    return result

output= add(10, 30)
print(output)

#function mn jahan ap return laga do gy us sy neechy koi line nahi chaly gi theres only one return in one function aur yeh 
#return end py ayega