import tkinter as tk
from tkinter import messagebox

# this is the main script for the group project






class Admin:
    pass
class Volunteer:
    pass
class Refugee:
    pass

def LogIn():
    messagebox.showinfo("Log In:", "Log In Instructions")

def New_Account():
    messagebox.showinfo("Create Account:","New Account Instructions")

#Create window
root = tk.Tk()
root.title("Welcome to your Camp Management Interface")
#Create widgets
label=tk.Label(root, text="What would you like to do?")
label.pack(pady=10)
button1=tk.Button(root, text="Log In",command=LogIn)
button1.pack(pady=5)
button2=tk.Button(root, text="Create Account",command=New_Account)
button2.pack(pady=5)

#Run Loop
root.mainloop()
