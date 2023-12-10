# third tkinter script
# Get people in space

#Create a GUI Application - HW
#By Jaritzy Esquivel
#12/09/2023

# First tkinter script
# Add a button and command
# Create 

#Import tkinter
import tkinter
import requests

# Functions
def get_people_in_space():
    request_uri = "http://api.open-notify.org/astros.json"
    r = requests.get(request_uri)
    items =r.json()
    people_in_space = items["number"]
    tkinter.Label(my_window, text = people_in_space).pack()


# Create the GUI main window
my_window = tkinter.Tk()


# Add widgets
my_label = tkinter.Label(my_window, text = "People In Space", font = ("Arial Bold", 50))
my_label.pack()


my_button = tkinter.Button(my_window , text = "Click Here to Update", command = get_people_in_space) 
my_button.pack()


# Enter the main event loop
my_window.mainloop()