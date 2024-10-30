# Programmers: Hazel Osborne, Zain Huda, Andrew Leimbach
# Course:  CS151, Dr. Zee
# Due Date: 10/30/2024
# Lab Assignment: 07
# Problem: Create a program that can help determine the cost of new flooring given room dimensions.
# Purpose: Understanding functions, reviewing loops, re-using our old knowledge.


# Purpose:  Calculates cost based of user inputs
# Parameters: floor_type
# Return: cost, float
def cost_calculation(floor_type):
    hardwood_cost = 1.39
    carpet_cost = 3.99
    tile_cost = 4.99

    # askingthe user the width of the room
    width = input("Enter the width of the room: ")
    while not width.isdigit() or float(width) <= 0:
        width = input("Invalid input. Enter a positive number for width: ")
    width = float(width)

    # ask user to enter the length of the room
    length = input("Enter the length of the room: ")
    while not length.isdigit() or float(length) <= 0:
        length = input("Invalid input. Enter a positive number for length: ")
    length = float(length)

    # find the cost using the floor type
    if floor_type == 'hardwood':
        cost = hardwood_cost * width * length
    elif floor_type == 'carpet':
        cost = carpet_cost * width * length
    else:
        cost = tile_cost * width * length

    return cost
# Purpose:  To error check user input
# Parameters: None
# Return: Floor type, string
def floor_type_input():
    floor_type = input("Enter floor type (tile, hardwood, carpet): ").lower()
    while floor_type not in ['tile', 'hardwood', 'carpet']:
        floor_type = input("Invalid input. Enter floor type (tile, hardwood, carpet): ").lower()
    return floor_type
# Purpose:  Welcomes, and thanks user for playing, as well as tells computer when to stop
# Parameters: None
# Return: None
def main():
    count = 0
    total = 0
    room_num = 'room 1'
    print("Welcome to the Floor Cost Calculator!")
    print("You can calculate costs for up to 5 rooms.")

    while count < 5:
        floor_type = floor_type_input()
        cost = cost_calculation(floor_type)
        print(f"Cost for {room_num}: ${cost:.2f}")
        count += 1
        total += cost
        room_num = f'room {count + 1}' if count < 5 else 'room 5'

    print(f"Total cost for all rooms: ${total:.2f}")
    print("Thank you for using the Floor Cost Calculator!")

# run the function
main()