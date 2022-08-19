# filename: Rocket assignmnet

# Author name: Michael, Muhtasim, Sameer, Khatab, Aggash

# Date created: 23/06/2021

"""

this program is creating a rocket simulation using pygame

"""

# Import a library of functions called 'pygame'

import pygame

from math import pi

from pygame import mixer

from random import *

# Initialize the game engine

pygame.init()

# Define the colors we will use in RGB format

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

BLUE = (0, 0, 255)

GREEN = (0, 255, 0)

RED = (255, 0, 0)

dark_red = (173, 0, 0)

light_red = (219, 0, 0)

GRAY = (59, 49, 49)

BROWN = (193, 154, 107)

light_blue = (139, 204, 203)

PURPLE = (224, 16, 47)

YELLOW = (255, 247, 0)

light_yellow = (245, 242, 157)

PEACH = (245, 219, 154)

MAROON = (112, 0, 0)

GLASS = (168, 204, 215)

SKYBLUE = (135, 206, 235)

ROAD = (71, 72, 76)

SILVER = (192, 192, 192)

STEEL = (224, 223, 219)

ORANGE = (255, 51, 0)

# Set the height and width of the screen

size = [660, 400]

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Group 2 rocket assignment")

# Loop until the user clicks the close button.

done = False

clock = pygame.time.Clock()

count = 6

def rocket(x_rock, y_rock):

    # Top Triangle Red

    pygame.draw.polygon(screen, RED,

                        [[(x_rock), y_rock], [x_rock + 50, y_rock + 50],

                         [x_rock - 50, y_rock + 50]])

    # Rectangle Body Blue

    pygame.draw.rect(screen, BLUE, [x_rock - 50, y_rock + 50, 100, 200])

    # Side1a White

    pygame.draw.rect(screen, WHITE, [x_rock - 120, y_rock + 190, 70, 30])

    # Side1b

    pygame.draw.rect(screen, WHITE, [x_rock - 120, y_rock + 220, 20, 20])

    # Side2a White

    pygame.draw.rect(screen, WHITE, [x_rock + 50, y_rock + 190, 70, 30])

    # Side2b

    pygame.draw.rect(screen, WHITE, [x_rock + 100, y_rock + 220, 20, 20])

    # Flames1a RED

    pygame.draw.rect(screen, GREEN, [x_rock - 120, y_rock + 240, 20, 30])

    # Flames1b Orange

    pygame.draw.rect(screen, ORANGE, [x_rock - 115, y_rock + 270, 10, 400])

    # Flames2a RED

    pygame.draw.rect(screen, GREEN, [x_rock + 100, y_rock + 240, 20, 30])

    pygame.draw.rect(screen, ORANGE, [x_rock + 105, y_rock + 270, 10, 400])

    # Bottom ORANGE

    pygame.draw.polygon(

        screen, STEEL,

        [[x_rock - 50, y_rock + 250], [x_rock + 50, y_rock + 250],

         [x_rock + 80, y_rock + 290], [x_rock - 80, y_rock + 290],

         [x_rock - 50, y_rock + 250]])

    # Bottom Blue Flames

    pygame.draw.rect(screen, ORANGE, [x_rock - 75, y_rock + 290, 150, 400])

    pygame.draw.rect(screen, light_blue, [x_rock - 20, y_rock + 60, 40, 40])

def ext(x_d, y_d, y_e):

    # Side1b

    pygame.draw.rect(screen, GREEN, [x_d - 120, y_d + 220, 20, y_e])

    # Side2b

    pygame.draw.rect(screen, GREEN, [x_d + 100, y_d + 220, 20, y_e])

def rocket_two(x_rock, y_rock):

    #head of the rocket

    pygame.draw.polygon(

        screen, RED,

        [[x_rock, y_rock], [x_rock + 30, y_rock + 20], [x_rock, y_rock + 40]])

    #body of the rocket

    pygame.draw.rect(screen, BLUE, [x_rock - 80, y_rock, 80, 40])

    #wings

    pygame.draw.rect(screen, WHITE, [x_rock - 60, y_rock - 30, 10, 30])

    pygame.draw.rect(screen, WHITE, [x_rock - 60, y_rock + 40, 10, 30])

    pygame.draw.polygon(

        screen, GRAY, [[x_rock - 80, y_rock], [x_rock - 80, y_rock + 40],

                       [x_rock - 90, y_rock + 50], [x_rock - 90, y_rock - 10]])

    #fire

    pygame.draw.polygon(

        screen, ORANGE,

        [[x_rock - 90, y_rock - 10], [x_rock - 90, y_rock + 50],

         [x_rock - 120, y_rock + 80], [x_rock - 120, y_rock - 40],

         [x_rock - 90, y_rock - 10]])

    pygame.draw.rect(screen, light_blue, [x_rock - 30, y_rock + 10, 20, 20])

x_d = 210

y_d = 10

def detachable(x_d, x_y):

    pygame.draw.rect(screen, WHITE, [x_d, y_d, 40, 10])

    pygame.draw.rect(screen, WHITE, [x_d, y_d + 90, 40, 10])

    #detachable sides

x_f = 150

def fish_1(x_f):

    pygame.draw.polygon(

        screen,

        YELLOW,

        [[x_f, 300], [x_f + 20, 320], [x_f, 340]],

    )

    pygame.draw.rect(screen, RED, [x_f - 20, 310, 20, 10])

    pygame.draw.rect(screen, BLUE, [x_f - 20, 320, 20, 10])

    pygame.draw.polygon(screen, GREEN,

                        [[x_f - 30, 310], [x_f - 30, 320], [x_f - 20, 320]])

    pygame.draw.polygon(screen, BLACK,

                        [[x_f - 30, 320], [x_f - 20, 320], [x_f - 30, 330]])

x_f = 150

def fish_2(x_fd):

    pygame.draw.polygon(

        screen,

        PURPLE,

        [[x_fd + 100, 300], [x_fd + 120, 320], [x_fd + 100, 340]],

    )

    pygame.draw.rect(screen, GRAY, [x_fd + 80, 310, 20, 10])

    pygame.draw.rect(screen, BROWN, [x_fd + 80, 320, 20, 10])

    pygame.draw.polygon(screen, PEACH,

                        [[x_fd + 70, 310], [x_f + 70, 320], [x_f + 80, 320]])

    pygame.draw.polygon(screen, BLACK,

                        [[x_fd + 70, 320], [x_fd + 80, 320], [x_fd + 70, 330]])

# ----------count down------------------------

# countdown audio

x_f = 150

x_fd = 250

while not done:

    # This limits the while loop to a max of 10 times per second.

    # Leave this out and we will use all CPU we can.

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but

    # inside the main while done==False loop.

    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # Clear the screen and set the screen background

    screen.fill(WHITE)

    # wall color in the background

    y = 0

    for i in range(30):

        x = 0

        for i in range(10):

            pygame.draw.rect(screen, PEACH, [x, y, 50, 10])

            x = x + 70

        y = y + 20

        x = 30

        for i in range(10):

            pygame.draw.rect(screen, PEACH, [x, y, 50, 10])

            x = x + 70

    # Draw a tv

    pygame.draw.rect(screen, GRAY, [150, 30, 310, 170], 20)

    pygame.draw.rect(screen, BLACK, [150, 30, 310, 170])

    # Draw a rectangle for the sound box one

    pygame.draw.rect(screen, BLACK, [10, 20, 100, 180])

    pygame.draw.rect(screen, RED, [10, 20, 100, 180], 3)

    # Draw a rectangle for the sound box two

    pygame.draw.rect(screen, BLACK, [500, 20, 100, 180])

    pygame.draw.rect(screen, RED, [500, 20, 100, 180], 3)

    # Drawing a rectangle for the aquarium

    pygame.draw.rect(screen, BLACK, [30, 250, 550, 150], 3)

    # Draw a circle inside the soundbox 1

    pygame.draw.circle(screen, RED, [60, 160], 5)

    pygame.draw.circle(screen, BLUE, [60, 160], 20, 5)

    pygame.draw.circle(screen, dark_red, [60, 160], 40, 5)

    pygame.draw.circle(screen, RED, [60, 60], 3)

    pygame.draw.circle(screen, BLUE, [60, 60], 15, 5)

    pygame.draw.circle(screen, dark_red, [60, 60], 35, 5)

    # Draw a circle inside the soundbox 2

    pygame.draw.circle(screen, RED, [550, 160], 5)

    pygame.draw.circle(screen, BLUE, [550, 160], 20, 5)

    pygame.draw.circle(screen, dark_red, [550, 160], 40, 5)

    pygame.draw.circle(screen, RED, [550, 60], 3)

    pygame.draw.circle(screen, BLUE, [550, 60], 15, 5)

    pygame.draw.circle(screen, dark_red, [550, 60], 35, 5)

    # drawing glass for the fish tank

    pygame.draw.rect(screen, light_blue, [30, 250, 550, 150])

    # plants in the fish tank

    pygame.draw.line(screen, YELLOW, [80, 400], [60, 340], 5)

    pygame.draw.line(screen, YELLOW, [80, 400], [100, 340], 5)

    x = 50

    for i in range(9):

        pygame.draw.line(screen, GREEN, [80, 400], [x, 360], 6)

        x = x + 10

    pygame.draw.line(screen, YELLOW, [220, 400], [230, 340], 5)

    pygame.draw.line(screen, YELLOW, [220, 400], [260, 340], 5)

    pygame.draw.line(screen, YELLOW, [220, 400], [200, 340], 5)

    # a playground for the fishes

    pygame.draw.line(screen, light_yellow, [390, 310], [390, 380], 4)

    pygame.draw.line(screen, light_yellow, [390, 310], [450, 330], 4)

    pygame.draw.line(screen, light_yellow, [390, 310], [430, 280], 4)

    pygame.draw.line(screen, light_yellow, [390, 380], [450, 400], 4)

    pygame.draw.line(screen, light_yellow, [450, 330], [450, 400], 4)

    pygame.draw.line(screen, light_yellow, [390, 380], [450, 400], 4)

    pygame.draw.line(screen, light_yellow, [390, 380], [430, 360], 4)

    pygame.draw.line(screen, light_yellow, [430, 360], [430, 280], 4)

    pygame.draw.line(screen, light_yellow, [430, 280], [480, 300], 4)

    pygame.draw.line(screen, light_yellow, [480, 300], [450, 330], 4)

    pygame.draw.line(screen, light_yellow, [480, 300], [480, 380], 4)

    pygame.draw.line(screen, light_yellow, [480, 380], [450, 400], 4)

    pygame.draw.line(screen, light_yellow, [430, 360], [480, 380], 4)

    # drawing more grass

    x = 190

    for i in range(9):

        pygame.draw.line(screen, GREEN, [220, 400], [x, 360], 6)

        x = x + 10

    x = 39

    y = 40

    a = 560

    # stones for the fish tank

    for i in range(10):

        pygame.draw.ellipse(screen, BROWN, [y, 380, 35, 25])

        y = y + 30

        pygame.draw.circle(screen, GRAY, [x, 390], 10)

        x = x + 35

        pygame.draw.ellipse(screen, GRAY, [y, 380, 20, 30])

        y = y + 20

        pygame.draw.circle(screen, BROWN, [a, 390], 15)

        a = a - 3

    # white reflection on the fish tank glass

    pygame.draw.line(screen, WHITE, [70, 270], [50, 300], 3)

    pygame.draw.line(screen, WHITE, [60, 270], [40, 300], 3)

    pygame.draw.line(screen, WHITE, [370, 270], [350, 300], 3)

    pygame.draw.line(screen, WHITE, [360, 270], [340, 300], 3)

    # Draw a display on the tv

    pygame.draw.arc(screen, YELLOW, [200, 75, 150, 125], 0, pi / 2, 2)

    pygame.draw.arc(screen, GREEN, [200, 75, 150, 125], pi / 2, pi, 2)

    pygame.draw.arc(screen, BLUE, [200, 75, 150, 125], pi, 3 * pi / 2, 2)

    pygame.draw.arc(screen, RED, [200, 75, 150, 125], 3 * pi / 2, 2 * pi, 2)

    pygame.draw.arc(screen, YELLOW, [260, 75, 150, 125], 0, pi / 2, 2)

    pygame.draw.arc(screen, GREEN, [260, 75, 150, 125], pi / 2, pi, 2)

    pygame.draw.arc(screen, BLUE, [260, 75, 150, 125], pi, 3 * pi / 2, 2)

    pygame.draw.arc(screen, RED, [260, 75, 150, 125], 3 * pi / 2, 2 * pi, 2)

    pygame.draw.arc(screen, YELLOW, [230, 35, 150, 125], 0, pi / 2, 2)

    pygame.draw.arc(screen, GREEN, [230, 35, 150, 125], pi / 2, pi, 2)

    pygame.draw.arc(screen, BLUE, [230, 35, 150, 125], pi, 3 * pi / 2, 2)

    pygame.draw.arc(screen, RED, [230, 35, 150, 125], 3 * pi / 2, 2 * pi, 2)

    # bubbles in the fish tank

    pygame.draw.circle(screen, WHITE, [240, 260], 5, 3)

    pygame.draw.circle(screen, WHITE, [250, 220], 5, 3)

    pygame.draw.circle(screen, WHITE, [260, 280], 5, 3)

    pygame.draw.circle(screen, WHITE, [270, 290], 5, 3)

    pygame.draw.circle(screen, WHITE, [250, 320], 5, 3)

    pygame.draw.circle(screen, WHITE, [170, 310], 5, 3)

    pygame.draw.circle(screen, WHITE, [190, 290], 5, 3)

    pygame.draw.circle(screen, WHITE, [280, 320], 5, 3)

    pygame.draw.circle(screen, WHITE, [290, 310], 5, 3)

    pygame.draw.circle(screen, WHITE, [300, 320], 5, 3)

    pygame.draw.circle(screen, WHITE, [310, 330], 5, 3)

    pygame.draw.circle(screen, WHITE, [270, 310], 5, 3)

    pygame.draw.circle(screen, WHITE, [310, 290], 5, 3)

    pygame.draw.circle(screen, WHITE, [320, 360], 5, 3)

    pygame.draw.circle(screen, WHITE, [350, 380], 5, 3)

    pygame.draw.circle(screen, WHITE, [380, 350], 5, 3)

    pygame.draw.circle(screen, WHITE, [370, 320], 5, 3)

    # draw fish house the fish tank

    pygame.draw.polygon(

        screen,

        RED,

        [[260, 340], [300, 300], [340, 340]],

    )

    pygame.draw.rect(screen, GREEN, [270, 340, 30, 40])

    pygame.draw.rect(screen, BLUE, [300, 340, 30, 40])

    # opening for fish tank

    pygame.draw.circle(screen, BLACK, [100, 300], 20, 5)

    pygame.draw.line(screen, RED, [100, 300], [120, 300], 4)

    # fishes in the fish tanks

    def fish_1(x_f):

        x_f += 10

    def fish_2(x_fd):

        x_fd -= 10

    # drawing more stones in the fish tank

    pygame.draw.circle(screen, GRAY, [550, 390], 10)

    pygame.draw.circle(screen, GRAY, [520, 390], 10)

    pygame.draw.circle(screen, GRAY, [570, 390], 10)

    # timer for the count down

    font = pygame.font.SysFont('Calibri', 65, True, False)

    showScreen = False

    # Render the text. "True" means anti-aliased text.

    # Black is the color. The variable BLACK was defined

    # above as a list of [0, 0, 0]

    # Note: This line creates an image of the letters,

    # but does not put it on the screen yet.

    if count < 0:

        showScreen = True

    else:

        text = font.render(str(count), True, WHITE)

    count = count - 1

    # Put the image of the text on the screen at 250x250

    screen.blit(text, [285, 90])

    # TV screen getting bigger

    if showScreen:

        xval = 80

        for i in range(13):

            pygame.draw.rect(screen, GRAY, [0, 0, xval, xval])

            pygame.display.flip()

            xval = xval + 50

            pygame.time.delay(100)

            done = True

    pygame.display.flip()

    clock.tick(1)

    # Go ahead and update the screen with what we've drawn.

    # This MUST happen after all the other drawing commands.

    pygame.display.flip()

# end scene 2

done = False

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# ----------scene 1---------------------------

x_rock = 450

y_rock = 20

#clapping music

while not done:

    # This limits the while loop to a max of 10 times per second.

    # Leave this out and we will use all CPU we can.

    clock.tick(10)

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but

    # inside the main while done==False loop.

    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # Clear the screen and set the screen background

    screen.fill(SKYBLUE)

    # Background

    # Nasa building

    pygame.draw.rect(screen, MAROON, [0, 210, 660, 140])

    # Building glass

    x = 20

    for i in range(7):

        pygame.draw.rect(screen, GLASS, [x, 240, 40, 30])

        # line on the glass

        pygame.draw.line(screen, WHITE, [x, 240], [x + 5, 245], 2)

        x += 100

    x = 20

    for i in range(7):

        pygame.draw.rect(screen, GLASS, [x, 300, 40, 30])

        # line on the glass

        pygame.draw.line(screen, WHITE, [x, 300], [x + 5, 305], 2)

        x += 100

    # road and line

    pygame.draw.rect(screen, ROAD, [0, 350, 660, 50])

    x = 10

    for i in range(5):

        pygame.draw.rect(screen, WHITE, [x, 380, 60, 10])

        x += 150

    font = pygame.font.SysFont('Impact', 25, True, False)

    text = font.render("NASA", True, WHITE)

    screen.blit(text, [220, 210])

    # stand

    pygame.draw.rect(screen, SILVER, [590, 130, 70, 270])

    # ladder

    pygame.draw.rect(screen, STEEL, [390, 130, 200, 50])

    rocket(x_rock, y_rock)

    y_rock = y_rock - 5

    if y_rock == -250:

        done = True

    pygame.display.flip()

    clock.tick(60)

    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # Go ahead and update the screen with what we've drawn.

    # This MUST happen after all the other drawing commands.

    pygame.display.flip()

#end scene 2--------

done = False

#start scene 3

x_rock = 300

y_rock = 40

background = (0, 0)

rocketbell = 200

background_image = pygame.image.load("postbg95255.jpg").convert()

background_image = pygame.transform.scale(background_image, (660, 400))

while not done:

    # This limits the while loop to a max of 10 times per second.

    # Leave this out and we will use all CPU we can.

    clock.tick(10)

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but

    # inside the main while done==False loop.

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Clear the screen and set the screen background

    screen.blit(background_image, background)

    #Generates smaller engine plume thorugh randomly genereated rectangles

    for i in range(4):

        pointx = randint(rocketbell - 100, rocketbell)

        pointy = randint(0, 130)

        length = randint(20, 70)

        width = randint(3, 20)

        pygame.draw.rect(screen, RED, [pointx, pointy, length, width])

        pygame.draw.rect(screen, ORANGE, [pointx, pointy, length, width], 2)

        rocketbell = rocketbell + 1

    for i in range(4):

        pointx = randint(rocketbell - 100, rocketbell)

        pointy = randint(0, 130)

        length = randint(20, 70)

        width = randint(3, 20)

        pygame.draw.rect(screen, ORANGE, [pointx, pointy, length, width])

        pygame.draw.rect(screen, RED, [pointx, pointy, length, width], 2)

    #moves rocket across screen and moves detached boosters

    rocket_two(x_rock, y_rock)

    x_rock = x_rock + 5

    detachable(x_d, y_d)

    y_d = y_d + 2

    x_d = x_d + 7

    if x_rock == 720:

        done = True

    pygame.display.flip()

    clock.tick(60)

    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # Go ahead and update the screen with what we've drawn.

    # This MUST happen after all the other drawing commands.

    pygame.display.flip()

done = False

#-----Extending out the engines---------------------

x_rock = 550

y_rock = 5

x_d = 550

y_d = 5

y_e = 1

background = (0, 0)

background_image = pygame.image.load(

    "Rocket - Scene 4 BackGround.jpg").convert()

background_image = pygame.transform.scale(background_image, (660, 400))

while not done:

    # This limits the while loop to a max of 10 times per second.

    # Leave this out and we will use all CPU we can.

    clock.tick(10)

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but

    # inside the main while done==False loop.

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Clear the screen and set the screen background

    screen.blit(background_image, background)

    rocket(x_rock, y_rock)

    y_rock = y_rock + 1

    ext(x_d, y_d, y_e)

    y_d = y_d + 1

    y_e = y_e + 1

    if y_e == 20:

        done = True

    pygame.display.flip()

    clock.tick(60)

    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # Go ahead and update the screen with what we've drawn.

    # This MUST happen after all the other drawing commands.

    pygame.display.flip()

done = False

#-------FInal scene-------------

background = (0, 0)

#Michael here, invading the code (if this doesn't work, I have organized it in chunks for easy deletion)

#Loading images and initial co-ordinates of a smaller spacecraft. It will fly across the top of the screen, just to add a bit to the background.

orion = pygame.image.load("Orion-ESM_B.bmp").convert()

orion.set_colorkey(WHITE)

orion_x = 800

orion_y = 0

background_image = pygame.image.load(

    "Rocket - Scene 11b BackGround.jpg").convert()

background_image = pygame.transform.scale(background_image, (660, 400))

x_rock = 320

y_rock = -100

while not done:

    # This limits the while loop to a max of 10 times per second.

    # Leave this out and we will use all CPU we can.

    clock.tick(10)

    for event in pygame.event.get():  # User did something

        if event.type == pygame.QUIT:  # If user clicked close

            done = True  # Flag that we are done so we exit this loop

    # All drawing code happens after the for loop and but

    # inside the main while done==False loop.

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# Clear the screen and set the screen background

    frame = 65

    delta = 5

    screen.blit(background_image, background)

    #Michael here again, this chunk moves Orion across the screen

    screen.blit(orion, [orion_x, orion_y])

    orion_x = orion_x - 30

    #Moves main rocket across screen and ends animation

    rocket(x_rock, y_rock)

    y_rock = y_rock + delta

    if y_rock == 190:

        done = True

    #Prints "Thank you for watching" in bold font

    font = pygame.font.SysFont('BOLD', 30, True, False)

    text = font.render("Thank you for watching", True, WHITE)

    screen.blit(text, [10, 180])

    pygame.display.flip()

    clock.tick(frame)

    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    # Go ahead and update the screen with what we've drawn.

    # This MUST happen after all the other drawing commands.

    pygame.display.flip()

done = False

# Be IDLE friendly

pygame.quit()

