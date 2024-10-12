import turtle
import pandas as pd
import string

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_states_list = []
correct_states = 0
total_states = 50

data = pd.read_csv("50_states.csv")

while correct_states < total_states:
    answer_state = string.capwords(screen.textinput(title=f"{correct_states}/{total_states} States guessed", prompt="What's another state's name?"))

    if answer_state == 'Exit':
        states_to_learn = [state for state in data['state'] if state not in correct_states_list]
        # states_to_learn = []
        # for state in data['state']:
        #     if state not in correct_states_list:
        #         states_to_learn['State'].append(state)
              
        df = pd.DataFrame(states_to_learn).to_csv("states_to_learn.csv"
                                                  )        
        break
    answer_data = data[data['state'] == answer_state]
    if not answer_data.empty and answer_state not in correct_states_list:
        answer_x = answer_data['x'].values[0]
        answer_y = answer_data['y'].values[0]
        
        answer_turtle = turtle.Turtle()
        answer_turtle.hideturtle()
        answer_turtle.penup()
        answer_turtle.goto(answer_x, answer_y)
        answer_turtle.write(answer_state)
        
        correct_states_list.append(answer_state)
        correct_states += 1
    
    
turtle.mainloop()