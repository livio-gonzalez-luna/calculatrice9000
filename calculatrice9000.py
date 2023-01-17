# Scientific buttons: function sc
# Number and mathematical buttons: function click
# Equal button: function evaluate
# Backspace button: function bksps
# Clear button: function clear

from tkinter import *
import math as m

root = Tk()
root.title("Scientific Calculator")
l=Label(root,text="This is a label", bg="lightgreen")
e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

def click(to_print):
    old=e.get()
    e.delete(0, END)
    e.insert(0, old+to_print)

def sc(event): # event catches whatever your action need to perform 
    key=event.widget # widget get the button
    text=key["text"] # Need it in text
    no=e.get()
    result=""
    if text=="deg":
        result=str(m.degrees(float(no)))
    if text=="sin":
        result=str(m.sin(float(no)))
    if text=="cos":
        result=str(m.cos(float(no)))
    if text=="tan":
        result=str(m.tan(float(no)))
    if text=="lg":
        result=str(m.log10(float(no)))
    if text=="ln":
        result=str(m.log(float(no)))
    if text=="Sqrt":
        result==str(m.sqrt(float(no)))
    if text=="x!":
        result=str(m.factorial(float(no)))
    if text=="1/x":
        result=str(1/(float(no)))
    if text=="pi":
        if no=="":
            result=str(m.pi)
        else:
            result=str(float(no) * m.pi)
    if text=="e":
        if no=="":
            result=str(m.e)
        else:
            result=str(m.e**float(no))
    
    e.delete(0, END)
    e.insert(0, END)

def clear():
    e.delete(0, END)
    return

def bksps():
    current=e.get()
    length=len(current)-1
    e.delete(length, END)

def evaluate():
    ans=e.get()
    ans=eval(ans) #fonction eval to be explained
    e.delete(0, END)
    e.insert(0, ans)

lg = Button(root, text="lg", padx=27, pady=10, relief=RAISED, bg="Black", fg="White")
lg.bind("<Button-1>", sc)
ln = Button(root, text="ln", padx=27, pady=10, relief=RAISED, bg="Black", fg="White")
ln.bind("<Button-1>", sc)

div = Button(root, text="/", padx=29, pady=10, relief=RAISED)

dot = Button(root, text=".", padx=27, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("."))
bksp = Button(root, text="Bksp", padx=27, pady=10, relief=RAISED, bg="Red", fg="White", command=bksps)

zero = Button(root, text="0", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("0"))
one = Button(root, text="1", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("1"))
two = Button(root, text="2", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("2"))
three = Button(root, text="3", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("3"))
four = Button(root, text="4", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("4"))
five = Button(root, text="5", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("5"))
six = Button(root, text="6", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("6"))
seven = Button(root, text="7", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("7"))
eight = Button(root, text="8", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("8"))
nine = Button(root, text="9", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("9"))

lg.grid(row=1, column=0)
ln.grid(row=1, column=1)
# par1nd.grid(row=1, column=2)
# par2nd.grid(row=1, column=3)
div.grid(row=3, column=4)
dot.grid(row=1, column=4)

# exp.grid(row=2, column=0)
# degb.grid(row=2, column=1)
# sinb.grid(row=2, column=2)
# cosb.grid(row=2, column=3)
# tanb.grid(row=2, column=4)

# sqrtm.grid(row=3, column=0)
# ac.grid(row=3, column=1)
bksp.grid(row=3, column=2)
# mod.grid(row=3, column=3)
# div.grid(row=3, column=4)

zero.grid(row=7, column=2)
one.grid(row=6, column=1)
two.grid(row=6, column=2)
three.grid(row=6, column=3)
four.grid(row=5, column=1)
five.grid(row=5, column=2)
six.grid(row=5, column=3)
seven.grid(row=4, column=1)
eight.grid(row=4, column=2)
nine.grid(row=4, column=3)

# fact.grid(row=4, column=0)
# mult.grid(row=4, column=4)

# frac.grid(row=5, column=0)
# minus.grid(row=5, column=4)
# plus.grid(row=6, column=4)

# e_b.grid(row=7, column=1)
# equal.grid(row=7, column=3)

root.mainloop()
