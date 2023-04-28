from tkinter import *

# Create the main window
root = Tk()
root.title("Pizza Order")

# Set the window size
root.geometry("400x400")

# Define a function to handle the order button click
def order():
    # Get the values from the input fields
    size = size_var.get()
    toppings = toppings_var.get()

    # Create the order summary
    order_summary = f"You ordered a {size} pizza with {toppings}."

    # Display the order summary
    summary_label.config(text=order_summary)

# Create the size label and input field
size_label = Label(root, text="Pizza size:")
size_label.pack()
size_var = StringVar()
size_var.set("Medium")
size_options = ["Small", "Medium", "Large"]
size_menu = OptionMenu(root, size_var, *size_options)
size_menu.pack()

# Create the toppings label and input field
toppings_label = Label(root, text="Toppings:")
toppings_label.pack()
toppings_var = StringVar()
toppings_var.set("Cheese")
toppings_entry = Entry(root, textvariable=toppings_var)
toppings_entry.pack()

# Create the order button
order_button = Button(root, text="Order", command=order)
order_button.pack()

# Create the order summary label
summary_label = Label(root, text="")
summary_label.pack()

# Start the main loop
root.mainloop()
