class Item:
    def __init__(self,name,price,quantity):
       self.name=name
       self.price=price
       self.quantity=quantity
       print(f"im created:{name}")
       
    def calculate_total_price(self):
        return self.price*self.quantity
    #functions inside classes called methods
item1=Item("phone",5,9)
print(item1.calculate_total_price())