from tkinter import *

# Create the main window
root = Tk()
root.title("Pizza Ordering System")

# Create a pizza size radio button group
size_group = LabelFrame(root, text="Size")
size_group.pack(padx=10, pady=10)
size_var = StringVar()
Radiobutton(size_group, text="Small", variable=size_var, value="Small").pack(anchor=W)
Radiobutton(size_group, text="Medium", variable=size_var, value="Medium").pack(anchor=W)
Radiobutton(size_group, text="Large", variable=size_var, value="Large").pack(anchor=W)

# Create a toppings checkbox group
toppings_group = LabelFrame(root, text="Toppings")
toppings_group.pack(padx=10, pady=10)
pepperoni_var = BooleanVar()
Checkbutton(toppings_group, text="Pepperoni", variable=pepperoni_var).pack(anchor=W)
mushrooms_var = BooleanVar()
Checkbutton(toppings_group, text="Mushrooms", variable=mushrooms_var).pack(anchor=W)
olives_var = BooleanVar()
Checkbutton(toppings_group, text="Olives", variable=olives_var).pack(anchor=W)

# Create a delivery method radio button group
delivery_group = LabelFrame(root, text="Delivery Method")
delivery_group.pack(padx=10, pady=10)
delivery_var = StringVar()
Radiobutton(delivery_group, text="Delivery", variable=delivery_var, value="Delivery").pack(anchor=W)
Radiobutton(delivery_group, text="Pickup", variable=delivery_var, value="Pickup").pack(anchor=W)

# Create a submit button that displays the order summary
def submit():
    summary = "Order Summary:\n\nSize: {}\nToppings: ".format(size_var.get())
    if pepperoni_var.get():
        summary += "Pepperoni "
    if mushrooms_var.get():
        summary += "Mushrooms "
    if olives_var.get():
        summary += "Olives "
    summary += "\nDelivery Method: {}".format(delivery_var.get())
    messagebox.showinfo("Order Summary", summary)

Button(root, text="Submit", command=submit).pack(padx=10, pady=10)

# Run the main loop
root.mainloop()
