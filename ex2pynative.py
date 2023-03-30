# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(11):
    if (i == 0):
        print(i, i)
    else:
        print(i, i + numbers[i-1])
