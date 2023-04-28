from tkinter import *

root = Tk()
#gui logic
#width x hieght
#root.geometry("800x1200")
root.title("Pizza orders")
#width,height
'''
root.minsize(100,100)
root.maxsize(750,750)
'''
#imp label operation
'''
text = add text
bd = backgroung
fg = foreground
font = ses the font
padx = x padding
pady = y padding
refief = border stylig = SUNKEN , RAISED, GROOVE, RIDGE
'''
title_label = Label(text="select your order",bg="red",fg="blue",padx ="25",pady="45",font=("comicsansns",20,"bold"),borderwidth=5,relief=GROOVE)
title_label.pack(side=TOP,fill=X)

#imp pack options
'''
anchor
side = top,bottom,left,right
fill
padx
pady
'''
order = Label(text="i am a good boy")
order.pack(anchor ="nw")
'''
photo = PhotoImage(file="1.png.PNG")
pic = Label(image=photo)
pic.pack()
'''
f1= Frame(root,bg="grey",borderwidth=10,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
l=Label(f1,text="HEllo worLd")
l.pack(pady=150)
root.mainloop()

