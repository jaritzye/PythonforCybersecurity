#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created by Jaritzy on Oct 8

# Suggestion, build out 1 line at a time
# Once multiple print statemetns exist, put a breakpoint at first print line
# Then walk through as an example of "debugging"
#Ask user for the(ir name

user_name = input("What is your name? ")

#Print Hello and their name
print ("Hello {0}".format(user_name))
print (f"Hello {user_name}")
print ("Hello " + user_name)
print ("Hello", user_name)
message = "Hello " + user_name
print (message)


print (message + ", I am proud of you!")

age = input("How old are you? ")
age= int(age)

aged = age + 2
print (f"In two years you will be {aged} years old!")


