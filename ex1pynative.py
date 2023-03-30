# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

if (x * y <= 1000):
    print("The product of x and y is", x * y)
else:
    print("The sum of x and y is", x + y)
