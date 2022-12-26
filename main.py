from tkinter import *
import csv
from funcs import write_result
import re

window = Tk()
window.title("LAWYER CALCULATOR")
window.geometry("700x750")


def calculate_taxes():
    percentage = float(percent.get())
    summary = float(sum.get())
    periodical = int(period.get())
    result = (summary / periodical) * (percentage / 100)
    write_result(result=result)
    label.config(text=result)


def show_history():
    with open('results.csv', 'r') as file:
        result = file.readlines()
        for item in result:
            text.insert(1.0, str(item))


def delete_text():
    text.delete(1.0, END)
    with open('results.csv', 'w') as file:
        file.write("")
        file.close()

def is_valid(newval):
    result=  re.match("^\+{0,1}\d{0,11}$", newval) is not None
    if not result and len(newval) <= 12:
        errmsg.set("Номер телефона должен быть в формате +xxxxxxxxxxx, где x представляет цифру")
    else:
        errmsg.set("")
    return result
check = (window.register(is_valid), "%P")

errmsg = StringVar()
error_label = Label(foreground="red", textvariable=errmsg, wraplength=250)
error_label.pack(padx=5, pady=5, anchor=NW)


Label(window, text="Enter percent", font=('Calibri 10')).pack(anchor=NW, padx=8, pady= 8)
percent = Entry(window, width=35, validate="key", validatecommand=check)
percent.pack(anchor=NW, padx=8, pady= 8)
Label(window, text="Enter sum", font=('Calibri 10')).pack(anchor=NW, padx=8, pady= 8)
sum = Entry(window, width=35, validate="key", validatecommand=check)
sum.pack(anchor=NW, padx=8, pady= 8)
Label(window, text="Enter period", font=('Calibri 10')).pack(anchor=NW, padx=8, pady= 8)
period = Entry(window, width=35)
period.pack(anchor=NW, padx=8, pady= 8)

label = Label(window, text="Total Sum : ", font=('Calibri 15'))
label.pack(pady=20)
text = Text(window, font=('Calibri 10'))
text.pack()

calculate_taxes_button = Button(window, text="Calculate taxes", command=calculate_taxes)
calculate_taxes_button.pack()
show_history = Button(window, text="Show history", command=show_history)
show_history.pack()
frame = Frame()
frame.pack()
Button(frame, text="Clear history",
       command=delete_text).pack(side=LEFT)

def main():
    window.mainloop()


if __name__ == '__main__':
    main()
