# 5. Simple Alarm System
# ● Objective: Simulate an alarm trigger based on conditions.
# ● Task:
# ○ Ask the user two yes/no questions:
# ■ Is the door open? (yes or no)
# ■ Is motion detected? (yes or no)
# ○ Use if conditions to print:
# ■ "Alarm Triggered" if either condition is yes.
# ■ "All Safe" if both conditions are no.

door = input("is door open? yes or no")
motion = input("is motion detected yes or no")
if door or motion == "yes":
    print("Alarm trigerred")
elif door or motion == "no":
    print("All safe")
