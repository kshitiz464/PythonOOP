import csv

class Item:
    pay_rate = 0.8
    all=[] 
    def __init__(self, name: str, price: float, quantity= 0):
        
        #Run Validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"
        
        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    @property
    def name(self):
        # return self._name #This single underscore makes it still accesible outside the class
       
        # This makes it completely unaccesible outside the class
        return self.__name 
        # return "Def name"
    @property
    def price(self):
        # return "Def price"
        return self.__price

    @name.setter
    def name(self, value):
        self.__name = value
        
        
    def calculate_total_price(self):
        return self.__price * self.quantity
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
    def apply_increment(self,factor):
        self.__price = self.__price +self.__price * factor
    
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
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})" #This will #return all the items in simple format(as when we created the instances) when we use Print#(Item.all)
# Item.instantiate_from_csv()
    def __connect(self,smtp_server):
        pass
    def __prepare_body(self):
        return f"""
    Hello Someone.
    We have {self.name} {self.quantity} times.
    Regards, ABCD
    """
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()