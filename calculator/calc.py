#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a basic calculator that can do four operations; addition, subtraction, summation and division.
"""

def addition(a, b):
    """ Addition Operator """
    return a + b

def subtraction(a, b):
    """ Subtraction Operator """
    return a - b

def summation(a, b):
    """ Summation Operator """
    return a * b

def division(a, b):
    """ Division Operator """
    if b == 0:
        raise ValueError("Divison by Zero!")
    return a / b
