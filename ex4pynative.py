# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.
# For example:
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.

def remove_chars(frase, charsTo):
    frase = frase[charsTo:]  
    print(frase)

string = input("Introduce a string: ")
charsToDel = int(input("Introduce the number of characters to delete: "))
remove_chars(string, charsToDel)
