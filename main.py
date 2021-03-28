import re

print('Magical Calculator')
print("Type 'quit' to exit \n")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation = input("Enter equation:")
    if equation == 'quit':
        run = False
    else:
        previous = eval(equation)
        print("You typed", previous)


while run:
    perform_math()