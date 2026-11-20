# 7. Password Strength Checker
# ● Objective: Check the strength of a password.
# ● Task:
# ○ Take a password as input and check conditions:
# ■ Length >= 8: Print "Strong Password"
# ■ Length between 5 and 7: Print "Moderate Password"
# ■ Length < 5: Print "Weak Password"

# ● Extension: Check if the password contains numbers or special characters for more
# detailed feedback.

password= (input("enter your desired password"))
if len((password)) >= 8:
    print("strong password")
elif len((password)) >= 5 and len((password)) <=7:
    print("moderate password")
elif len((password)) <5 :
    print("weak password")    