import csv

class Item:
    pay_rate = 0.8
    all=[] 
    def __init__(self, name: str, price: float, quantity= 0):
        
        #Run Validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open("data.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader) 

        for item in items:
            Item(f"{item.get('name')}",float(item.get('price')),int(item.get('quantity')))
    
    @staticmethod
    #This counts off the float to integer who are decimals with only zero
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})" #This will return all the items in simple format(as when we created the instances) when we use Print(Item.all)

# Item1 = Item("Phone", 100, 1)
# Item2 = Item("Laptop", 1000, 3)
# Item3 = Item("Cable", 10, 5)
# Item4 = Item("Mouse", 50, 5)
# Item5 = Item("Keyboard", 75, 5)   Instead of all these lines, we will make a class method to instantiate using data from a csv file
# print(Item.all)

Item.instantiate_from_csv() #This class method creates instances from a external data source

print(Item.is_integer(5.0))

for instance in Item.all:
    print(instance) #This prints each instance.