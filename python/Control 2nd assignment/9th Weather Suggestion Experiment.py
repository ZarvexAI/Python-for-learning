# 9. Weather Suggestion Experiment
# ● Objective: Give outfit suggestions based on weather conditions.
# ● Task:
# ○ Take weather input (Sunny, Rainy, Cold) from the user.
# ○ Print:
# ■ "Wear sunglasses" for Sunny
# ■ "Take an umbrella" for Rainy
# ■ "Wear a jacket" for Cold

userinput= input("enter weather as ==> Sunny, Rainy or Cold")
if userinput == "Sunny" or userinput == "sunny":
    print("Wear sunglasses")
elif userinput == "Rainy" or userinput == "rainy":
    print("Take an umbrella")
elif userinput == "Cold" or userinput == "cold":
    print("Wear a jacket")     
else :
    print("invalid input")

# now with match case
userinput1 = input("enter weather as ==> sunny, rainy or cold")
match userinput1 :
    case "sunny" :
        print("wear sunglasses")
    case "rainy" :
        print("take an umbrella")
    case "cold" :
        print("wear a jacket")    
    case "Sunny" :
         print("wear sunglasses")
    case "Rainy" :
         print("take an umbrella")
    case "Cold" :
        print("wear a jacket")    
    case _ :
        print("invalid input")    