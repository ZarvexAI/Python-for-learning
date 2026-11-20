#python mn built in modules hn jo use karsakty hn
import time
import datetime

#time module
print(time.time())#yeh aik function hy jis mn yeh wo time in milli second show karta hy jo 1970 1st 
#january sy lekar ab tak ka time in millisecond show kart hy
time.sleep(2)#yeh aik aisa function hy jo jab use hota hy toh yeh utny seconds ka delay deta hy jitna 
#ap parameters mn likhty ho 
print("hello world")#here hello world output mn show hoga after 2 seconds of line 3

#date time module
current_time= datetime.datetime.now()
print(current_time)
#yeh current date and time dega
#agar sirf date chaiye toh
print(current_time.date())
print(current_time.time())
