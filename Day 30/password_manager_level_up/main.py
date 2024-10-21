from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ----------------------------- PASSWORD MANAGER -------------------------------- #
def search_password():
    website_string = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found.')    
    else:
        if website_string in data:
            email = data[website_string]['email']
            password = data[website_string]['password']
            messagebox.showinfo(title=f"{website_string}", message=f'Info about {website_string}: \n\nE-mail: {email} \nPassword: {password}')
        else:    
            messagebox.showerror(title='No data found!', message=f"Sorry, but there's no data for the website '{website_string}'")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))] 
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))] 
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_string = website_entry.get()
    username_string = username_entry.get()
    password_string = password_entry.get()
    new_data = {
        website_string:{
            "email": username_string,
            "password": password_string
        }
    }
    
    if len(website_string) == 0:
        messagebox.showwarning(title='Warning!!', message='Hey, you forgot to input a website!')
    elif len(password_string) == 0:
        messagebox.showwarning(title='Warning!!', message='Hey, you forgot to input a password!')
    else:
        try:
            with open('data.json', mode='r') as data_file:
                data = json.load(data_file) # <<< read data
        except FileNotFoundError:
            with open('data.json', mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data) # <<< update_data
        
            with open('data.json', mode='w') as data_file:
                json.dump(data, data_file, indent=4) # <<< write data (saving updated data)
        finally:    
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# grid_starter = Label()
# grid_starter.grid(row=0, column=0)

canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)
username_entry = Entry(width=52)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, 'joaoclunardi@gmail.com')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
password_button = Button(text='Generate Passowrd', width=15, command=generate_password)
password_button.grid(row=3, column=2)

search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2)

add_button = Button(text='Add', width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()