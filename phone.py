from item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity= 0, broken_phones= 0):
        # Run validations to the received arguments
        # Call super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        ) 
        
        assert broken_phones >= 0, f"Brokenphones {broken_phones} is not greater than or equal to zero!"
        
        # Assign to self object
        # Instance attributes/ variables
        
        self.quantity = quantity

        # Actions to execute

