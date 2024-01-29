'''
Author: Evelyn Zepeda
Date: 1/28/24
Title: zepeda.calculator.py
'''
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1-num2

def divide(num1, num2):
    return num1/num2

def multiply(num1, num2):
    return num1 * num2

x = 4
y = 4

a = 10
b = 6

c = 8
d = 2


print("The adding result is " + str(add(x,y)))
print("The subtraction result is " + str(subtract(a, b)))
print("The division result is " + str(divide(c, d)))
print("The multiplication result is " + str(multiply(a, d)))