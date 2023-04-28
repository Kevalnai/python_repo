from tkinter import *
from tkinter import messagebox
def display_message():
    messagebox.showinfo("Message Box", "Your order is submited!")


root = Tk()
pr=Label(text="Welcome the the pizza shop",bg="red",fg="green")
pr.pack(fill=X)


root.title("Pizza Ordering System")
root.geometry("500x500")
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


button = Button(root, text="Submit", command=display_message).place(x=0,y=175)


photo = PhotoImage(file="pizza.png")
pic = Label(image=photo).place(x=0,y=225)
#pic.pack(side=LEFT,anchor="nw",fill=X)
root.mainloop()
