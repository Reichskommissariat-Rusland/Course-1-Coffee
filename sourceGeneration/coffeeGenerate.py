#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Coffee generation.

    Date: 2022-04-25
    Version: 1.0
"""

# Here, for the convenience, we only use three ingredients: Coffee, Water and the Milk.


def generateCoffee():
    """Generate the coffee with the information of the ingredients.
    """

    print("Coffee generating machine")

    coffeeName = input("Enter coffee name: ")

    if coffeeName == 'Quit':
        # Stop generating.
        print("Machine exiting...")
        exit()
    else:
        waterAmount = int(input("Enter water amount: "))
        milkAmount = int(input("Enter milk amount: "))
        coffeeAmount = int(input("Enter coffee amount: "))
        price = int(input("Enter price: "))

        coffeeInstance = {'Name': coffeeName, 'WaterAmount': waterAmount,
                          'MilkAmount': milkAmount, 'CoffeeAmount': coffeeAmount, 'Price': price}
        # Write the output to the file.
        with open('./coffee.txt', 'a') as coffeeFile:
            coffeeFile.write(str(coffeeInstance) + '\n')


if __name__ == '__main__':
    while(True):
        generateCoffee()
