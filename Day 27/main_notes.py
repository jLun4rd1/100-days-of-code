from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


# Label
my_label = Label(text='My Label', font=("Arial", 14))
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Button
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    
button = Button(text='I am clickable', command=button_clicked)
button.grid(column=1, row=1)

def button2_clicked():
    new_text = input.get()
    my_label.config(text=new_text)
    
button2 = Button(text='I am clickable', command=button_clicked)
button2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
input.grid(column=4, row=2)


window.mainloop()