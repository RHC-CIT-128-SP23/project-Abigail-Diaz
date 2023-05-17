[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10716410&assignment_repo_type=AssignmentRepo)
# Space Cat

CIT 128 Student Directed Project

## Student Info

- Abigail Diaz
- CIT 128
- Spring 2023

## Program Description

My project is a platformer game where the player must pass two levels in the game. 
The enemies are alien green eyes with purple wings. The playable character is a cat.
The cat must jump and move forward while avoiding pitfalls and attacking enemies.
The goal of the program is to provide a simple game that works according to the player's input and
without errors that would ruin the gaming experience. The program will let the user know if they
have lost the game or not.

### Video Demonstration

Add a Link to your video demonstration

### Install Instructions

Add any install instructions, if needed. This includes how to install included modules or libraries as well as configurations. You may remove this section if no special instructions are required.

- Required modules: Pygame

  -Installing Pygame module 
    macOS
    On terminal type the command:
    python3 -m pip install -U pygame --user

    Windows
    On command prompt type the command:
    pip install pygame

## Software Engineering

Describe the software engineering techniques used for the design and development of this program.

The software engeneering techniques from the Software Development Life Cycle (SDLC) that have been used in the development of the project are checking if the project is feasible. The feasability taken into account is technical, since it would affect the project's progress the most when it comes to proper knowledge for implementation. Learning pygame for instance would take at least a week, therefore implementation would be delayed by a week. The second important feasibility is time since the project must be finished within 8 weeks, therefore I took into account that the game could not have varied enemies. Instead it was more feasable to keep one kind of enemy.

Secondly, once it was clear what was feasable, an analysis of the requirements was performed. The main functional requirements are allowing the cat to run forwards, backwards, jump, jump on platforms and reach a checkpoint to win. Logically, the game's goal is to give a gaming experience of a cat trying to pass a level, so thos functional requirements are important since it is a platformer game. Shooting the enemies was also a functional requirement since it is part of the game's description that the player should have some type of attack. Some non-functional reuquirements are animating the run, idle, and damage of the cat.

The other software developing technique used was the overall developing in the software stage. At this stage, the programming languages that will be used are taken into account. Since python is the main programming language used, due to its resourcefulness, no other languages were necessary. Built in modules that were chosen were math and random for instance. Pygame, which might need an installation as described above in the install instructions, was perfect for a simple and straight forward creation of a simple game.

At last, testing was also used as part of the SDLC. The main testing was checking if the functional requirements work with manual testing. For instance, one of the requirments is giving the illusion that the cat is moving forward to the right of the screen by pressing the right key. Another one is making sure that the cat can jump by pressing the space bar. If defects or errors were detected, which happened with the cat and tile collision, then they are fixed. Testing individual functional requirements in order also helped with isolating issues.

## Testing Script

Describe the testing process using paragraphs and numbered bullet lists how to manually test the software here. 
  
  ## Cat Testing
    1. Upon starting the game, the cat's initial position should be near the start (left side) of the screen.
    2. The cat should stay idling it isn't moving forwards or backwards due to user input. 
    3. Press [space bar] to check if the cat jumps.
    4. Press right keyboard key to check if the character moves to the right.
    5. Press left keyboard key to check if character moves to the left.
    6. Check if the character walk animation is active while pressing the right key or left key.
    7. Press [x] twice to check if the cat shoots blue fireballs.
    
 ## Cat and Platform Testing
    8. Jump on top of a platform to confirm the character stays on top of the platform.
    9. Walk off the platform with either the left or right keyboard key to see if character falls off the platform.
    
 ## Cat and Enemy testing
    10. Check that the enemy hits the cat once they collide.
    11. Check if cat's life bar looses point (becomes more red) by allowing the cat to get hit by a monster.
 
 # Enemy testing
    12.Check if the enemies dissappear once they are hit by the blue fireballs.
    13. Enemies should keep appearing from the right side of the screen until the player wins or looses.

## Directions and Grading Rubric

To review the project directions or update the grading rubric review the [DIRECTIONS.md](DIRECTIONS.md) file.
