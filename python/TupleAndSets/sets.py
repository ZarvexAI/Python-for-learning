#Sets
useremaillist=["asim@gamil.com","zuhaib@gmail.com","asim@gmail.com"]
useremailsets={"asim@gmail.com","zuhaib@gmail.com","asim@gmail.com"}
print("list",useremaillist)
print("set",useremailsets)
#set mn kabhi duplication ni ati 
nums={20,30,20,40,54,33,30}
print(nums)#duplication khatam hogya
#sets mn indexing system ni ata bcs sab values jo sets mn hn toh woh sab unique hn aur sets mn order khaarab hojata hy

#what if we want to add new value to set sirf 1 value dy sakty hn at a single time
useremailsets.add("minahil@gmail.com")
print(useremailsets)
#agar koi aissi cheez  add karwarahy ho joo pehly hi set mn hoo toh ni karega cuz sets unique value ralhty hn
useremailsets.add("zuhaib@gmail.com")
print(useremailsets)
#see zuhaib@gmail.com add ni kiya

useremailsets.remove("asim@gmail.com")
print(useremailsets)#agar remove function mn jo value apny usy di wo set naho toh yeh error deta hy

useremailsets.update(["ali@gmail.com","usman@gmail.com"])
print(useremailsets)#add function aik time py aik value add karta hy update  more than one values 

useremailsets.discard("ali@gmail.com")
print(useremailsets)#yeh value delete karta hy par agar jo value pass ki hy wo set mn na ho toh yeh error ni deta but program chlta rehta
useremailsets.discard("sadaqat@gmail.com")
print(useremailsets)#see no error