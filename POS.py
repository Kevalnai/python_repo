import tkinter as tk
root = tk.Tk()
root.title("pizza ordering system")

var1=tk.Button(text="submit",bg="black",fg="white")
var1.pack()


size_var = tk.StringVar(value="Medium")
toppings = {
            "Pepperoni": tk.BooleanVar(value=True),
            "Mushrooms": tk.BooleanVar(value=False),
            "Onions": tk.BooleanVar(value=False),
            "Sausage": tk.BooleanVar(value=False),
            "Bacon": tk.BooleanVar(value=False)
        }
order_total = 0

        # Create widgets
size_label = tk.Label( text="Size:")
size_label.grid(row=0, column=0, padx=5, pady=5)
size_dropdown = tk.OptionMenu(size_var, "Small", "Medium", "Large")
size_dropdown.grid(row=0, column=1, padx=5, pady=5)

toppings_label = tk.Label( text="Toppings:")
toppings_label.grid(row=1, column=0, padx=5, pady=5)
pepperoni_checkbox = tk.Checkbutton( text="Pepperoni")
pepperoni_checkbox.grid(row=1, column=1, sticky="W")
mushrooms_checkbox = tk.Checkbutton( text="Mushrooms")
mushrooms_checkbox.grid(row=2, column=1, sticky="W")
onions_checkbox = tk.Checkbutton( text="Onions")
onions_checkbox.grid(row=3, column=1, sticky="W")
sausage_checkbox = tk.Checkbutton( text="Sausage")
sausage_checkbox.grid(row=4, column=1, sticky="W")
bacon_checkbox = tk.Checkbutton( text="Bacon")
bacon_checkbox.grid(row=5, column=1, sticky="W")

calculate_button = tk.Button( text="Calculate Total")
calculate_button.grid(row=6, column=0, padx=5, pady=5)

total_label = tk.Label( text=f"Order Total: ${order_total:.2f}")
total_label.grid(row=6, column=1, padx=5, pady=5)


root.mainloop()