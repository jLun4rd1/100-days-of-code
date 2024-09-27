# from turtle import Turtle, Screen

# testy = Turtle()
# testy.shape("turtle")
# testy.color("DarkRed")

# for i in range(0,4):
#     if i % 2 == 0:
#         testy.left(72)
#         testy.forward(100)
#         testy.right(144)
#         testy.forward(100)
#         testy.left(72)
#         testy.forward(100)
#     else:
#         testy.right(72)
#         testy.forward(100)
#         testy.left(144)
#         testy.forward(100)
#         testy.right(72)
#         testy.forward(100)
        
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])

print(table.align)

table.align = 'l'
print(table)