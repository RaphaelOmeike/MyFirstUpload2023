import csv

class Item:
    # class variables
    pay_rate = 0.8 # The pay rate after 20% discount.
    all = []
    def __init__(self, name: str, price: float, quantity= 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        # Assign to self object
        # Instance attributes/ variables
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    @property
    def price(self):
        return self.__price

    @property # for working on attributes
    # Property Decorator = Read-Only-Attribute
    def name(self): # To get name
        print("You are trying to get")
        return self.__name
    @name.setter
    def name(self, value): # To set name
        print("You are trying to set")
        if len(value) > 10:
            raise Exception("The name is too long ")
        else:
            self.__name = value
    def calculate_total_price(self):
        return self.quantity * self.__price 
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    @classmethod # decorator
    def instantiate_from_csv(cls):
        with open("item.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Excludes numbers that are point zero.
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"
    def __send_email(self):
        pass
    # @property
    # def read_only_name(self):
    #     return "AAA"