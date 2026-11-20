from user_data import sum

from user_data import username

#we can also import a bunch of things together
from list import admin, admin2

#we can also import full file but yeh memory leta hy isi liye bas needed data import karty hn
import list
#to access values from the imported file
print(list.admin)

#kya ho agar like ham user_data import karien aur jis file mn import kar rahy hn us mn pehly hi aik variable
#user_data ky name sy ban ho toh phir confusion ayega 
#is sy bachny ky liye han "as" ka keyword use karsakty hn toh change the name of file of user_data
#yeh name jo ham badal kar rakhien gy yeh sirf ussi file mn hi chal sakta hy jahan apny as ky sath change kiya hy
#agar changed name dusri file mn bhi use karogy toh ni chaly ga
import list as changedname
#to access function from this
print(changedname.admin)  

#Python modules
print("hello")
print(username)
#modules use hoty hn to use stuff from one file in another file
#all imports are to be done in top of program
#import cannot be done if the needed file is not saved
output=(sum(2,78))
print(output)
print(admin)
print(admin2)