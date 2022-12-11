# Chesslet (a.k.a. Chess Quizlet)

# The Short Version

You play a color and the computer plays a color. Use the built in openings or add your own with the input.py file. The
computer will bully you with red X's until you make the correct move, and then it will keep playing against you until 
the input line ends. Hit enter to restart the opening and it will randomly choose a new line of the opening you selected
to play as your opponent..

# The Long Version
Chesslet is meant to help people learn openings. At the time of writing this, I'm 1474 and still occasionally blunder a 
pawn in the first 5 moves. That's not good. Studying with an analysis board is fun but painful and courses cost money.

With Chesslet, you use input a line using an outside analysis board and the input.py file. On line 7 there is a line 
that specifies a file name for the computer to write in. Change that name to be the name of whatever opening you want 
and create a file with that same name in your project folder. From there, just make the moves on the board ui and toggle 
with the arrow keys to go back to add new potential moves for your opponent. The program will add that all into the 
file you just made in a way that it can easily interpret, and you're all set. The G6 Modern is already built in with
the e4/g6 lines, and the queen's gambit will soon be added as an opening for white.

Once you have your openings file, change the opening name on line 7 of main.py to match your opening file. Then the 
training process can begin!

You will play one color and the computer will play the other. With each move, if you get it correct, it will give you 
a checkmark and make its next move. Otherwise, it will give you an X and you will have to undo the move and try again. 
The computer chooses its next move based on whatever you input, and it weights each line by how many variations it has.
Hit enter to restart the opening (it will again randomly choose a line).

# Installation

No Stockfish. Nothing complicated. 

Any Python (version 3+) IDE is good as long as you can install pygame. To do this, google it and don't try to figure it 
out from a README file. There are many many great tutorials on it. It's not hard... 

But for those of you who want to ignore what I just said, I'll give you even more directions for you to ignore and 
screw up. Happy?

Use PyCharm because it's the easiest. Just clone this repository (using gitKraken or the terminal or whatever else) and 
open the project in PyCharm. In the bottom right corner, there's a space that shows the interpreter. It should say 
Python 3.something, and if it doesn't then install python. But assuming you have Python installed, click on the 
interpreter and a menu should pop up. Click "Interpreter Settings" and then there's a table showing all the packages you 
have installed. Hit the plus button and type in "Pygame" and that's it. That's literally all you have to do to run 
the program.

You may have to set your run configuration if you want to use the input.py file for yourself, but for that you just 
click on your run configuration and change the name of the file from "main.py" to "input.py" so it's not that bad.