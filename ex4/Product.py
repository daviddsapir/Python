"""--------------------------------------------------------

file: product.py

Written by:
David Sapir, id = 208917351, login = davidsa
Shimson Polak, id = 315605642, login = shimshonpo

Program Description:
Class Product.
The product has three private features: name, price and
quantity in stock.

--------------------------------------------------------"""


class Product:

    def __init__(self, name: str, price: int, quantity: int) -> None:
        """ Contractor sets the name, price and quantity. """
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @property
    def name(self) -> str:
        """ Returns the name. """
        return self.__name

    @property
    def quantity(self):
        """ Returns the quantity. """
        return self.quantity

    @quantity.setter
    def quantity(self, quantity):
        """ Sets the quantity. """
        self.quantity = int(quantity)
    
    @property
    def price(self):
        """ Returns the price. """
        return self.__price

    @price.setter
    def price(self, price):
        """ Sets the price. """
        self.__price = int(price)
