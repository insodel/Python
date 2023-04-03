# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

userString = input("Input a string to work with: ")
i = 0

while i < len(userString):
    if (i % 2 == 0):
        print(userString[i])
        i = i + 1
    else:
        i = i + 1
