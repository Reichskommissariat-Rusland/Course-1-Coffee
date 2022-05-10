#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Coupon generation.
    
    Date: 2022-04-25
    Version: 1.0
"""
import random
import string

# Here, for the convenience, we set the length of the Coupon as 8, with the combination of the letters and the numbers.


def generateCoupon():
    """Generate the coupon with the number you want.
    """

    couponNumber = int(input('Coupon Number: '))

    for index in range(0, couponNumber):
        # Generate the coupon with the length 8 and the combination of the letters and the numbers.
        coupon = ''.join(random.sample(
            string.ascii_letters + string.digits, 8))
        # Write the output to the file.
        with open('./coupon.txt', 'a') as couponFile:
            couponFile.write(str(coupon) + '\n')


if __name__ == '__main__':
    generateCoupon()
