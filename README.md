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
  
   1. Upon running the program, a blue start menu should be present with a 'start' text in the middle.
   Flying enemies are in the background of the start menu as well, appearing from the left of the screen and then flying to      the right until they are off the screen. The background music and the purple space background is present as well, along with the layout of tiles. On the top right corner of the screen, the health bar is displayed. The health bar should be fully green.
   
   Note: Keep pressing [x] when an enemy is nearby to avoid dying while testing the next steps:
   
   2. When clicking the start text, the start menu will dissapear off the screen. Once the start menu is off the screen, the cat appears near the start (from the left) of the screen. Also, the enemies's in the current screen disappear and therefore start coming from the right of the screen again and are moving towards the left side of the screen.
   
   3. Press [x] to make the cat shoot blue fireballs. The enemies will dissappear once they are hit by the blue fireballs.
   While shooting enemies, the blue fireballs should explode after they hit an enemy. Fireballs of the same group will also explode.
   
   4. Press left keyboard key to check if cat moves to the left. While walking left, walk animation should be active as well.
   5. By pressing left, check that the cat does not go through a wall on its left side.
 
   6. Press right keyboard key to check if the cat moves to the right. While walking right, walk animation should be active as well.
  
   7. By pressing left, walk towards a wall to check that the cat does not go through a wall on its right side.
   
   8. While not pressing anything, except [x] when necessary, the cat's idling animation should be active if it isn't moving forwards or backwards.
  
   9. Press [space bar] to check if the cat jumps.
   
   10. By using the moving keys (left or right) move the cat towards a platform and jump on one. Confirm the cat stays on top of the platform.
   
   11. Walk off the platform with either the left or right keyboard key to see if cat falls off the platform.
   
   12. Walk off a platform into a pit where there are no tiles where the cat will land. A restart menu should appear. The restart menu should say 'you lose!' on top of the restart button.
   
   13. Click the restart button to restart the game. Once the restart button is pressed, the level's layout should reset to original position. The cat's position is also reset to its original position.
   
   14. By not pressing [x] anymore, let the player be hit by an enemy once. As soon as the cat turns red, press [x] to kill the enemy. The player's damage animation, which turns him red, should be active after the collision with the enemy. Also, the cat's life bar looses points (becomes more red) after the enemy collision.
   
   15. Allow the cat to be hit multiple times by an enemy or enemies. Once the health bar looses all life points and therefore is all red, the restart screen for loosing should appear.
   
   16. Click the restart button to restart the game. Check that once the restart button is pressed, that the level's layout resets to original position, along with the cat.
  
   17. Search for the winning red flag by moving forward (right) and by avoiding falling off a pit or being killed off by enemies. The flag should have a waving animation. Allow the cat to collide with the flag. Once both the cat and flag collide, a winning screen should appear. The winning screen lets the player know they have won. The text should say 'You won!' and underneath this text, the restart button is located.
   
   18. Click the restart button to restart the game.
   
   19. Press the red x on the left top corner to exit the program.
  
 # Directions and Grading Rubric

To review the project directions or update the grading rubric review the [DIRECTIONS.md](DIRECTIONS.md) file.
