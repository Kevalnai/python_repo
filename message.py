import tkinter as tk
from tkinter import messagebox

# Define a function to display a message box
def display_message():
    messagebox.showinfo("Message Box", "Hello, this is a message box!")

# Create a window
root = tk.Tk()

# Create a button and attach the display_message function to it
button = tk.Button(root, text="Click me!", command=display_message)
button.pack()

# Start the main event loop
root.mainloop()
