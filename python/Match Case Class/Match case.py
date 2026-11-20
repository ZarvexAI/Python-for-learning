# Match case it requires no condition only define cases 
# syntax
userinput = int(input("enter any num 0 to 6"))
match userinput :
  case 0 :
      print("sunday")
  case 1 :
      print("monday")
  case 2 :
      print("tuesday")
  case 3 :
        print("wednesday")
  case 4 :
        print("thursday")
  case 5 :
        print("friday")
  case 6 :
          print("saturday")
          #now for default case use "_"
  case _ :
          print("invalid number")        