#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Coffee machine.

    Date: 2022-04-25
    Version: 1.0
"""

import ast
import time


def initialization():
    """Initialize basic information for the machine from the external file.

    Returns:
        tuple: The basic information of the machine.
    """
    coffeeInformationList = []
    coffeeIngredientList = []
    couponInformationList = []

    with open('./coffee.txt', 'r') as coffeeFile:
        # Initialize the coffee from the external file.
        for line in coffeeFile.readlines():
            if line:
                # Avoid the empty line.
                coffeeInformationList.append(ast.literal_eval(line))

    with open('./coupon.txt', 'r') as couponFile:
        # Initialize the coupon from the external file.
        for line in couponFile.readlines():
            if line:
                # Avoid the empty line.
                couponInformationList.append(line.strip('\n'))

    with open('./ingredients.txt', 'r') as ingredientsFile:
        # Initialize the ingredients from the external file.
        for line in ingredientsFile.readlines():
            if line:
                # Avoid the empty line.
                coffeeIngredientList.append(ast.literal_eval(line))

    return coffeeInformationList, coffeeIngredientList, couponInformationList


def checkAbility(waterAmount, milkAmount, coffeeAmount, coffeeInformationList, selection):
    """Check the ability to produce the coffee.

    Args:
        waterAmount (int): Amount of water.
        milkAmount (int): Amount of milk.
        coffeeAmount (int): Amount of coffee.
        coffeeInformationList (list): List that contains the information of the coffee.
        selection (str): The selection of the user.

    Returns:
        bool: True if the coffee can be produced, otherwise False.
    """
    # Get the information of the coffee.
    coffeeInformation = coffeeInformationList[int(selection) - 1]

    # Check the ability to produce the coffee.
    if coffeeInformation['WaterAmount'] <= waterAmount and coffeeInformation['MilkAmount'] <= milkAmount and coffeeInformation['CoffeeAmount'] <= coffeeAmount:
        return True
    else:
        return False


def takeMoney():
    """Calculate the total money with the given amount, here we only consider the integer scenario.

    Returns:
        int: Total money.
    """

    amountOf20 = int(input('Amount of 20$ bills: '))
    amountOf10 = int(input('Amount of 10$ bills: '))
    amountOf5 = int(input('Amount of 5$ bills: '))
    amountOf1 = int(input('Amount of 1$ bills: '))

    totalMoney = amountOf20 * 20 + amountOf10 * 10 + amountOf5 * 5 + amountOf1 * 1

    return totalMoney


def menu(coffeeInformationList):
    """Display the information on the menu and take the selection from the user.

    Args:
        coffeeInformationList (list): List that contains the information of the coffee.

    Returns:
        str: The selection of the user.
    """
    print('*************************************************************')
    print('**             Welcome to the Coffee Machine!              **')
    print('*************************************************************')
    for i in range(0, len(coffeeInformationList)):
        print('{0}. {1} [Water: {2}ml; Milk: {3}ml; Coffee: {4}ml]: {5}$'.format(i + 1, coffeeInformationList[i]['Name'], coffeeInformationList[i]
                                                                                 ['WaterAmount'], coffeeInformationList[i]['MilkAmount'], coffeeInformationList[i]['CoffeeAmount'], coffeeInformationList[i]['Price']))
    print('Quit [Q\q]')
    print('*************************************************************')

    # Get the user selection.
    selection = input('$ Please select your item: ')

    return selection


def main():
    """The main function, that is the entry point of the program.
    """

    # Initialize the machine.
    coffeeInformationList, coffeeIngredientList, couponInformationList = initialization()

    waterAmount = coffeeIngredientList[0]['Water']
    milkAmount = coffeeIngredientList[0]['Milk']
    coffeeAmount = coffeeIngredientList[0]['Coffee']

    discount = 0.8

    # Set the quit flag.
    quitFlag = False

    # This dictionary contains the sold amount of the coffee and the total price.
    businessInformation = {}

    for index in range(0, len(coffeeInformationList)):
        businessInformation[coffeeInformationList[index]['Name']] = 0

    businessInformation['Total Profile'] = 0

    while not quitFlag:

        selection = menu(coffeeInformationList)

        if selection == 'Q' or selection == 'q':
            # Quit the machine.
            print("Thanks for using, quitting...")
            quitFlag = True
        else:
            # Check whether this item is available.
            while int(selection) > len(coffeeInformationList):
                print("Please select a valid item.")
                selection = menu(coffeeInformationList)
            print('Checking the ability to produce this item...')

            # Check whether this item can be produced.
            ability = checkAbility(
                waterAmount, milkAmount, coffeeAmount, coffeeInformationList, selection)

            while not ability:
                print("Sorry, we don't have enough ingredients to produce this item.")
                selection = menu(coffeeInformationList)
                while int(selection) > len(coffeeInformationList):
                    print("Please select a valid item.")
                    selection = menu(coffeeInformationList)

                print('Checking the ability to produce this item...')

                ability = checkAbility(
                    waterAmount, milkAmount, coffeeAmount, coffeeInformationList, selection)

            # Here, the coffee can be produced.
            confirm = input(
                'Good, this item can be produced, press "c" to continue:')
            while confirm != 'c' and confirm != 'C':
                confirm = input('Please enter "c" to continue:')

            # Determine the price, for the next step of discout.
            currentPrice = coffeeInformationList[int(selection) - 1]['Price']

            # The step to check whether the user has a coupon.
            haveCoupon = input('Do you have a coupon? [Y/N]: ')
            while haveCoupon != 'Y' and haveCoupon != 'y' and haveCoupon != 'N' and haveCoupon != 'n':
                haveCoupon = input(
                    'Wrong operation, please enter the correct operation:')
            if haveCoupon == 'Y' or haveCoupon == 'y':
                # Check whether the coupon is valid.
                coupon = input('Please enter your coupon([Q\q] for quit): ')
                if coupon == 'Q' or coupon == 'q':
                    print('Sorry, there is no coupon.')
                else:
                    while coupon not in couponInformationList:
                        coupon = input('Please enter a valid coupon: ')

                    # Reduce the price.
                    currentPrice = coffeeInformationList[int(
                        selection) - 1]['Price'] * discount
                    print('Good, you have a coupon with {2}%% discount, the price of your item will be: {0} * 0.8 = {1}, enjoy!'.format(
                        coffeeInformationList[int(selection) - 1]['Price'], currentPrice, int(discount * 100)))

            # If no coupon is available, just continue to the payment step.
            totalPayment = 0
            print("Please enter your cash.")
            # While the money is not enough.
            while totalPayment < currentPrice:
                # Get the total payment.
                totalPayment += takeMoney()
                print('Total payment: {0}'.format(totalPayment))
                # Remind the user.
                if totalPayment < currentPrice:
                    print('This is not enough, please input more money.')

            # Calculate the change.
            print("Your change is {0}, please receipt it.".format(
                totalPayment - currentPrice))

            # Consume the ingredients.
            waterAmount -= coffeeInformationList[int(
                selection) - 1]['WaterAmount']
            milkAmount -= coffeeInformationList[int(
                selection) - 1]['MilkAmount']
            coffeeAmount -= coffeeInformationList[int(
                selection) - 1]['CoffeeAmount']

            # Produce the coffee.
            print('Your coffee is making:')
            print('................................................................')
            time.sleep(2)
            print('## Coffee prepared finished!')
            print('................................................................')
            time.sleep(2)
            print('## Coffee making finished!')
            print('................................................................')
            time.sleep(2)
            print('Coffee packaging finished!')

            print('Please take it carefully!')

            # Print the information of this business.

            # First, we update the information.
            businessInformation[coffeeInformationList[int(
                selection) - 1]['Name']] += 1
            businessInformation['Total Profile'] += currentPrice

            # Then, print it, and write it to the external log file.
            with open('./record.log', 'a') as f:
                for key, value in businessInformation.items():
                    if key == 'Total Profile':
                        print('###{0}: {1}'.format(key, value))
                        f.writelines('###{0}: {1}'.format(key, value) + '\n')
                    else:
                        print('#{0}: {1}'.format(key, value))
                        f.writelines('#{0}: {1}'.format(key, value) + '\n')


if __name__ == '__main__':
    main()
