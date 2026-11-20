#1. Light Bulb Experiment
#● Objective: Simulate a light bulb's on/off state.
#● Task:
#○ Write a program that asks the user to input either 1 (turn on) or 0 (turn off).
# Use an if condition to print "The light is ON" or "The light is OFF."
#● Extension: Add a third option to print "Invalid Input" if the user enters anything other
#than 1 or 0.


userinput = int(input("Enter 0 or 1"))
if userinput == 1 :
    print("The light is ON")
elif userinput == 0 :
    print("The light in OFF")
else:
    print("Invalid Number")
            