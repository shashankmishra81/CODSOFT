import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title("Calculator")
frame = tk.Frame(master=window, bg="white", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)
def Click(number):
    entry.insert(tk.END, number)
def equal():
    try:
        a = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, a)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)
b1 = tk.Button(master=frame, text='1', padx=15, pady=5, width=3, command=lambda: Click(1))
b1.grid(row=1,column=0,pady=2)

b2 = tk.Button(master=frame, text='2', padx=15, pady=5, width=3,command=lambda:Click(2))
b2.grid(row=1, column=1, pady=2)

b3 = tk.Button(master=frame, text='3', padx=15, pady=5, width=3,command=lambda:Click(3))
b3.grid(row=1, column=2, pady=2)

b4 = tk.Button(master=frame, text='4', padx=15, pady=5, width=3, command=lambda: Click(4))
b4.grid(row=2, column=0, pady=2)

b5 = tk.Button(master=frame, text='5', padx=15, pady=5, width=3, command=lambda: Click(5))
b5.grid(row=2, column=1, pady=2)

b6 = tk.Button(master=frame, text='6', padx=15, pady=5, width=3, command=lambda: Click(6))
b6.grid(row=2, column=2, pady=2)

b7 = tk.Button(master=frame, text='7', padx=15, pady=5, width=3, command=lambda: Click(7))
b7.grid(row=3, column=0, pady=2)

b8 = tk.Button(master=frame, text='8', padx=15, pady=5, width=3, command=lambda: Click(8))
b8.grid(row=3, column=1, pady=2)

b9 = tk.Button(master=frame, text='9', padx=15, pady=5, width=3, command=lambda: Click(9))
b9.grid(row=3, column=2, pady=2)

b0 = tk.Button(master=frame, text='0', padx=15, pady=5, width=3, command=lambda: Click(0))
b0.grid(row=4, column=1, pady=2)

add = tk.Button(master=frame, text="+", padx=15, pady=5, width=3, command=lambda: Click('+'))
add.grid(row=4, column=2, pady=2)

subtract = tk.Button(master=frame, text="-", padx=15, pady=5, width=3, command=lambda: Click('-'))
subtract.grid(row=4, column=0, pady=2)
 
multiply = tk.Button(master=frame, text="*", padx=15, pady=5, width=3, command=lambda: Click('*'))
multiply.grid(row=5, column=0, pady=2)
 
division = tk.Button(master=frame, text="/", padx=15, pady=5, width=3, command=lambda: Click('/'))
division.grid(row=5, column=2, pady=2)

Equal = tk.Button(master=frame, text="=", padx=15, pady=5, width=9, command=equal)
Equal.grid(row=5, column=1, pady=2)

Clear = tk.Button(master=frame, text="clear", padx=15, pady=5, width=12, command=clear)
Clear.grid(row=7, column=1, columnspan=1, pady=2)

window.mainloop()
