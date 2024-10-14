from tkinter import *

def convert():
    miles = int(entry.get())
    km = round(miles * 1.60934, 2)
    result.config(text=f'{km}')

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

grid_starter = Label()
grid_starter.grid(column=0, row=0)

entry = Entry()
entry.insert(0, '0')
entry.grid(column=1, row=0)

miles = Label(text='Miles')
miles.grid(column=2, row=0)

is_equal_to = Label(text='is equal to')
is_equal_to.grid(column=0, row=1)

result = Label(text='0')
result.grid(column=1, row=1)

km = Label(text='Km')
km.grid(column=2, row=1)

calculate = Button(text='Calculate', command=convert)
calculate.grid(column=1, row=2)

window.mainloop()