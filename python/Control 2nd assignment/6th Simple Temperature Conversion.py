# 6. Simple Temperature Conversion
# ● Objective: Convert Celsius to Fahrenheit or vice versa.
# ● Task:
# ○ Ask the user to choose a conversion type: 1 for Celsius to Fahrenheit, 2 for
# Fahrenheit to Celsius.
# ○ Take the temperature as input and use the formulas:
# ■ C to F: F=(C×9/5)+32
# ■ F to C: C=(F−32)×5/9
# ○ Print the result using if conditions to ensure the correct formula is applied.

print ("temprature converion!")
print ("for celsius to farenheit ==> 1")
print ("for farenheit to celsius ==> 2")

conversion = int(input("1 or 2"))
temprature = float(input("enter temprature"))

if conversion == 1 :
    farenheit= (temprature*9/5)+32
    print("your temp in farenheit is", farenheit)
elif conversion == 2:
    celsius= (temprature-32)*5/9
    print("your tempratuer in celsius is",celsius)
else:
    print("wrong coversion chosen")
