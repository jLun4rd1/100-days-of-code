from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WRONG_COLOR = "#FD4659"
RIGHT_COLOR = "#2DFE54"


class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.score = Label(
            text='Score: 0',
            fg='white',
            bg=THEME_COLOR,
            font=('Arial', 12, 'bold')
        )
        self.score.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text='placeholder',
            font=('Arial', 16, 'italic'),
            fill=THEME_COLOR
        )
        
        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true_answer)
        self.true_button.grid(row=2, column=0)
        
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false_answer)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end\nYou scored {self.quiz.score}/10!")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
        
    def check_true_answer(self):
        correct_answer = self.quiz.check_answer('True')
        self.give_feedback(correct_answer)
            
    def check_false_answer(self):
        correct_answer = self.quiz.check_answer('False')
        self.give_feedback(correct_answer)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=RIGHT_COLOR)
        else:
            self.canvas.config(bg=WRONG_COLOR)
        self.window.after(1000, func=self.get_next_question)