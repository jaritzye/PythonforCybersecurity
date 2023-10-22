
#!/usr/bin/env python3
# By Jaritzy Esquivel
# date: 10/15/23

#Function HW: New function
def send_message(message, times):
    for _ in range (times):
        print (message)

#Ask if user is having a good day
user_input= input("Is today a good day? (y/n)  ")


if user_input.lower() == "y":
    send_message("Yeah it is",10)

