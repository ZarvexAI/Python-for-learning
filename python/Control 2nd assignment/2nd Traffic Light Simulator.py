# 2. Traffic Light Simulator
# ● Objective: Simulate traffic light behavior.
# ● Task:
# ○ Accept an input (Red, Yellow, Green) from the user.
# ○ Use if conditions to display:
# ■ "Stop" for Red
# ■ "Slow Down" for Yellow
# ■ "Go" for Green
# ● Extension: Add a default message for invalid inputs like "Invalid Color."

userinput = input("Enter either Red, Yellow or Green")
if userinput == "Red" or userinput == "red":
    print("Stop")
elif userinput == "Yellow" or userinput == "yellow":
    print("Slow down")
elif userinput == "Green" or userinput == "green":
    print("Go")
else:
    print("Invalid Color")
