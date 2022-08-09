#! /usr/bin/env python3
"""
exercises on strings
"""
import random

var1 = "Udacity is fun"
var2 = 'I am a string'
var3 = """I am a string,
and I don't care about new lines
or "quotations"
"""

oppenheimer = "I'm become death, destroyer of worlds"
opp = 'I\'m become death, destroyer of worlds'

doub = "I said \"Hello\""
print(var1)
print(var2)
print(var3)

# indexing
# to get y
print(var1[6])

# slicing
# get fun from var1
print(var1[-3:])

# get Udacity from var1
print(var1[0:7])
# the start index is inclusive
# the end index is exclusive
print(var1[:7])


print(var1[::2])
# collection[start:<end-1>:step]


# important functions
# TODO: length of var1
print(len(var1))

# TODO check the type of some literal
print(type(25))
print(type(3+2j)) # advanced

# print(help(len))
# print(help(random))

print(dir(var1))


# string methods
print(var1.split()[2])

var2 = "Udacity-is-fun"
print(var2.split("-")[2])

var2 = "Udacity\tis\nfun"
print(var2.split())

print(var1.upper())
print(var1.lower())
print(var1.title())

print(var1.find("i"))
print(var1.rfind("i")) # reverse find 
