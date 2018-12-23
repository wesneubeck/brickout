
import pygame 

SCREEN_SIZE = 640, 480

# Object dimensions
BRICK_WIDTH = 60
BRICK_HEIGHT = 15

PADDLE_WIDTH = 60
PADDLE_HEIGHT = 12

BALL_DIAMETER = 16
BALL_RADIUS = BALL_DIAMETER / 2

# Paddle and ball movement
MAX_PADDLE_X = SCREEN_SIZE[0] - PADDLE_WIDTH 
MAX_BALL_X = SCREEN_SIZE[0] - BALL_DIAMETER
MAX_BALL_Y = SCREEN_SIZE[1] - BALL_DIAMETER

# Paddle Y coordinate
PADDLE_Y = SCREEN_SIZE[1] - PADDLE_HEIGHT - 10 

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BRICK_COLOR = (200, 200, 0)

# Game States constants
STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3


class Bricka:
# create the game inside this class	
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode(SCREEN_SIZE)
		pygame.display.set_caption("Brickout!")

		self.clock = pygame.time.Clock()

		if pygame.font:
			self.font = pygame.font.Font(None, 30)
		else:
			self.font = None

		self.init_game()


# start of the game
def init_game(self):
	self.lives = 3
	self.score = 0
	self.state = STATE_BALL_IN_PADDLE

	self.paddle = pygame.Rect(300, PADDLE_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
	self.ball = pygame.Rect(300, PADDLE_Y - BALL_DIAMETER, BALL_DIAMETER, BALL_DIAMETER)

	self.ball_vel = [5, -5]

	self.create_bricks()

def create_brick(self):
	y_ofs = 35
	self.bricks = []
	for i in range(7):
		x_ofs = 35
		for j in range(8):
			self.bricks.append(pygame.Rect(x_ofs, y_ofs, BRICK_WIDTH, BRICK_HEIGHT))
			x_ofs += BRICK_WIDTH + 10
		y_ofs += BRICK_HEIGHT + 5


# Create Keyboard input function

def check_input(self):
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		self.paddle.left -= 5
		if self.paddle.left < 0:
			self.paddle.left = 0

	if keys[pygame.K_RIGHT]:
		self.paddle.left += 5
		if self.paddle.left > MAX_PADDLE_X:
			self.paddle.left = MAX_PADDLE_X

	if keys[pygame.K_SPACE] and self.state == STATE_BALL_IN_PADDLE:
		self.ball_vel = [5, -5]
		self.state = STATE_PLAYING
	elif keys[pygame.K_RETURN] and (self.state == STATE_GAME_0VER or self.state == STATE_WON):
		self.init_game() 



