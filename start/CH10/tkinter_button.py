# Seconder tkinter script
# Add a button and command
#Create a GUI Application - HW
#By Jaritzy Esquivel
#12/09/2023


#Import tkinter
import tkinter
from tkinter import messagebox

# Functions

# Create the GUI main window
my_window = tkinter.Tk()

#Functions
def button_clicked():
    tkinter.Label(my_window, text = "Button was clicked").pack()
    messagebox.showerror("Error", "Don't click that")

# Add widgets
my_label = tkinter.Label(my_window, text = "Hello World", font = ("Arial Bold", 50))
my_label.pack()


my_button = tkinter.Button(my_window , text = "Click Here", command = button_clicked) 
my_button.pack()


# Enter the main event loop
my_window.mainloop()