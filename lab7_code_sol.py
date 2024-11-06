# Programmers:  [your name here]
# Course:  CS151, [Instructors name here]
# Due Date: [date assignment is due]
# Programming Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]

# Initialize the constant
HARDWOOD = 1.39
CARPET = 3.99
TILE = 4.99

# Purpose: To check if a given string can be converted to a float.
# Parameters: value (string)
# Return: Boolean indicating if the value can be converted to a float.
def isfloat(value):
    temp = value.replace('.', '', 1)
    return temp.isdigit()

# Purpose: To get a valid positive dimension from the user.
# Parameters: prompt (string)
# Return: dimension as a float
def input_dim(prompt):
    print(prompt)
    dim = input("Enter dimension: ")
    while not isfloat(dim) or float(dim) < 0.0:
        dim = input("Enter dimension: ")
    return float(dim)

# Purpose: To get a valid floor type input from the user.
# Parameters: none
# Return: floor type as a string
def input_floor_type():
    floor_type = ''
    while floor_type != 'hardwood' and floor_type != 'carpet' and floor_type != 'tiles':
        floor_type = input("Enter type of floor: "
                           "\n\thardwood, "
                           "\n\tcarpet, or "
                           "\n\ttiles "
                           "\nYour choice ").lower().strip()
    return floor_type

# Purpose: To calculate the cost of flooring based on the room dimensions and floor type.
# Parameters: length (float), width (float), floor_type (string)
# Return: cost as a float
def room_renovation_cost(length, width, floor_type):
    if floor_type == 'hardwood':
        cost_per_sqft = HARDWOOD
    elif floor_type == 'carpet':
        cost_per_sqft = CARPET
    else:
        cost_per_sqft = TILE
    return length * width * cost_per_sqft

# Purpose: Main function to calculate and display the cost of flooring for multiple rooms and the total cost.
# Parameters: none
# Return: none
def main():
    print('-' * 100)
    print("This program determines the cost of flooring for each room and the total cost of flooring.")
    print('-' * 100)
    print()
    count = 1
    total_cost = 0

    while count <= 5:
        length =  input_dim(f'Let\'s get the width of the room {count}')
        width = input_dim(f'Let\'s get the length of the room {count}')
        floor_type = input_floor_type()

        room_cost = room_renovation_cost(length, width, floor_type)
        print(f'The cost of the room is {room_cost}')
        total_cost += room_cost
        count += 1

    print(f'The total cost of the room is {total_cost:.2f}')
    
    print()
    print('-' * 100)
    print('Thank you for using room cost calculator!')

main()