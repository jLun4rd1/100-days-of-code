from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/flashcards_data.csv').head(1)
else:
    if data.empty:
        data = pd.read_csv('data/flashcards_data.csv').head(5)
finally:
    list_of_dicts = data.to_dict(orient='records')
    
word_data = {}

# -------------------------- CARD MANAGER ----------------------------- #
def flip_card():
    canvas.itemconfig(front, image=card_back)
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(word, text=word_data["English"], fill='white')
    
def change_flashcard(is_correct):
    global word_data, flip_timer
    window.after_cancel(flip_timer)
    
    if is_correct:
            list_of_dicts.remove(word_data)
    
    if len(list_of_dicts) == 0:
        messagebox.showinfo(title='Congratulations', message='Congratulations for your amazing feet! \nYou learned all the words from the list!!')
        pd.DataFrame(columns=['German', 'English']).to_csv('data/words_to_learn.csv', index=False)
    else:
        word_data = random.choice(list_of_dicts)
        canvas.itemconfig(front, image=card_front)
        canvas.itemconfig(title, text="German", fill='black')
        canvas.itemconfig(word, text=word_data["German"], fill='black')
    
        flip_timer = window.after(3000, flip_card)
        
        pd.DataFrame(list_of_dicts).to_csv('data/words_to_learn.csv', index=False)
    
def right_answer():
    change_flashcard(is_correct=True)
    
def wrong_answer():
    change_flashcard(is_correct=False)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

card_back = PhotoImage(file='images/card_back.png')
card_front = PhotoImage(file='images/card_front.png')
right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"))
word = canvas.create_text(400, 236, text='', font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_button = Button(image=wrong, bg=BACKGROUND_COLOR, highlightthickness=0, command=wrong_answer)
wrong_button.grid(row=1, column=0)

right_button = Button(image=right, bg=BACKGROUND_COLOR, highlightthickness=0, command=right_answer)
right_button.grid(row=1, column=1)

change_flashcard(is_correct=False)

window.mainloop()