from tkinter import *

#FUNCTIONS#

def click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

def calculation():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def plus_minus():
    try:
        current = entry.get()
        if current.startswith("-"):
            entry.delete(0, END)
            entry.insert(0, current[1:])
        else:
            entry.delete(0, END)
            entry.insert(0, "-" + current)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

def percentage():
    try:
        current = entry.get()
        result = eval(current) / 100
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

#GUI#

app = Tk()
app.title("Calculator")
try:
    logo = PhotoImage(file='a.png')
    app.iconphoto(True, logo)
except:
    pass
app.config(bg="#000000")

#buttons#

acButton = Button(app, 
            text="AC", 
            width=5, 
            height=2, 
            bg="#727272", 
            fg="#000000", 
            font=("Arial", 20),
            command=lambda: entry.delete(0, END))
acButton.grid(row=0, column=0)

plusMinusButton = Button(app, 
            text="+/-",
            width=5, 
            height=2, 
            bg="#727272", 
            fg="#000000", 
            font=("Arial", 20),
            command=lambda: plus_minus())
plusMinusButton.grid(row=0, column=1)

percentButton = Button(app, 
            text="%",
            width=5, 
            height=2, 
            bg="#727272", 
            fg="#000000", 
            font=("Arial", 20),
            command=lambda: percentage())
percentButton.grid(row=0, column=2)

divideButton = Button(app, 
            text="÷",
            width=5, 
            height=2, 
            bg="#727272", 
            fg="#000000", 
            font=("Arial", 20),
            command=lambda: click("/"))
divideButton.grid(row=0, column=3)

multiplyButton = Button(app, 
            text="×",
            width=5, 
            height=2, 
            bg="#727272", 
            fg="#000000", 
            font=("Arial", 20),
            command=lambda: click("*"))
multiplyButton.grid(row=1, column=3)

subtractButton = Button(app, 
            text="-",
            width=5, 
            height=2, 
            bg="#727272", 
            fg="#000000", 
            font=("Arial", 20),
            command=lambda: click("-"))
subtractButton.grid(row=2, column=3)

addButton = Button(app, 
            text="+",
            width=5, 
            height=2, 
            bg="#727272", 
            fg="#000000", 
            font=("Arial", 20),
            command=lambda: click("+"))
addButton.grid(row=3, column=3)

EqualButton = Button(app, 
            text="=",
            width=5, 
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=calculation)
EqualButton.grid(row=4, column=3)

entry = Entry(app,
            width=20,
            font=("Arial", 20),
            bg="#000000",
            fg="#FFFFFF")
entry.grid(row=1, column=0, columnspan=3)
#-------------------------------------------------------------------------------------------------
button1 = Button(app,
            text="1",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(1))
button1.grid(row=2, column=0)

button2 = Button(app,
            text="2",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(2))
button2.grid(row=2, column=1)

button3 = Button(app,
            text="3",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(3))
button3.grid(row=2, column=2)

button4 = Button(app,
            text="4",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(4))
button4.grid(row=3, column=0)

button5 = Button(app,
            text="5",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(5))
button5.grid(row=3, column=1)

button6 = Button(app,
            text="6",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(6))
button6.grid(row=3, column=2)

button7 = Button(app,
            text="7",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(7))
button7.grid(row=4, column=0)

button8 = Button(app,
            text="8",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(8))
button8.grid(row=4, column=1)

button9 = Button(app,
            text="9",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(9))
button9.grid(row=4, column=2)

button0 = Button(app,
            text="0",
            width=5,
            height=2,
            bg="#727272",
            fg="#000000",
            font=("Arial", 20),
            command=lambda: click(0))
button0.grid(row=5, column=1)


app.mainloop()
