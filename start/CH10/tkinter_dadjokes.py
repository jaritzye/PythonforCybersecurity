#Create a GUI Application - HW
#By Jaritzy Esquivel
#12/09/2023

# Fourh tkinter script
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

def get_dadjoke():
    request_uri = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    r = requests.get(request_uri, headers = headers)
    items = r.json()
    joke = items["joke"]
    #tkinter.Label(my_window, text = joke).pack()
    my_label.configure(text = joke)


# Create the GUI main window
my_window = tkinter.Tk()


# Add widgets
my_label = tkinter.Label(my_window, text = "Get Dad Joke", font = ("Arial Bold", 25))
my_label.pack()


my_button = tkinter.Button(my_window , text = "Click Here to Get Dad Joke", command = get_dadjoke)
my_button.pack()


# Enter the main event loop
my_window.mainloop()