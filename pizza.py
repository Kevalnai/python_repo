import tkinter as tk

class PizzaOrderingSystem:
    def __init__(self, master):
        self.master = master
        master.title("Pizza Ordering System")
        self.size_var = tk.StringVar(value="Medium")
        self.toppings = {
            "Pepperoni": tk.BooleanVar(value=False),
            "Mushrooms": tk.BooleanVar(value=False),
            "Onions": tk.BooleanVar(value=False),
            "Sausage": tk.BooleanVar(value=False),
            "Bacon": tk.BooleanVar(value=False)
        }
        self.order_total = 0

        # Create widgets
        self.size_label = tk.Label(master, text="Size:")
        self.size_label.grid(row=0, column=0, padx=5, pady=5)
        self.size_dropdown = tk.OptionMenu(master, self.size_var, "Small", "Medium", "Large")
        self.size_dropdown.grid(row=0, column=1, padx=5, pady=5)

        self.toppings_label = tk.Label(master, text="Toppings:")
        self.toppings_label.grid(row=1, column=0, padx=5, pady=5)
        self.pepperoni_checkbox = tk.Checkbutton(master, text="Pepperoni", variable=self.toppings["Pepperoni"])
        self.pepperoni_checkbox.grid(row=1, column=1, sticky="W")
        self.mushrooms_checkbox = tk.Checkbutton(master, text="Mushrooms", variable=self.toppings["Mushrooms"])
        self.mushrooms_checkbox.grid(row=2, column=1, sticky="W")
        self.onions_checkbox = tk.Checkbutton(master, text="Onions", variable=self.toppings["Onions"])
        self.onions_checkbox.grid(row=3, column=1, sticky="W")
        self.sausage_checkbox = tk.Checkbutton(master, text="Sausage", variable=self.toppings["Sausage"])
        self.sausage_checkbox.grid(row=4, column=1, sticky="W")
        self.bacon_checkbox = tk.Checkbutton(master, text="Bacon", variable=self.toppings["Bacon"])
        self.bacon_checkbox.grid(row=5, column=1, sticky="W")

        self.calculate_button = tk.Button(master, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=6, column=0, padx=5, pady=5)

        self.total_label = tk.Label(master, text=f"Order Total: ${self.order_total:.2f}")
        self.total_label.grid(row=6, column=1, padx=5, pady=5)

    def calculate_total(self):
        # Calculate the order total based on size and toppings
        prices = {"Small": 5.99, "Medium": 7.99, "Large": 9.99}
        size_price = prices[self.size_var.get()]
        topping_price = sum([1.50 for topping in self.toppings.values() if topping.get()])
        self.order_total = size_price + topping_price

        # Update the order total label
        self.total_label.config(text=f"Order Total: ${self.order_total:.2f}")

root = tk.Tk()
pizza_ordering_system = PizzaOrderingSystem(root)
root.mainloop()
