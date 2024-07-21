from item import Item

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