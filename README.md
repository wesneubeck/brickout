
BRICKOUT GAME

from:

http://codentronix.com/2011/04/14/game-programming-with-python-and-pygame-making-breakout/


using pygame

idea

Game states:
* Ball in paddle - we get in this state when the game starts or when we lose the ball.  
* Playing - we get in this state when we press SPACE to launch the ball. while playing the score may increase on the screen. 
* Game Over - when we lose all of our lives we get in this state.
* Won - we get in this state when we destroy all the bricks.


Game begins in the ball in paddle state.  in this state the ball is glued to the paddle and moves with the paddle because it is glued.  When you hit the SPACE bar the game goes in to "Playing" state. in this state the ball moves across the screen bouncing in to bricks, walls, and the paddle.  Each time a brick is broken a score is added to the overall score.  Each time the ball hits the bottom border, a life is taken away.  When the players life = 0, the game goes into Game Over state.  If all the bricks are destroyed, game enters Won state.

When the game goes to "Won" or "Game Over" we can move back to "Ball in Paddle" by hitting the Enter key. reset the score to 0. 

Paddle Movement:
We move the paddle left to right by hitting the 'LEFT' and 'RIGHT' keys.  We make sure to keep the paddle on the screen at all times.  

Ball Movement:
The Ball moves in 4 directions:
* up-right
* up-left
* down-right
* down-left

simulate a velocity vector??? we are going to use seperate values to update the position of the Ball.  

[X, Y]
[5, -5] --> up-right direction
[-5, -5] --> up-left direction
[-5, 5] --> down-right direction
[-5, -5] --> down-left direction

We have make sure the ball stays on the screen. When it hits the left of right borders we invert the X velocity component. So if it was going to the left it will end up going to the right and vice versa.

On the other hand.... we have to invert the Y velocity when the ball hits a brick, top border, the paddle, or the bottom border. so if the ball is moving up it ends up going down and vice versa. 


Collision Detection:
Technic use to determine if a collision has occured or not.  Basically two objects collide if they overlap.  We employ collision detection to determine if the ball collides with the bricks and the paddle.  


We will run in the game inside the Class Bricka:






