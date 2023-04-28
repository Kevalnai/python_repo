from tkinter import *
root = Tk()
def calculate_total():
    # Calculate the order total based on size and toppings
    prices = {"Small": 5.99, "Medium": 7.99, "Large": 9.99}
    size_price = prices[size_var.get()]
    topping_price = sum([1.50 for topping in toppings.values() if topping.get()])
    order_total = size_price + topping_price

    # Update the order total label
    #total_label.config(text=f"Order Total: ${order_total:.2f}")

root.title("Pizza Ordering System")
root.geometry("250x250")
size_var = StringVar(value="Medium")
order_total = 0


size=Label(text="Size:",padx="5",pady="5",borderwidth="3",relief=GROOVE).place(x=0,y=22)



var = IntVar()
R1 = Radiobutton(root,text="SMALL", variable=var, value=1).place(x=50,y=25)


R2 = Radiobutton(root,text="MEDIUM", variable=var, value=2).place(x=50,y=50)


R3 = Radiobutton(root,text="LARGE", variable=var, value=3).place(x=50,y=75)


toppings = {
            "Pepperoni": BooleanVar(value=True),
            "Mushrooms": BooleanVar(value=False),
            "Onions": BooleanVar(value=False),
            "Sausage": BooleanVar(value=False),
            "Bacon": BooleanVar(value=False)
        }
toppings_ = Label(root, text="Toppings:",padx="5",pady="5",borderwidth="3",relief=GROOVE).place(x=150,y=25)


p = Checkbutton(root,text="Pepperoni",variable=toppings["Pepperoni"]).place(x=225,y=50)
m = Checkbutton(root,text="Mushrooms",variable=toppings["Mushrooms"]).place(x=225,y=75)
o = Checkbutton(root,text="Onions",variable=toppings["Onions"]).place(x=225,y=100)
s = Checkbutton(root,text="Sausage",variable=toppings["Sausage"]).place(x=225,y=125)
b = Checkbutton(root,text="Bacon",variable=toppings["Bacon"]).place(x=225,y=25)
'''
p.pack()
m.pack()
o.pack()
s.pack()
b.pack()
'''


calculate = Button(root, text="Calculate Total", command=calculate_total()).place(x=0,y=175)

total = Label(root, text=f"Order Total: ${order_total:.2f}").place(x=95,y=177)




        


root.mainloop()
