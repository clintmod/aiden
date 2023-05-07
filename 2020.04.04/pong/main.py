# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Open a new window
SIZE = (700, 500)
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong")

PADDLE_A = Paddle(WHITE, 10, 100)
PADDLE_A.rect.x = 20
PADDLE_A.rect.y = 200

PADDLE_B = Paddle(WHITE, 10, 100)
PADDLE_B.rect.x = 670
PADDLE_B.rect.y = 200

BALL = Ball(WHITE, 10, 10)
BALL.rect.x = 345
BALL.rect.y = 195

# This will be a list that will contain all the sprites we intend to use in our game.
ALL_SPRITES_LIST = pygame.sprite.Group()

# Add the car to the list of objects
ALL_SPRITES_LIST.add(PADDLE_A)
ALL_SPRITES_LIST.add(PADDLE_B)
ALL_SPRITES_LIST.add(BALL)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
CARRYON = True

# The CLOCK will be used to control how fast the SCREEN updates
CLOCK = pygame.time.Clock()

# Initialise player scores
SCOREA = 0
SCOREB = 0

# -------- Main Program Loop -----------
while CARRYON:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            CARRYON = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                CARRYON = False
    # Moving the paddles when the use uses the arrow KEYS (player A) or "W/S" KEYS (player B)
    KEYS = pygame.key.get_pressed()
    if KEYS[pygame.K_w]:
        PADDLE_A.move_up(5)
    if KEYS[pygame.K_s]:
        PADDLE_A.move_down(5)
    if KEYS[pygame.K_UP]:
        PADDLE_B.move_up(5)
    if KEYS[pygame.K_DOWN]:
        PADDLE_B.move_down(5)
    # --- Game logic should go here
    ALL_SPRITES_LIST.update()
    # Check if the BALL is bouncing against any of the 4 walls:
    if BALL.rect.x >= 690:
        SCOREA += 1
        BALL.velocity[0] = -BALL.velocity[0]
    if BALL.rect.x <= 0:
        SCOREB += 1
        BALL.velocity[0] = -BALL.velocity[0]
    if BALL.rect.y > 490:
        BALL.velocity[1] = -BALL.velocity[1]
    if BALL.rect.y < 0:
        BALL.velocity[1] = -BALL.velocity[1]
    # Detect collisions between the BALL and the paddles
    if pygame.sprite.collide_mask(BALL, PADDLE_A) or pygame.sprite.collide_mask(BALL, PADDLE_B):
        BALL.bounce()
    # --- Drawing code should go here
    # First, clear the SCREEN to black.
    SCREEN.fill(BLACK)
    # Draw the net
    pygame.draw.line(SCREEN, WHITE, [349, 0], [349, 500], 5)
    # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
    ALL_SPRITES_LIST.draw(SCREEN)
    # Display scores:
    FONT = pygame.font.Font(None, 74)
    TEXT = FONT.render(str(SCOREA), 1, WHITE)
    SCREEN.blit(TEXT, (250, 10))
    TEXT = FONT.render(str(SCOREB), 1, WHITE)
    SCREEN.blit(TEXT, (420, 10))
    # --- Go ahead and update the SCREEN with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    CLOCK.tick(60)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
