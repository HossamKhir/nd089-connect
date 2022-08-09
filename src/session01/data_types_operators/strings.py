#! /usr/bin/env python3
"""exercise on strings
"""

var = "Udacity has great content"
quote = "I'm become death, destroyer of worlds"
quote = 'I\'m become death, destroyer of worlds'
# POSIX
quote = 'He said "hi"'

var3= 'Udacity has great content'
var2 = """I can type
on different\tlines
and I don't care\n 
about "quotation marks"
"""
print(var2)
# indexing
print(var[0], var[2])
# slicing
start = 0
end = 6
print(var[start:end+1]) 
# NOTE in indexing, end is not inclusive, but start is
print(var[:7])
# temp = var[:]
# print(temp is var)

print(len(var))

print(type(var))
print(type(__name__) == str)
print(type(__name__) == type(""))
print(type(24))
print(type(2+3j))

# NOTE string methods
print(var3.split())
print(var.lower())
print(var.upper())
print(var.isalnum())
print("Q24".isalnum())
print("var".isalpha())