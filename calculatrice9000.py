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
e = Entry(root, width=40, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

def click(to_print):
    old=e.get()
    e.delete(0, END)
    e.insert(0, old+to_print)

def sqrt():
    sq=e.get()
    sq=float(sq)
    if sq < 0:
        raise ValueError("Cannot compute square root of negative number {0}".format(sq))
    guess = sq
    i = 0
    while abs(guess*guess - sq) > 1e-10 and i < 20:
        guess = (guess + sq/guess) / 2
        i += 1
    return guess

def sc(event): # event catches whatever your action need to perform 
    key=event.widget # widget get the button
    text=key["text"] # Need it in text
    no=e.get()
    result=""
    if text=="sqrt":
        result=sqrt(float(no))
        if result.imag == 0:
            result = str(result.real)
            e.delete(0, END)
            e.insert(0, result)
        else:
            result=str(result)
            e.delete(0, END)
            e.insert(0, result)
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
    e.insert(0, result)

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



# lg = Button(root, text="lg", padx=27, pady=10, relief=RAISED, bg="Black", fg="White")
# lg.bind("<Button-1>", sc)
# ln = Button(root, text="ln", padx=27, pady=10, relief=RAISED, bg="Black", fg="White")
# ln.bind("<Button-1>", sc)
pi = Button(root, text="π", padx=27, pady=10, relief=RAISED, bg="Black", fg="White")
pi.bind("Button1-1", sc)

sqrtm = Button(root,text="sqrt", padx=27, pady=10, relief=RAISED, bg="Black", fg="White", command=sqrt)
sqrtm.bind("Button1-1", sc)

# Simple signs
plus = Button(root, text="+", padx=27, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("+"))
minus = Button(root, text="-", padx=28, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("-"))
div = Button(root, text="/", padx=27, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("/"))
mult = Button(root, text="x", padx=27, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("*"))
equal = Button(root, text="=", padx=27, pady=10, relief=RAISED, bg="Orange", fg="White", command=evaluate)
# Syntax
dot = Button(root, text=".", padx=30, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("."))
bksp = Button(root, text="⌫", padx=17, pady=10, relief=RAISED, bg="Red", fg="White", command=bksps)
cls = Button(root, text="C", padx=27, pady=10, relief=RAISED, bg="Red", fg="White", command=clear)
negate = Button(root, text="+/-", padx=21, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("-"))
# Numbers
zero = Button(root, text="0", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("0"))
one = Button(root, text="1", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("1"))
two = Button(root, text="2", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("2"))
three = Button(root, text="3", padx=28, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("3"))
four = Button(root, text="4", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("4"))
five = Button(root, text="5", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("5"))
six = Button(root, text="6", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("6"))
seven = Button(root, text="7", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("7"))
eight = Button(root, text="8", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("8"))
nine = Button(root, text="9", padx=27, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("9"))

zero.grid(row=7, column=1)
one.grid(row=6, column=0)
two.grid(row=6, column=1)
three.grid(row=6, column=2)
four.grid(row=5, column=0)
five.grid(row=5, column=1)
six.grid(row=5, column=2)
seven.grid(row=4, column=0)
eight.grid(row=4, column=1)
nine.grid(row=4, column=2)

# pi.grid(row=3, column=1)
div.grid(row=3, column=3)
mult.grid(row=4, column=3)
minus.grid(row=5, column=3)
plus.grid(row=6, column=3)
equal.grid(row=7, column=3)

dot.grid(row=7, column=2)
bksp.grid(row=2, column=3)
cls.grid(row=2, column=2)
negate.grid(row=7, column=0)

# lg.grid(row=1, column=0)
# ln.grid(row=1, column=1)
# sinb.grid(row=2, column=2)
# cosb.grid(row=2, column=3)
# tanb.grid(row=2, column=4)
sqrtm.grid(row=3, column=2)
# fact.grid(row=4, column=0)
# frac.grid(row=5, column=0)
# e_b.grid(row=7, column=1)
root.mainloop()
