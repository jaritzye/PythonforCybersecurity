#!/usr/bin/env python3
# HackMe.Txt HW
# By Jaritzy Esquivel
# 10/22/23

#questions to ask user

questions = {}

questions['Name'] = input("What is your name? ")
questions['Color'] = input("What is your favorite color? ")
questions['Pet'] = input("What is your first pet's name? ")
questions['Mom'] = input("What is your mother's maiden name? ")
questions['school'] = input("What elementary school did you attend? ")


# Write lines to the file
with open("hackme.txt", "w") as file:
    for key , value in questions.items():
        file.write(f"{key}: {value}\n")

#confirmation
print("Information stored in hackme.txt")

#Read file
with open("hackme.txt", "r") as file:
    file_contents =  file.read()


print("Here is someone to hack- information")


#Print the information from hackme.txt
print(file_contents)

