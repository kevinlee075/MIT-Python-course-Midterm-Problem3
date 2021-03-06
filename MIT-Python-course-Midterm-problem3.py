# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:17:24 2021

@author: Lenovo
"""

#Implement a function called closest_power that meets the specifications below.
#For example,
#closest_power(3,12) returns 2
#closest_power(4,12) returns 2
#closest_power(4,1) returns 0

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    expon = 0                                                                      #search the expon(exponent) from 0
    while base ** expon < num:                                                     #execute 'base^expon using while loop to find the closest int which is smaller than the num
        expon += 1
    if abs(num - base ** expon) >= abs(num - base ** (expon-1)):                   #after the loop, base^expon will be larger than num
        result = expon - 1                                                         #chech whether base^expon or base^(expon-1) is closer to num
    else:
        result = expon
    return result