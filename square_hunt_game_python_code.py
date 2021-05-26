import threading
import time
import random
import turtle
from turtle import setup
from turtle import textinput

# -------------------------------------------------------------------------------------------------------------------
# Variable declarations
# -------------------------------------------------------------------------------------------------------------------
side = 0  # This variable stores the size of each square of the grid created
x_cord = 0  # This variable stores the randomly generated x-coordinates for flashing squares within grid
y_cord = 0  # This variable stores the randomly generated y-coordinates for flashing squares within grid
score_inc = 0  # This variable stores the score made by user
missedClick = 0  # This variable stores the number of misses by user while playing game
counter = 0  # This variable displays the total number of squares displayed with the grid throughout the game.


# -------------------------------------------------------------------------------------------------------------------
#   Function declarations used throughout the code
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
#   Next 2 functions are to handle incorrect user inputs
# -------------------------------------------------------------------------------------------------------------------
def incorrect_grid_input():  # This function will be called upon incorrect input for Grid size
    global m, level, diff_level, user_input
    turt.goto(-200, 0)
    turt.write(str(m) + ' is Invalid grid size.\nKindly enter grid size between 3 and 6', font=("Calibre", 18, "bold"))
    user_input = int(turtle.textinput('Grid Size', 'Enter grid size between 3 to 6: '))
    m = user_input
    if m in (3, 4, 5, 6):
        turt.undo()
        difficulty_level_input()


def difficulty_level_input():  # This function will be called upon incorrect input for Game level
    global level, diff_level, side
    diff_level = int(turtle.textinput('Difficulty Level', 'Enter difficulty level from 1 to 3: '))
    level = diff_level
    if level in (1, 2, 3):  # While loop starts until correct input is obtained from user
        turt.goto(-200, 0)
        turt.pendown()
        turt.pencolor('white')
        turt.begin_fill()
        turt.fillcolor('white')
        for i in range(2):
            turt.forward(600)
            turt.left(90)
            turt.forward(200)
            turt.left(90)
        turt.end_fill()
        turt.penup()
        if m == 6:
            side = 116
        elif m == 5:
            side = 140
        elif m == 4:
            side = 175
        else:
            side = 233
        row_of_rows(m, side)
    else:
        turt.goto(-200, 0)
        turt.write(str(level) + ' is Invalid difficulty level.\nKindly enter difficulty level between 1 and 3', font=("Calibre", 18, "bold"))
        difficulty_level_input()


# -------------------------------------------------------------------------------------------------------------------
#   Next 3 functions are to draw a grid for game play according to user input
# -------------------------------------------------------------------------------------------------------------------
def square(side):  # This function will be called to draw a square to create game grid
    for i in range(4):
        turt.forward(side)
        turt.left(90)


def row(m, side):  # This function will be called to make rows of square
    for i in range(m):
        turt.pencolor("maroon")
        turt.pensize(2)
        square(side)  # This function draws a square
        turt.forward(side)
    turt.penup()
    turt.left(180)
    turt.forward(m * side)
    turt.left(180)
    # turt.pendown()
    # turt.pencolor('white')


def row_of_rows(m, side):  # This function will be called to make rows of rows of square
    turt.penup()
    turt.goto(-350, -375)
    turt.pendown()
    for i in range(m):
        row(m, side)  # This function starts drawing squares from given coordinates in a row
        turt.penup()
        turt.left(90)
        turt.forward(side)
        turt.right(90)
        turt.pendown()
    turt.penup()
    turt.right(90)
    turt.forward(m * side)
    turt.left(90)


# -------------------------------------------------------------------------------------------------------------------
#   Next 2 functions are to handle clicks by user to start game and later to start flashing squares to be hit at by user
# -------------------------------------------------------------------------------------------------------------------
def next_square():
    global counter, missedClick
    for r in range(10):
        turt.penup()
        turt.pencolor('black')
        turt.goto(20, 345)
        turt.pendown()
        turt.begin_fill()
        turt.color('white')
        for i in range(4):
            turt.forward(side)
            turt.left(90)
        turt.end_fill()
        turt.goto(20, 345)
        turt.pencolor('black')
        turt.pendown()
        turt.write('[' + str(r + 1) + ']', font=("Calibre", 18, "bold"))
        turt.penup()
        print(missedClick)
        if missedClick <= 2:
            display_score()
            square_fill()
        else:
            turt.penup()
            turt.pencolor('black')
            turt.goto(-200, -50)
            turt.write("GAME OVER", font=("Calibre", 50, "bold"))
            time.sleep(2)
            turt.reset()
    threading.Timer(2, next_square).start()


def display_score():
    turt.penup()
    turt.pencolor('black')
    turt.goto(295, 345)
    turt.pendown()
    turt.begin_fill()
    turt.color('white')
    for i in range(4):
        turt.forward(side)
        turt.left(90)
    turt.end_fill()
    turt.pendown()
    turt.goto(200, 345)
    turt.pendown()
    turt.pencolor('black')
    if score_inc <= 0:
        turt.write('SCORE: 0', font=("Calibre", 18, "bold"))
    else:
        turt.write('SCORE: ' + str(score_inc), font=("Calibre", 18, "bold"))
    turt.pencolor('white')
    turt.penup()


def handle_click(x, y):
    if 0 < x < 100 and 345 < y < 395:
        turt.pencolor('white')
        turt.goto(-12.5, 336)
        turt.pendown()
        turt.begin_fill()
        turt.fillcolor("white")
        for i in range(2):
            turt.forward(101)
            turt.left(90)
            turt.forward(51)
            turt.left(90)
        turt.end_fill()
        turt.penup()
        print('Detected a click for START button at: ', x, y)
        turt.goto(-12.5, 336)
        turt.write('[')
        next_square()


# -------------------------------------------------------------------------------------------------------------------
#   Next 3 functions are to draw flashing squares within grid to be hit by user
# -------------------------------------------------------------------------------------------------------------------
def inner_square(side):  # This function will be called to draw the squares that flashes within the grid.
    turt.pensize(2)
    for i in range(4):
        turt.forward(side - 10)
        turt.left(90)


def square_fill():  # This function will draw squares RANDOMLY across the grid created for user to hit.
    global x_cord, counter
    x_cord = random.randrange(-350, 350 - side, side)
    global y_cord
    y_cord = random.randrange(-375, 325 - side, side)
    turt.forward(10)
    turt.penup()
    turt.goto(x_cord + 5, y_cord + 5)
    turt.pendown()
    turt.begin_fill()
    turt.fillcolor('green')
    inner_square(side)
    turt.end_fill()
    turt.penup()
    if level == 1:
        time.sleep(2)
    elif level == 2:
        time.sleep(1.5)
    else:
        time.sleep(1)
    turtle.listen()
    turtle.onscreenclick(score_count)
    turt.goto(x_cord + 5, y_cord + 5)
    turt.pendown()
    turt.begin_fill()
    turt.fillcolor('white')
    inner_square(side)
    turt.end_fill()
    turt.penup()


# -------------------------------------------------------------------------------------------------------------------
#   Next functions is to keep track of score during game play
# -------------------------------------------------------------------------------------------------------------------
def score_count(x, y):  # This function will be called to calculate HIT/MISS score during game play
    global score_inc, missedClick
    if x_cord <= x <= (x_cord + side) and y_cord <= y <= (y_cord + side):
        turt.goto(x_cord + 5, y_cord + 5)
        turt.pendown()
        turt.begin_fill()
        turt.fillcolor('sky blue')
        inner_square(side)
        turt.end_fill()
        turt.penup()
        print('HIT')
        score_inc = score_inc + 1
    else:
        missedClick = missedClick + 1
        print('MISSED')
        if score_inc < 0:
            score_inc = 0
        else:
            score_inc = score_inc - 1


# --------------------------------------------------------------------------------------------------------------------
# Setting turtle
# --------------------------------------------------------------------------------------------------------------------
turt = turtle.Turtle()  # creating an instance of turtle
turt.speed(0)  # Setting turtle speed as fastest
setup(750, 800)  # Setting game screen as 750 x 800
turt.hideturtle()  # Hiding turtle to avoid lines shown on game screen
turt.penup()  # Pen Up to avoid lines shown on game screen
# --------------------------------------------------------------------------------------------------------------------
# Start creating a START button to start game.
# --------------------------------------------------------------------------------------------------------------------
turt.goto(-12, 337.5)  # Turtle pointer set at x =-12 and y = 337.5
turt.pendown()  # Pen Down to start drawing using turtle
turt.fillcolor("turquoise")  # Button colour set to Turquoise
turt.begin_fill()  # This functions will fill the button drwan in Turquoise colour
for i in range(2):  # For loop to draw Button borders
    turt.forward(100)
    turt.left(90)
    turt.forward(50)
    turt.left(90)
turt.end_fill()  # This functions stops colour fill
turt.penup()  # Pen Up to avoid lines shown on game screen
turt.goto(-350, 345)  # Turtle pointer set at x =-350 and y = 345 to write name of the game
turt.write("Square Hunt", font=("Calibre", 18, "bold"))  # This function helps in writing TEXT on turtle screen
turt.goto(0, 345)
turt.write("START", font=("Calibre", 18, "bold"))
# turt.goto(350, 345)
# turt.write("Score: ", font=("Calibre", 18, "bold"))
# -------------------------------------------------------------------------------------------------------------------
# Main code
# -------------------------------------------------------------------------------------------------------------------
user_input = int(turtle.textinput('Grid Size', 'Enter grid size between 3 to 6: '))  # Takes user input for grid size
m = user_input  # Assigns variable 'm' with user's grid size input
if m in (3, 4, 5, 6):  # For loop to check if input is correct
    difficulty_level_input()
else:
    incorrect_grid_input()
turt.hideturtle()
turtle.listen()  # This function will listen to user's clicks
turtle.onscreenclick(handle_click)  # This function will call handle_click() function whenever user clicks to check
# further conditions.
turtle.done()  # Stops turtle screen from closing
