def add():
    userinput1= int(input("enter any numer"))
    userinput2= int(input("enter any numer"))
    sum = userinput1+ userinput2
    print("the sum is", sum)


add()
#the brackets in declaration are used to recieve data from function call
#the brackets in calling are used to pass data to daclaration
#to recieve data from call make variables in brackets of declaration like

def test(num1,num2):
    result= num1 + num2
test(20,12)    
#data in paranthesis of calling are called arguments
#data in parantesis of declaration are called parameters