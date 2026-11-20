#list slicing
# print(usernamelist[1:3])end point sy aik ehly tak yani ali umar print hoga


#list mn data saving ky liye use hota hy
usernamelist=["hamza","ali","umar","ahmad"]
usernametuple=("hamza","ali","umar")
#list ki value mutable hy as in update hosakti hn 
#tuple mn value update ni karsakty
#new values add b ni karsakty
#value delete ni karsakty
#tuple mn data constant rkhty hn like birth date
usernamelist=["hamza","ali",("umar")]#We can also use tuple in list
print(usernamelist)
print(usernametuple)
usernamelist[0]="asim"
# usernametuple[0]="asim"
print(usernamelist)
print(usernametuple)#update ni hoga 0 index
#loop ka process b same hy in tuple
for item in usernametuple:
    print(item)
#2 build methods for tuple
#count function is also used in tuple
print(usernametuple.count("hamza"))
#index function can also be used in tuple
print(usernametuple.index("hamza"))
#unpacked tuple
#unpacked tuple means the values deefined in tuple us har value ko apni taraf sy
#variable dy sakty ho like index ki jag khud sy variables assign karsakty hn
usernametuple=("hamza","ali","umar")
# lets say i wanna give variables to these 3 values
usernametuple=("hamza","ali","umar")
name,name2,name3= usernametuple
name,name2,name3=("hamza","ali","umar")#aisy bhi hosakta hy
#tuple par range function use hosakta hy
nums=(10,20,30,40,50,60,70,80,90)
print(len(nums))
print(nums.count(30))
print(nums.index(30))

#Sets data structure
