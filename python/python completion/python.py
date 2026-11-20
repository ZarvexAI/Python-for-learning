class Laptops:
    def __init__(self,size,color,gen,price):
        self.size=size
        self.color=color
        self.gen= gen
        self.__price=price


    def price(self):
        return self.__price

    def Email(self,mail):
        self.email="mail"


    
lap=Laptops("14inch","silver","12th","70,000")
print(lap)
output=(lap.price())
print(output)
