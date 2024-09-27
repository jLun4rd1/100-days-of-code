from data import question_data
from quiz_brain import QuizBrain

# Creating the Question Class:
class Question:
    
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

question_bank = []
for dict in question_data:
    new_q = Question(q_text=dict['question'], q_answer=dict['correct_answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    
print("You've completed the Quiz!")
print(f"Your final_score was: {quiz.score}/{quiz.question_number}")