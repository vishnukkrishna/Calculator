# from tkinter import *

# window = Tk()
# window.configure(bg="#f73b4b")
# window.geometry("480x350")
# window.title("Calculator")
# entry = Entry(window, font=("GEEKSFORGEEKS", 20), width=30,  borderwidth=3, bg="#f6eeef", fg="black", )
# entry.grid(row=0, column=0, padx=5, pady=5, columnspan=30)


# def button_click(number):
#     current = entry.get()
#     entry.delete(0, END)
#     entry.insert(0, str(current) + str(number))


# def addition_button():
#     first_number = entry.get()
#     entry.delete(0, END)
#     global f_num
#     global math
#     f_num = int(first_number)
#     math = "addition"


# def subtraction_button():
#     first_number = entry.get()
#     entry.delete(0, END)
#     global f_num
#     global math
#     f_num = int(first_number)
#     math = "subtraction"


# def multiplication_button():
#     first_number = entry.get()
#     entry.delete(0, END)
#     global f_num
#     global math
#     f_num = int(first_number)
#     math = "multiplication"


# def division_button():
#     first_number = entry.get()
#     entry.delete(0, END)
#     global f_num
#     global math
#     f_num = int(first_number)
#     math = "division"


# def equal_button():
#     second_number = entry.get()
#     entry.delete(0, END)
#     if math == "addition":
#         entry.insert(0, f_num + int(second_number))
#     elif math == "subtraction":
#         entry.insert(0, f_num - int(second_number))
#     elif math == "multiplication":
#         entry.insert(0, f_num * int(second_number))
#     elif math == "division":
#         entry.insert(0, f_num / int(second_number))


# def clear_button():
#     entry.delete(0, END)


# button_1 = Button(window, text="1", padx="50", pady=20, command=lambda: button_click(1), bg="black", fg="white")
# button_2 = Button(window, text="2", padx="50", pady=20, command=lambda: button_click(2), bg="black", fg="white")
# button_3 = Button(window, text="3", padx="50", pady=20, command=lambda: button_click(3), bg="black", fg="white")

# button_4 = Button(window, text="4", padx="50", pady=20, command=lambda: button_click(4), bg="black", fg="white")
# button_5 = Button(window, text="5", padx="50", pady=20, command=lambda: button_click(5), bg="black", fg="white")
# button_6 = Button(window, text="6", padx="50", pady=20, command=lambda: button_click(6), bg="black", fg="white")

# button_7 = Button(window, text="7", padx="50", pady=20, command=lambda: button_click(7), bg="black", fg="white")
# button_8 = Button(window, text="8", padx="50", pady=20, command=lambda: button_click(8), bg="black", fg="white")
# button_9 = Button(window, text="9", padx="50", pady=20, command=lambda: button_click(9), bg="black", fg="white")

# button_0 = Button(window, text="0", padx="50", pady=20, command=lambda: button_click(0), bg="black", fg="white")

# button_addition = Button(window, text="+", padx=50, pady=20, command=addition_button, bg="#343b3b", fg="white")
# button_subtraction = Button(window, text="-", padx=50, pady=20, command=subtraction_button, bg="#343b3b", fg="white")
# button_multiplication = Button(window, text="x", padx=50, pady=20, command=multiplication_button, bg="#343b3b", fg="white")
# button_division = Button(window, text="÷", padx=50, pady=20, command=division_button, bg="#343b3b", fg="white")
# button_equal = Button(window, text="=", padx=50, pady=20, command=equal_button, bg="#343b3b", fg="white")
# button_clear = Button(window, text="C", padx=50, pady=20, command=clear_button)

# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2, )

# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2, )

# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2, )

# button_multiplication.grid(row=4, column=0)
# button_0.grid(row=4, column=1)
# button_division.grid(row=4, column=2)

# button_clear.grid(row=1, column=4)
# button_addition.grid(row=2, column=4)
# button_subtraction.grid(row=3, column=4,)
# button_equal.grid(row=4, column=4)

# window.mainloop()

import tkinter as tk
from tkinter.messagebox import showerror

elements = ['+', '-', '/', '*']
root = tk.Tk()
root.title('My Calculator')

root.resizable(0, 0)
root.config(bg='black')


def make_equation(number):
    present = e.get()
    clear()
    e.insert(0, present + number)


def check(equation):
    global elements
    for i in elements:
        if i in equation:
            return False
    else:
        return True


def calculator():
    try:
        equation = e.get()
        if len(equation) == 0 or check(equation):
            showerror('Error', 'Nothing Found to Calculator')
        else:
            calculated = eval(equation)
            clear()
            e.insert(0, str(calculated))
    except:
        showerror('Error!', 'Something Went Wrong!')


def clear():
    e.delete(0, tk.END)


# main entry

e = tk.Entry(root, font=('GEEKSFORGEEKS', 20), borderwidth=0, bg='white', fg='black')
e.grid(row=0, column=0, columnspan=3, padx=10, pady=20, ipady=20)

button_clear = tk.Button(root, text='⌫', command=clear, font=('Helvetica', 12), padx=25, pady=25, bg='Black',
                         fg='#EE0000', borderwidth=0)
button_clear.grid(row=0, column=3)

# row 1

button_1 = tk.Button(root, text='1', command=lambda: make_equation('1'), font=('Helvetica', 12), padx=25, pady=25,
                     bg='Black', fg='#39FF14', borderwidth=0)
button_1.grid(row=1, column=0, padx=2)
button_2 = tk.Button(root, text='2', command=lambda: make_equation('2'), font=('Helvetica', 12), padx=25, pady=25,
                     bg='Black', fg='#39FF14', borderwidth=0)
button_2.grid(row=1, column=1)
button_3 = tk.Button(root, text='3', command=lambda: make_equation('3'), font=('Helvetica', 12), padx=25, pady=25,
                     bg='Black', fg='#39FF14', borderwidth=0)
button_3.grid(row=1, column=2)
button_divide = tk.Button(root, text='➗', command=lambda: make_equation('/'), font=('Helvetica', 12), padx=23, pady=25,
                          bg='Black', fg='#EE0000', borderwidth=0)
button_divide.grid(row=1, column=3)

# row 2

button_4 = tk.Button(root, text='4', command=lambda: make_equation('4'), font=('Helvetica', 12), padx=25, pady=25,
                     bg='Black', fg='#39FF14', borderwidth=0)
button_4.grid(row=2, column=0, padx=2)
button_5 = tk.Button(root, text='5', command=lambda: make_equation('5'), font=('Helvetica', 12), padx=25, pady=25,
                     bg='Black', fg='#39FF14', borderwidth=0)
button_5.grid(row=2, column=1)
button_6 = tk.Button(root, text='6', command=lambda: make_equation('6'), font=('Helvetica', 12), padx=25, pady=25,
                     bg='Black', fg='#39FF14', borderwidth=0)
button_6.grid(row=2, column=2)
button_multiple = tk.Button(root, text='✖', command=lambda: make_equation('*'), font=('Helvetica', 12), padx=25,
                            pady=25, bg='Black', fg='#EE0000', borderwidth=0)
button_multiple.grid(row=2, column=3)

# row 3

button_7 = tk.Button(root, text='7', command=lambda: make_equation('7'), font=('Helvetica', 12), padx=25, pady=25,
                     bg='Black', fg='#39FF14', borderwidth=0)
button_7.grid(row=3, column=0, padx=2)
button_8 = tk.Button(root, text='8', command=lambda: make_equation('8'), font=('Helvetica', 12), padx=25, pady=25,
                     bg='Black', fg='#39FF14', borderwidth=0)
button_8.grid(row=3, column=1)
button_9 = tk.Button(root, text='9', command=lambda: make_equation('9'), font=('Helvetica', 12), padx=25, pady=25,
                     bg='Black', fg='#39FF14', borderwidth=0)
button_9.grid(row=3, column=2)
button_sub = tk.Button(root, text='➖', command=lambda: make_equation('-'), font=('Helvetica', 12), padx=27, pady=25,
                       bg='Black', fg='#EE0000', borderwidth=0)
button_sub.grid(row=3, column=3)

# row 4

button_dot = tk.Button(root, text='•', command=lambda: make_equation('.'), font=('Helvetica', 12), padx=25, pady=10,
                       bg='Black', fg='#EE0000', borderwidth=0)
button_dot.grid(row=4, column=0)
button_zero = tk.Button(root, text='0', command=lambda: make_equation('0'), font=('Helvetica', 12), padx=25, pady=15,
                        bg='Black', fg='#39FF14', borderwidth=0)
button_zero.grid(row=4, column=1)
button_equate = tk.Button(root, text='=', command=calculator, font=('Helvetica', 12), padx=25, pady=25, bg='Black',
                         fg='#EE0000', borderwidth=0)
button_equate.grid(row=4, column=2)
button_add = tk.Button(root, text='➕', command=lambda: make_equation('+'), font=('Helvetica', 12), padx=25, pady=25,
                       bg='Black', fg='#EE0000', borderwidth=0)
button_add.grid(row=4, column=3)

root.mainloop()