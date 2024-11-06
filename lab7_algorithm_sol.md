# Algorithm for Room Renovation Program


## Tasks
- A way to input a dimension
- Check if the dimension is float
- A way to input the floot type
- Calculate the renovation cost per room
- main, to run the entier program

## Initialization
- Set `HARDWOOD = 1.39` (cost per square foot for hardwood flooring)
- Set `CARPET = 3.99` (cost per square foot for carpet flooring)
- Set `TILE = 4.99` (cost per square foot for tile flooring)
-----------
## Algorithm for `isfloat`
- **Purpose**: To check if a given string can be converted to a float.
- **Name**: `isfloat`
- **Parameters**: `value` (string)
- **Return**: Boolean indicating if the value can be converted to a float.
- **Algorithm**:
  1. Replace the first occurrence of a period `.` in `value` with an empty string.
  3. Return a boolean that the modified `value` is composed of digits or not.
-----------
## Algorithm for `input_dim`
- **Purpose**: To get a valid positive dimension from the user.
- **Name**: `input_dim`
- **Parameters**: `prompt` (string)
- **Return**: Dimension as a float.
- **Algorithm**:
  1. Print the `prompt`.
  2. Ask the user to enter a dimension and store it in `dim`.
  3. While `dim` is not a valid float or is less than 0:
     - Ask the user to enter the dimension again.
  4. Return `dim` to the calling function.
-----------
## Algorithm for `input_floor_type`
- **Purpose**: To get a valid floor type input from the user.
- **Name**: `input_floor_type`
- **Parameters**: none
- **Return**: Floor type as a string.
- **Algorithm**:
  1. Initialize `floor_type` to an empty string.
  2. While `floor_type` is not `hardwood`, `carpet`, or `tiles`:
     - Ask the user to input the type of floor (options: hardwood, carpet, tiles).
  3. Return `floor_type`.
-----------
## Algorithm for `room_renovation_cost`
- **Purpose**: To calculate the cost of flooring based on room dimensions and floor type.
- **Name**: `room_renovation_cost`
- **Parameters**: `length` (float), `width` (float), `floor_type` (string)
- **Return**: Cost as a float.
- **Algorithm**:
  1. If `floor_type` is 'hardwood':
     - Set `cost_per_sqft` to `HARDWOOD`.
  2. Otherwise, if `floor_type` is 'carpet':
     - Set `cost_per_sqft` to `CARPET`.
  3. Otherwise:
     - Set `cost_per_sqft` to `TILE`.
  4. Calculate `room_cost` as `length * width * cost_per_sqft`.
  5. Return `room_cost`.
-----------
## Algorithm for `main`
- **Purpose**: Main function to calculate and display the cost of flooring for multiple rooms and the total cost.
- **Name**: `main`
- **Parameters**: none
- **Return**: none
- **Algorithm**:
  1. Print a decorative line and a message indicating the purpose of the program.
  2. Initialize `count` to 1 (to track the number of rooms).
  3. Initialize `total_cost` to 0 (to store the cumulative cost of all rooms).
  4. While `count` is less than or equal to 5:
     - Call `input_dim` with a prompt to get `length`.
     - Call `input_dim` with a prompt to get `width`.
     - Call `input_floor_type` to get `floor_type`.
     - Call `room_renovation_cost` with `length`, `width`, and `floor_type` to get `room_cost`.
     - Print the `room_cost`.
     - Add `room_cost` to `total_cost`.
     - Increment `count` by 1.
  5. Print the `total_cost`, formatted to two decimal places.
  6. Print a decorative line and a closing message thanking the user for using the program.