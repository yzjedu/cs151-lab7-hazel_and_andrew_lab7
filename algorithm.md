# Algorithm Document
1. Set Hardwood costs as 1.39
2. Set carpet cost as 3.99
3. Set tile cost as 4.99

4. Name: cost_calculation 
5. Parameter: floor_type
6. Return: cost
7. Algorithm: 
   1. Prompt user to enter the width of the room
   2. Prompt user to enter the length of the room 
   3. check if floor_type = 'hardwood'
      1. cost = hardwood_cost * width * length
   4. otherwise, if floor_type = 'carpet'
      1. cost = carpet_cost * width * length
   5. otherwise:
      1. cost = tile_cost * width * length
    6. return cost

8. Name: floor_type_input
9. Parameter: none
10. Return: floor_type
11. Algorithm:
    1. prompt user to enter floor_type
    2. while floor_type is not 'tile', 'hardwood', and 'carpet
       1. re-prompt user to enter floor_type
    3. return floor_type

12. Name: Main
13. Parameter: none
14. Return: none
15. Algorithm:
    1. count = 0
    2. total = 0
    3. room_num = 'room 1'
    4. Display Welcome message / purpose
    5. while count < 5:
       1. call floor_type_input 
       2. call cost_calculation 
       3. display room cost
       4. add one to count 
       5. add cost to total
       6. replace 5th index of room num with count
       7. 
    6. display total cost to user 
    7. display ending message

16. run main

room_num.replace(room_num[5], count)


   