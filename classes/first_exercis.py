class Item:
    pay_rate=0.8
    def __init__(self,name:str ,price: float,quantity=0):
       assert quantity>=0, f"quantity {quantity} is not greater than or equal to zero"
       assert price>=0, f"price {price} is not greater than or equal t zero"
       self.name=name
       self.price=price
       self.quantity=quantity
       Item.all.append(self)
       #for each instance is going to be created  is going to be filled
       # with the instances created below
       print(f"im created:{name}")
    def apply_discount(self):
        self.price=self.price*self.pay_rate
        #the pay_rate belongs to the item class itself you can either access
        # it from the class level or the instance level
    def calculate_total_price(self):
        return self.price*self.quantity
    #functions inside classes called methods
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)  
#we can do this because at first it will search at the instance level and because the instance dosnt have this value 
# it will assgin the value we have right now
for instance in Item.all:
    print(instance.name)