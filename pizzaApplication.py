import tkinter as tk
#from PIL import ImageTk, Image

class PizzaApplication:
    def __init__(self, master):
        self.master = master
        master.title("Pizza Application")

        # Define pizza sizes
        self.sizes = {
            "Small": 6.99,
            "Medium": 9.99,
            "Large": 12.99
        }

        # Define pizza toppings and prices
        self.toppings = {
            "Pepperoni": 1.50,
            "Mushrooms": 1.00,
            "Onions": 0.75,
            "Sausage": 1.50,
            "Bacon": 2.00
        }

        # Define pizza crusts
        self.crusts = {
            "Thin Crust": 0.50,
            "Thick Crust": 1.00,
            "Stuffed Crust": 2.00
        }

        # Create widgets
        self.size_label = tk.Label(master, text="Select Pizza Size:")
        self.size_label.grid(row=0, column=0, padx=5, pady=5)

        self.size_var = tk.StringVar()
        self.size_var.set("Medium")
        for i, size in enumerate(self.sizes.keys()):
            size_radio = tk.Radiobutton(master, text=size, variable=self.size_var, value=size)
            size_radio.grid(row=i+1, column=0, padx=5, pady=5)

        self.toppings_label = tk.Label(master, text="Select Toppings:")
        self.toppings_label.grid(row=0, column=1, padx=5, pady=5)

        self.toppings_vars = {topping: tk.BooleanVar() for topping in self.toppings.keys()}
        for i, topping in enumerate(self.toppings.keys()):
            topping_checkbox = tk.Checkbutton(master, text=topping, variable=self.toppings_vars[topping])
            topping_checkbox.grid(row=i+1, column=1, padx=5, pady=5)

        self.crust_label = tk.Label(master, text="Select Crust Type:")
        self.crust_label.grid(row=0, column=2, padx=5, pady=5)

        self.crust_var = tk.StringVar()
        self.crust_var.set("Thin Crust")
        for i, crust in enumerate(self.crusts.keys()):
            crust_radio = tk.Radiobutton(master, text=crust, variable=self.crust_var, value=crust)
            crust_radio.grid(row=i+1, column=2, padx=5, pady=5)

        self.name_label = tk.Label(master, text="Enter Your Name:")
        self.name_label.grid(row=4, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=4, column=1, padx=5, pady=5)

        #self.image = Image.open("pizza.png")
        #self.image = self.image.resize((200, 200))
        #self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(master, image=self.photo)
        self.image_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.total_label = tk.Label(master, text="Total Price: $0.00")
        self.total_label.grid(row=6, column=0, columnspan=3, padx=5, pady=5)
