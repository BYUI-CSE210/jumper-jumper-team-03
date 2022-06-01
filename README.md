# Jumper
Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time. 

Jumper is played according to the following rules.

    -The puzzle is a secret word randomly chosen from a list.
    -The player guesses a letter in the puzzle.
    -If the guess is correct, the letter is revealed.
    -If the guess is incorrect, a line is cut on the player's parachute.
    -If the puzzle is solved the game is over.
    -If the player has no more parachute the game is over.

As part of additional work our team did on this assignment, the terminal will display if you already guessed a letter. If it is a letter that is correct that is already guessed, the player will not lose a parachute line, however, if it is an additional incorrect guess, the player will lose an additional parachute line.

## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine.

You can run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
The project files and folders are organized as follows:
```
jumper-jumper-team-03   (project root folder)
+-- jumper              (source code for game)
  +-- game              (specific classes)
    +--director.py
    +--parachute.py
    +--terminal_service.py
    +--puzzle.py
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.8.0

## Authors
* Nayara Mateus Nobre (nayara.mnobre@gmail.com)
* Olamilekan Ajibola (aji22001@byui.edu)
* Hannah Mosier(hannah89mosier@byui.edu)
* Paul  Agyare(agy21003@byui.edu)
