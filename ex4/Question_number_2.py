"""--------------------------------------------------------

File: Question_number_2.py

Written by:
David Sapir, id = 208917351, login = davidsa
Shimson Polak, id = 315605642, login = shimshonpo

Program Description:
Two different (most appropriate) ways in which each product
will be tested whether it meets the condition and if so,
the updated price will be returned.

--------------------------------------------------------"""

from Product import *

new_product_list = list()
new_product_list.append(Product("Cucumber", 10, 5))
new_product_list.append(Product("Matzo", 5, 5))
new_product_list.append(Product("Cookies", 3, 5))
new_product_list.append(Product("Flour", 2, 5))
new_product_list.append(Product("Moo", 100, 5))


def my_generator(new_product_list):
    """ Return the next product when next is called. """
    for i in new_product_list:
        yield i


def check_product_discount(product) -> bool:
    """ Checks if the current product deserve discount
    according to the "Kosher Passover" """
    discount_code = set("Kosher Passover")
    counter = 0

    for i in discount_code:
        if i in product.name:
            counter += 1

        if counter >= 2:
            return True

    return False


def set_discount_generator():
    """ Sets discount using generator """
    global new_product_list

    return my_generator(new_product_list)


def set_discount_iterator():
    """ Sets discount using iterator. """
    global new_product_list

    return iter(new_product_list)


def update_product_price(product_list):
    """ Update the product given next value. """
    try:
        product_current = next(product_list)
        if check_product_discount(product_current):
            product_current.price = product_current.price * 0.95

    except StopIteration:
        # Catches the exception that is thrown when the
        # iteration on the object is completed.
        print("All products were checked.")


if __name__ == "__main__":
    product_list = set_discount_iterator()

    print("Examples: ")
    update_product_price(product_list)
    update_product_price(product_list)
    update_product_price(product_list)
    update_product_price(product_list)

    for i in new_product_list:
        print(i.price)