# Mower_Rep

This repository contains essential files to solve the Mower problem. It contains:
- Mower_Exercice.py which is a Python script that gives you the final position of a mower based on lawn dimensions and instructions.
- README.md which is a markdown descrybing this project.
- Tondeuse.txt which is a txt file containg lawn dimensions, initial positions of mowers and instructions.

## Description of the mower problem

The instructions mentioned in the Tondeuse.txt file can contains two types of orders "A" to advance or "G" and "D" (to signify left and right) to change mower's direction.
If we are in the case of Advance instruction, the mower will advance with only one step keeping it's current direction. If it meets one of the walls of the lawn, the instruction that leaded to this situation won't be taken into consideration and the mower won't move.
As we said in the instruction file we can only find two types of direction: "D" and "G" where in the spot, the mower can take more directions: "E", "W", "N", and "S" (East, West, North and South). In fact, the Mower takes a turn of 90 degrees by changing every time the direction. This looks like moving on a cercle by a 90 degrees each time and that leads to the four possible directions. 

## To run it

To run it we should have an envirement which uses [Python 3](https://docs.python.org/3.6/using/windows.html#installing-python). Open the CMD and move to the directory containing the script and the file Tondeuse.txt.
Then type:
```bash
python Mower_Exercice.py
```
Make sure before running the script that the envirement you use contains the package regex, if not install it as follow:
```bash
pip install regex
```

## Fonctions in the script

This script contains 6 functions:

#### get_dimensions(f_Tondeuse)
- This function recuperate the lawn dimensions from Tondeuse.txt.

It has has only one argument:
f_Tondeuse (string) which is Tondeuse file's contents. 

It has two returns:
1) int: The value of espace_i which is the length of the axis I.
2) int: The value of espace_j which is the length of the axis J.
    
#### get_initial_position_direction(f_pos_dir)
- This function recuperate the initial position and direction of a mower.

It has has only one argument:
f_pos_dir (string) which is Tondeuse file's line containing iformations about the initial position and direction of a mower . 

It has three returns:
1) int: The initial position of a mower on the axis I.
2) int: The initial position of a mower on the axis J.
3) string: The initial direction of a mower

#### To_advance(current_i,current_j,current_direction,espace_i,espace_j)
- This function updates the current positions after verifying tha the mower dosn't exceed the the lawn surface.

It has five arguments:
1) current_i (int) which is the current position of the mower on the axis I.
2) current_j (int) which is the current position of the mower on the axis J.
3) current_direction (string) which is the current direction of the mower.
4) espace_i (int) which is the length of the axis I.
5) espace_j (int) which is the length of the axis J.
    
It has two returns:
1) int: The updated current position of a mower on the axis I.
2) int: The updated current position of a mower on the axis J.

#### Manage_direction(current_direction,i)
- This function updates the current direction of a mower.
    
It has only one argument:
current_direction (string) which is the current direction of the mower.
    
And it has only one return:
string: The updated current direction of a mower.

#### To_move(instructions,current_i,current_j,current_direction,espace_i,espace_j)
- This function manage the flow of a mower's instructions.
    
It has 6 arguments:
1) instructions (string) which is the string containing instructions.
2) current_i (int) which is the current position of the mower on the axis I.
3) current_j (int) which is the current position of the mower on the axis J.
4) current_direction (string) which is the current direction of the mower.
5) espace_i (int) which is the length of the axis I.
6) espace_j (int) which the length of the axis J.
    
It has three returns:
1) int: The updated current position of the mower on the axis I.
2) int: The updated current position of the mower on the axis J.
3) string: The updated current direction of a mower.

#### main() 
- The main function of the script.
