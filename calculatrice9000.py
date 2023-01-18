from tkinter import *

# Create a Tkinter window and set the title and geometry
screen = Tk()
screen.title=("Calculator 9000")
screen.geometry("380x447") 

# Create a global variable to store the input string
input = ""

# Create a StringVar to store the output 
output = StringVar()

# Create a list to store the history of calculations
history = []
# Create a global variable to store the current calculation
current_calculation = ""

# Function to handle button clicks
def click(b):
    global input, current_calculation
    current_calculation += b
    if b == '^':
        input += '**'
    else:
        input += b
    output.set(input)

# Function to handle the '=' button
def equals():
    global input, current_calculation
    try:
        if '^' in input:
            base, exponent = input.split("**")
            base, exponent = int(base), int(exponent)
            result = 1
            for _ in range(exponent):
                result *= base
        else:
            result = eval(input)
        input = str(result)
        output.set(result)
        history.append(current_calculation + " = " + str(result)) 
    except:
        output.set("Invalid input")
        input = ""

# Function to handle the clear button
def clear():
    global input
    input = ""
    output.set("")

# Function to handle the backspace button
def bksps():
    global input
    input = input[:-1]
    output.set(input)

## History function
history_open = False

# Function to show the history of calculations
def show_history():
    global history_open, history_listbox
    if history_open:
        history_listbox.destroy()
        history_open = False
    else:
        history_listbox = Listbox(screen)
        history_listbox.place(x=10,y=300, width=360, height=120)
        for calculation in history:
            history_listbox.insert(END, calculation) # insert the full calculation
        history_open = True

# Clear the history of calculations
def clear_history():
    history.clear()

## Advanced calculator functions
# Function to calculate pi with a specified number of terms
n_terms = 1000
def calculate_pi(n_terms: int) -> float:
    pi = 0
    for i in range(n_terms):
        pi += 4 / (2*i+1) * (-1)**i
    return pi

# Function to calculate pi with a specified number of terms
def my_pi(n_terms:int = 1000, input_value: str = None) -> float:
    pi_approx = calculate_pi(n_terms)
    if input_value is None or input_value == "":
        return output.set(pi_approx)
    else:
        try:
            input_value = float(input_value)
            return output.set(input_value * pi_approx)
        except ValueError:
            return output.set("Invalid input")

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Function to calculate the factorial of a number
def factorial_button():
    global input
    try:
        input = int(input)
        if input >= 0:
            result = factorial(input)
            input = str(result)
            output.set(result)
        else:
            output.set("Invalid input")
            input = ""
    except:
        output.set("Invalid input")
        input = ""

# Function to convert degrees to radians
def to_radians(angle: float) -> float:
    pi = calculate_pi(1000)
    return angle * pi / 180

# Function to calculate the sine of an angle
def sin(x: float) -> float:
    try:
        x = float(x)
        x = to_radians(x)
        n_terms = 10
        result = x
        for i in range(1, n_terms):
            result += ((-1)**i) * (x**(2*i+1))/(factorial(2*i+1))
            output.set(result)
    except:
        output.set("Invalid input")
        input = ""

# Function to calculate the cosine of an angle
def cos(x: float) -> float:
    try:
        x = float(x)
        x = to_radians(x)
        n_terms = 10
        result = 1
        for i in range(1, n_terms):
            result += ((-1)**i) * (x**(2*i))/(factorial(2*i))
            output.set(result)
    except:
        output.set("Invalid input")
        input = ""

# Function to calculate the tangent of an angle
def tan(x: float) -> float:
    try:
        x = float(x)
        x = to_radians(x)
        result = sin(x) / cos(x)
        output.set(result)
    except:
        output.set("Invalid input")
        input=""

def power():
    global input
    try:
        # Split the input string on '^' to get the base and exponent
        base, exponent = input.split("^")
        # Use the ** operator to raise the base to the exponent
        result = float(base) ** float(exponent)
        input = str(result)
        output.set(result)
    except:
        output.set("Invalid input")
        input = ""

# Function to calculate the square root of a number
def sqrt():
    global input
    try:
        input = float(input)
        result = input**(1/2)
        input = str(result)
        output.set(result)
    except:
        output.set("Invalid input")
        input = ""

# Function to calculate the square of a number
def sqrd():
    global input
    try:
        input = float(input)
        result = input**2
        input = str(result)
        output.set(result)
    except:
        output.set("Invalid input")
        input = ""

# Function to calculate the natural logarithm of a number
def ln(x: float) -> float:
    try:
        x = float(x)
        if x <= 0:
            raise ValueError("Invalid input, x must be greater than 0")
        result = 0
        while x < 1:
            x += 1
            result -= 1
        while x > 2:
            x /= 2
            result += 1
        n = (x-1)/(x+1)
        result += (2*n)/(1 + n*n)
        return output.set(result)
    except:
        output.set("Invalid input")
        input = ""

# Function to calculate the factorial of a number
def inverse():
    global input
    try:
        input = float(input)
        if input != 0:
            result = 1/input
            input = str(result)
            output.set(result)
        else:
            output.set("Invalid input")
            input = ""
    except:
        output.set("Invalid input")
        input = ""

result = Entry(screen, bg="light gray", relief=RIDGE, border=4, font=("Sergoe UI", 20, "bold"), justify= "right", textvariable=output)
result.place(x=80, y=0, height=60, width=300)

# Buttons sizes = 64 x 77
## History buttons
# Show history button
history_button = Button(screen, text="History", relief=RAISED, activebackground="gray", activeforeground="dark gray" ,command=show_history)
history_button.place(x=0, y=0, height=32 ,width=80)
# Clear history button
clear_history_button = Button(screen, relief=RAISED, activebackground="gray", activeforeground="dark gray", text="Clear History", command=clear_history)
clear_history_button.place(x=0, y=32, height=32, width=80)


## First buttons row
# Sin button
bSin = Button(screen, bg="silver", text="sin",relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: sin(input))
bSin.place(x=0, y=60, height=77, width=64)
#Sqrt button
bRoot = Button(screen, bg="silver", text="√", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command = sqrt)
bRoot.place(x=64, y=60, height=77, width=64)
# ( button
bOpenBrace = Button(screen, bg="silver", text="(", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("("))
bOpenBrace.place(x=128, y=60, height=77, width=64)
# ) button
bCloseBrace = Button(screen, bg="silver", text=")", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click(")"))
bCloseBrace.place(x=192, y=60, height=77, width=64)
# / button
bDiv = Button(screen, bg="silver", text="÷", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("/"))
bDiv.place(x=256, y=60, height=77, width=64)
# pi button
bpi = Button(screen, bg="silver", text="π", relief=RAISED, border=3, font=("Sergoe UI", 13), activebackground="light gray", activeforeground="gray", command=lambda: my_pi(input_value=input))
bpi.place(x=320, y=60, height=77, width=64)


## Second buttons row
# Cos button
bCos = Button(screen, bg="silver", text="cos",relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: cos(input))
bCos.place(x=0, y=137, height=77, width=64)
# 7 button
b7 = Button(screen, text="7",relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("7"))
b7.place(x=64, y=137, height=77, width=64)
# 8 button
b8 = Button(screen, text="8", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("8"))
b8.place(x=128, y=137, height=77, width=64)
# 9 button
b9 = Button(screen, text="9", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("9"))
b9.place(x=192, y=137, height=77, width=64)
# * button
bMul = Button(screen, bg="silver", text="x", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("*"))
bMul.place(x=256, y=137, height=77, width=64)
# Backspace button
bBksps = Button(screen, bg="silver", text="⌫", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command= bksps)
bBksps.place(x=320, y=137, height=77, width=64)


# Third Buttons row
# Tan button
bTan = Button(screen, bg="silver", text="tan", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: tan(input))
bTan.place(x=0, y=214, height=77, width=64)
# 4 button
b4 = Button(screen, text="4", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("4"))
b4.place(x=64, y=214, height=77, width=64)
# 5 button
b5 = Button(screen, text="5", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("5"))
b5.place(x=128, y=214, height=77, width=64)
# 6 button
b6 = Button(screen, text="6", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("6"))
b6.place(x=192, y=214, height=77, width=64)
# - button
bSub = Button(screen, bg="silver", text="-", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("-"))
bSub.place(x=256, y=214, height=77, width=64)
# x² button
bSqrd = Button(screen, bg="silver", text="x²", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command = sqrd)
bSqrd.place(x=320, y=214, height=77, width=64)


## Fourth Buttons row
# ln button
bln = Button(screen, bg="silver", text="ln", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: ln(input))
bln.place(x=0, y=291, height=77, width=64)
# 1 button
b1 = Button(screen, text="1", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("1"))
b1.place(x=64, y=291, height=77, width=64)
# 2 button
b2 = Button(screen, text="2", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("2"))
b2.place(x=128, y=291, height=77, width=64)
# 3 button
b3 = Button(screen, text="3", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("3"))
b3.place(x=192, y=291, height=77, width=64)
# + button
bAdd = Button(screen, bg="silver", text="+", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("+"))
bAdd.place(x=256, y=291, height=77, width=64)
# 1/x button
bInv = Button(screen, bg="silver", text="1/x", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command= inverse)
bInv.place(x=320, y=291, height=77, width=64)

## Fifth Buttons row
# Power button
bPower = Button(screen, bg="silver", text="x^y", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command = power)
bPower.place(x=0, y=368, height=77, width=64)
# Clear button
bC = Button(screen, text="C", bg="silver", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command = clear)
bC.place(x=64, y=368, height=77, width=64)
# 0 button
b0 = Button(screen, text="0", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("0"))
b0.place(x=128, y=368, height=77, width=64)
# . button
bDot = Button(screen, text=".", bg="silver", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=lambda: click("."))
bDot.place(x=192, y=368, height=77, width=64)
# = button
bEq = Button(screen, text="=", bg="black", fg="white" ,relief=RIDGE, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="silver", command = equals)
bEq.place(x=256, y=368, height=77, width=64)
# n! button
bFact = Button(screen, text="n!", bg= "silver", relief=RAISED, border=3, font=("Sergoe UI", 13, "bold"), activebackground="light gray", activeforeground="gray", command=factorial_button)
bFact.place(x=320, y=368, heigh=77, width=64)


# Run the Main loop in a separate window 
screen.mainloop()