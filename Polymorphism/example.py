#it refers to use of a single type entity 
#to represent different type in different scenarios
#polymorphism refers to many forms poly mean many and morphism mean forms

from Item import Item


class Keyboard(Item):
    pay_rate = 0.7
    def __init__(self, name: str, price: float, quantity=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )