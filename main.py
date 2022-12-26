from tkinter import *


window = Tk()
window.title("LAWYER CALCULATOR")
window.geometry("700x750")
def calculate_taxes():
    percentage = float(percent.get())
    summary = float(sum.get())
    periodical = int(period.get())
    result = (summary / periodical) * (percentage / 100)
    label.config(text=result)


Label(window, text="Enter percent", font=('Calibri 10')).pack()
percent = Entry(window, width=35)
percent.pack()
Label(window, text="Enter sum", font=('Calibri 10')).pack()
sum = Entry(window, width=35)
sum.pack()
Label(window, text="Enter period", font=('Calibri 10')).pack()
period = Entry(window, width=35)
period.pack()

label=Label(window, text="Total Sum : ", font=('Calibri 15'))
label.pack(pady=20)

calculate_taxes_button = Button(window, text = "Calculate taxes", command=calculate_taxes)
calculate_taxes_button.pack()



def main():
    window.mainloop()


if __name__ == '__main__':
    main()
