# Rubiks cube solver
With this program you can do many things.

These are all the functions in RubiksCubeSolverAdvanced:

home() is the function that allows you to manage everything
0: scrambles the cube and solves it
1: enter in play mode
2: resets the cube and all the global variables
3: shows the cube
4: quit the program

play() is the function that allows you to play with the cube by inserting the name of the moves (R, L, U, D, F, B, M, E, S, r, f, d)\n
-1: quit the program
0: shows the cube
1: shows all the moves inserted by the user
2: resets the cube and all the global variables
3: solves the cube
8: to go back in the home function

showCube() prints the all the faces of the cube in a pretty way

reset() is the function that resets all the global variables

scramble() it gets the first scramble combination from the "database" returns it and move it to the last posistion

solve() it solves the cube with the layer by layer method and at the end it changes some moves (read the comments in the code)

all the other functions are the moves, them are a little wild but it works

The ScramblesLoader is a function the creates/updates a list of scrambles using
the site: https://ruwix.com/puzzle-scramble-generator. It gets 9 scrambles at
a time, so you have to insert a multiple of 9 (don't ask why, it's just 9).

I tested the "algorithm" with over than 190000 different scrambles and worked all the times.
The average of the moves necessary to solve the cube is 161, they are so many due to some choices regarding the algorithm.I state that
the program should also work with the cross of all colors so I had to add some steps. I also set the program to solve the cube without
rotating it and then other moves were added. Finally for the F2L I had to use the layer by layer method given the complexity of the CFOP.
