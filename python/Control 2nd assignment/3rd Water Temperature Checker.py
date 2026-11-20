# 3. Water Temperature Checker
# ● Objective: Categorize water temperature based on input.
# ● Task:
# ○ Ask the user to input the temperature in Celsius.
# ○ Use if conditions to print:
# ■ "Freezing" if temperature <= 0
# ■ "Cold" if temperature > 0 and <= 15
# ■ "Warm" if temperature > 15 and <= 30
# ■ "Hot" if temperature > 30

temprature = int(input("Enter temp in celcius 0 to 30"))
if temprature <= 0:
    print("freezing")
elif temprature > 0 and temprature <= 15:
    print("cold")
elif temprature > 15 and temprature <= 30:
    print("warm")
elif temprature > 30:
    print("hot")            