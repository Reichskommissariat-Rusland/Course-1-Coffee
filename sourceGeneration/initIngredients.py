#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ingredient initialization.
    
    Date: 2022-04-25
    Version: 1.0
"""

# Initialize the ingredients, for the convenience, we only use three ingredients: Water, milk and coffee.


def initializeIngredients():
    """Initialize the ingredients for the coffee machine.
    """
    print("Initialization for the ingredients")

    water = int(input("Enter water amount: "))
    milk = int(input("Enter milk amount: "))
    coffee = int(input("Enter coffee amount: "))

    ingredients = {'Water': water, 'Milk': milk, 'Coffee': coffee}

    # Write the output to the file.
    with open('./ingredients.txt', 'w') as ingredientsFile:
        ingredientsFile.write(str(ingredients))


if __name__ == '__main__':
    initializeIngredients()
