from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 0.4
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    top_label.config(text='Timer')
    check_mark.config(text='')
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        top_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        top_label.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        top_label.config(text='Work', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    
    count_min = count // 60
    count_sec = count % 60
    
    if count_sec < 10:
        count_sec = f'0{count_sec}'
        
    if count_min < 10:
        count_min = f'0{count_min}'
        
    count_text = f'{count_min}:{count_sec}'
    
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark_text = ''
        work_sessions = reps // 2 # every work_session (2 sessions)
        for _ in range(work_sessions):
            check_mark_text += '✔'    
        check_mark.config(text=check_mark_text)
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

grid_starter = Label()
grid_starter.grid(column=0,row=0)

top_label = Label(text='Timer', font=(FONT_NAME, 34, 'bold'), bg=YELLOW, fg=GREEN)
top_label.grid(column=1,row=0)

canvas = Canvas(width=200, height=244, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1,row=1)

start_button = Button(text='Start', font=('Arial', 10, 'bold'), bg='white', highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text='Reset', font=('Arial', 10, 'bold'), bg='white', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark = Label(font=('Arial', 14), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()