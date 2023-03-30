import csv
class Item:
    all = []
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
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader= csv.DictReader(f)
    #to make this a class method we need to use @classmethod before the
    #method itself and this method will take the class itself instead of the instance
    #we created this method as a class method instead of an instance method because we have the data 
    #the csv file so we dont have instanes here so we need to created as a class method
        
    def calculate_total_price(self):
        return self.price*self.quantity
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"
    #functions inside classes called methods

#we can do this because at first it will search at the instance level and because the instance dosnt have this value 
# it will assgin the value we have right now
print(Item.all)