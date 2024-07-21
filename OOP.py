class Item:
    pay_rate = 0.8
    def __init__(self, name: str, price: float, quantity= 0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
Item1 = Item("Phone", 100, 1)
Item2 = Item("Phone", 1000, 3)

Item1.apply_discount()
print(Item1.price)

Item2.pay_rate = 0.7 # This only affects the instance attribute and not all element by changing class attributes
Item2.pay_rate = 0.7
Item2.apply_discount()
print(Item2.price)
print(Item.__dict__) #All the attributes for Class level
print(Item1.__dict__) #All the attributes for Instance level