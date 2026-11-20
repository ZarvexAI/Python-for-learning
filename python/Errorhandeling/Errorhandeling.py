# print("hii")
# print("hii")
# print("hii",num1)
# print("hii")
# print("hii")
#see line 3 py error hy jiski waja sy program band hojayega
#we want to fix this so ky agar error aye bhi toh program crash na kary
#there are 3 types of error syntax error and logical error and runtime error
#runtime error jis error ki waja sy prigram/file compeletly band hojaye crash hojaye
#most critical error to find is runtime error
#here error on line 3 is runtime error bcs it crahes the program and the program doesnot run any further

#try / except function
print("hii")
print("hii")
try:
    print("hii",num1)
except Exception as error:
    print("Error occured", error)
print("hii")
print("hii")
#now if error occured in line 17 app doesnt crash instead if tells about the error

#syntax try in built in function key word then indent:
#if theres no error in block then simply run but if error hy toh except blick aye toh kya return hoga
#except is built in function keyword
#"Exception" is built in parameter in python isky andar wo error ayega jo program mn hoga like a variable
#"as" yeh exception likhna mushkil hy isko exception ko chota karny ky liye as use karty hy jissy is exception waly varianble ka
#name chota hojaye
#as sy agy new name for exception variable hoga 
#yehi new variable name call karty hn jab error call karna hy like
    # print("Error occured", error)

#"else" block
#aik aur block hy else block yeh tab chlta hy jab error na aye toh yeh try ky block ky sath chaly ga
print("hii")
print("hii")
try:
    print("hii")
except Exception as error:
    print("Error occured", error)
else:
    print("else blocked occured")
print("hii")
print("hii")


#theres another block "finally"
#yeh aisa block hy jo error aeyga tab bhi except ky sath chaly aur
#na aye tb bhi try AUR else ky sath chaly

#example with error
print("hii")
print("hii")
try:
    print("hii",num1)
except Exception as error:
    print("Error occured", error)
else:
    print("else blocked occured")
finally:
    print("finally block occured")
print("hii")
print("hii")


#example with no error
print("hii")
print("hii")
try:
    print("hii")
except Exception as error:
    print("Error occured", error)
else:
    print("else blocked occured")
finally:
    print("finally block occured")
print("hii")
print("hii")

#yeh sab kaam tab karna hhy agar for example kaam apki python sy bahir horaha hy like files kahien
#download karwarahy ho ya kuch karahy ho like programming karo gy toh smaja