#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a basic calculator that can do four operations; addition, subtraction, summation and division.
"""

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def summation(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return ValueError("Divison by Zero!")
    return a / b
