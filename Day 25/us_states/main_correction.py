import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_states_list = []

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(correct_states_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states_list)}/50 States guessed", prompt="What's another state's name?").title()

    answer_data = data[data.state == answer_state]

    if answer_state == 'Exit':
        break
    if answer_state in all_states and answer_state not in correct_states_list:
        answer_x = answer_data['x'].item()
        answer_y = answer_data['y'].item()
        
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.penup()
        answer_turtle.goto(answer_x, answer_y)
        answer_turtle.write(answer_state)
        
        correct_states_list.append(answer_state)
    
turtle.mainloop()