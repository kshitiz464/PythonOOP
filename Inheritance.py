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
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})" #This will return all the items in simple format(as when we created the instances) when we use Print(Item.all)

class Phone(Item):
    def __init__(self,name:str,price:float,quantity=0, broken_phones=0):
        # Call to Super function to have access to all attributes from parent class
        super().__init__(
            name,price,quantity
        )
        #Run Validations to received arguments
        assert broken_phones > 0, f"Broken_phones {broken_phones} is not greater than zero"

        # Assign to self object
        self.broken_phones = broken_phones

phone1 = Phone("JscPhonev10",5000,5,1)       
print(Phone.all)
print(Item.all)
# print(Item.is_integer(5.0))

# for instance in Item.all:
#     print(instance) #This prints each instance.