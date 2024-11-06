[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/uUGFnNE6)
# Lab 7

### 🔴🔴 *DO NOT* Start to code before the instructor Approve your algorithm, and test cases 🔴🔴

- **Grade: EMRN**
- **Due: Before Next Lab**

## `Problem`: 
- Your friend just bought a new house, but all of the rooms have carpet or laminate that is horribly dirty and gross.  
- They need your help to know how much it will cost to re-do all of the floors!  
- They want to put hardwood, carpet, or tile in each of the rooms of their house.  
- They have all of the dimensions of the rooms, which are conveniently all rectangles! 
- Their house has 5 rooms in it.
- You may need to design, write, and test a program that calculates the cost of buying flooring for your friend’s house.
  - Your friend may need to test the cost with different designs, so your program should ask your friend if they want to check the cost of another design.


## `Purpose`: 
This lab gives you practice with:
* Designing and programming functions
* Re-using many of the other aspects of Python we've learned so far
* Testing code

## `Details`:

### `Input and Output`
- For each room you need to find out from the user 
  - The width (in terms of feet as a real number), 
  - The length (in terms of feet as a real number), and 
  - The flooring type (hardwood, carpet, or tile). 
- The cost for each flooring type is set per square foot: 
  - Hardwood costs $1.39/sqft; 
  - carpet costs $3.99/sqft; and 
  - tile costs $4.99/sqft. 
- You should output to your user 
  - The `cost for each room`, and then 
  - The `overall cost as well`.

### `Error Checking`
- You don’t really trust your friend to follow the directions in your program. 
  - Protect your program from bad user input.  
- Use loops to force a valid flooring option and a valid dimension. 
- Your program should work no matter what case they type the flooring option, 
  - i.e. if they put extra whitespace before or after the word 
    -   (so for example, "  HaRDwood  " should work for "hardwood").

### `Design Hints`
- Start by thinking of the tasks for this problem.
- Then think how you'd solve a task, which may end up as your algorithm for that function
- Write up the functions and their algorithms that you've thought of.
  - Then see what you are missing, or what seems like it needs to be moved to another function.
- Think about 
  - `Parameters`: data your function needs to be able to run, and 
  - `Returned values`: data the function gives back to whatever function calls it
- If you find yourself doing the same `set of steps many times`, perhaps even just `with different numbers`, then `those set of steps should probably be a function` that you call in each of those places of your program.

## `Program Requirements`:
When you plan your solution, you must take the following into account:  

1. Your program must be designed using functions. 
   - All code except a single function call to main must be in a function.
2. Your program must use a main function that actually does something. 
   - Do not have main just make a single call to another function and that's it.
3. Your program must include everything discussed above in the details section
   - Including all error checking.
4. Functions now need to have function comments above them.
   - Similar to what we saw in the last set of lecture notes and in the solution to last week's lab. 
   - Above every function should be comments like the below:

```python
# Purpose:  [what problem does the function solve?]
# Parameters: [list with purpose in the same order they appear in the function header]
# Return: [return value, it's type, and what it represents]
```

## `Steps`:
1. Understand the problem
2. Write an algorithm in `algorithm.md` showing the steps the program will go through to solve this problem, and the functions that will be used. 
3. For each `function algorithm` you need to note the `purpose`, `name`, `parameters`, `returned value`, and `algorithm`. 
   - All steps in your algorithm should be part of a function. 
   - `Take turns being driver for functions`
     - Each partner should be writing the algorithm for half of the functions
3. Test that your algorithm works by walking through it with example input, and re-reading the requirements above.
4. When you think your algorithm is correct, ask the lab instructor to approve it. 
   - *The lab instructor must approve your algorithm before you code*
5. Write your code following your algorithm and using good `HCI` usability principles in `main.py`. 
   - *Take turns being driver -- each partner should code exactly half of the functions*
6. Properly comment your code with intro comments, **function comments**, and line comments
8. Write a set of test cases in `test_cases.xlsx` file to test that your program works correctly. 
   1. Make sure you fully test the error checking aspects of your program. 
      - Have at least one test that goes into each if statement option. 
9. You may `practice the flow chart` for each function on `flowchar.drawio.svg`. 
   - This can ensure that you have tested all paths, but you don't need to turn it in.

## `What to Submit in GitHub:`

1. Completed `main.py` file  
2. `algorithm.md`
   1. Must contain image of your flow chart
3. An Excel file with your test cases.  
    - Edit the `test_cases.xlsx` file with Excel software 
    - If it can open then ok. Otherwise
      - Right click on `test_cases.xlsx` -> Open In -> Associated Application
4. Encrypt your files using the `keys` and `process_reflection.py`
   1. `RD1.md` -> Reflection for Drive 1
   2. `RD2.md` -> Reflection for Drive 2
   3. If you use a different key, it is considered unsubmited

**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get? 
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working with your partner?