import os
import random
import turtle
from turtle import Turtle
from turtle import Screen
import time
from playsound3 import playsound

# Initial parameters
pace = 5
score = 0
lives = 5
game_over = False

# Images & sounds
star_image = "images/star.gif"
sound_hurt = "sounds/hurt2.wav"
sound_gameover = "sounds/gameover4.wav"
sound_star = "sounds/coin3.wav"
sound_explosion = "sounds/explosion1.wav"

# Initialise Turtle
window = Screen()
player = Turtle()
enemy = Turtle()
star = Turtle()

# Time
Initial_time = int(time.time())


# Window
def set_window():
    window.setup(width=1280, height=720)
    window.title("SpaceRacer")
    window.bgcolor("black")
    window.bgpic("images/spacebgrnd.gif")
    window.tracer(False)


# Border
def border():
    border = Turtle()
    border.color("white")
    border.penup()
    border.setposition(-300, -300)
    border.pendown()
    border.pensize(5)
    for i in range(4):
        border.forward(600)
        border.left(90)
    border.hideturtle()


# Player images(all angles)
def create_player():
    for i in range(0, 390, 30):
        file_name = "images/ship" + str(i) + ".gif"
        Screen().register_shape(file_name)
    player.shape('images/ship0.gif')
    player.penup()
    player.speed("normal")


# Enemy images(all angles)
def create_enemy():
    for i in range(0, 390, 30):
        file_name = "images/enemy" + str(i) + ".gif"
        Screen().register_shape(file_name)
    enemy.shape('images/enemy0.gif')
    enemy.penup()
    enemy.speed('normal')
    enemy.setposition(50, 50)
    enemy.setheading(0)


# Star
def create_star():
    Screen().register_shape(star_image)
    star.shape(star_image)
    star.penup()
    star.speed(0)


# Control
def init_controls():
    """
    Listen for keyboard controls
    """

    # set response via keyboard
    turtle.listen()  # open event handling to turtle

    # move turtle using arrow keys
    turtle.onkey(turn_left, "Left")
    turtle.onkey(turn_right, "Right")
    turtle.onkey(increase_speed, "Up")
    turtle.onkey(decrease_speed, "Down")

    # move turtle using WASD (gamers mode)
    turtle.onkey(turn_left, "A")
    turtle.onkey(turn_left, "a")
    turtle.onkey(turn_right, "D")
    turtle.onkey(turn_right, "d")
    turtle.onkey(increase_speed, "W")
    turtle.onkey(increase_speed, "w")
    turtle.onkey(decrease_speed, "S")
    turtle.onkey(decrease_speed, "s")

    # New game?
    turtle.onkey(check_exit, "N")
    turtle.onkey(check_exit, "n")
    turtle.onkey(restart_game, "Y")
    turtle.onkey(restart_game, "y")


def update_player_image():
    heading = int(player.heading())
    if heading % 30 != 0:
        heading = int(30 * round(player.heading() / 30.))
    file_name = "images/ship" + str(heading) + ".gif"
    player.shape(file_name)


def update_enemy_image():
    heading = int(30 * round(player.heading() / 30.))
    file_name = "images/enemy" + str(heading) + ".gif"
    enemy.shape(file_name)


# Player controlling (Keyboard)
def turn_left():
    player.left(30)
    update_player_image()


def turn_right():
    player.right(30)
    update_player_image()


# Speed
def increase_speed():
    global pace
    if pace < 800:  # todo change
        pace += 1


def decrease_speed():
    global pace
    if pace > 1:
        pace -= 1


# Player has no lives and doesn't want to play anymore
def check_exit():
    if lives == 0:
        os._exit(0)


def restart_game():
    global game_over
    if game_over:
        clear_gameover()
        game_over = False
        player.setposition(random.randint(-290, 290), random.randint(-290, 290))
        start()


def generate_star():
    star.setposition(random.randint(-290, 290), random.randint(-290, 290))


def check_generate_star():
    global Initial_time
    now = int(time.time())
    if now - Initial_time > 10:
        generate_star()
        Initial_time = int(time.time())


def enemy_action():
    heading = enemy.towards(player.xcor(), player.ycor())
    enemy.setheading(heading)
    update_enemy_image()
    enemy.forward(pace - 2 if pace > 3 else 3)


def is_collision(entity1, entity2):
    if abs(entity1.xcor() - entity2.xcor()) < 9 and abs(entity1.ycor() - entity2.ycor()) < 9:
        return True
    else:
        return False


def check_enemy_collision():
    global lives
    if is_collision(player, enemy):
        playsound(os.getcwd() + '/' + sound_explosion)
        lives -= 1
        update_lives()
        enemy.setposition(random.randint(-290, 290), random.randint(-290, 290))
        update_enemy_image()


def check_star_collision():
    global score, Initial_time
    if is_collision(player, star):
        star.setposition(random.randint(-290, 290), random.randint(-290, 290))
        Initial_time = int(time.time())
        score += 1
        update_score()
        playsound(os.getcwd() + '/' + sound_star)


def check_boundary_collision():
    global lives
    if player.xcor() > 290 or player.xcor() < -290:
        player.right(180)
        update_player_image()
        lives -= 1
        playsound(os.getcwd() + '/' + sound_hurt)
        update_lives()
    elif player.ycor() > 290 or player.ycor() < -290:
        player.left(180)
        update_player_image()
        lives -= 1
        playsound(os.getcwd() + '/' + sound_hurt)
        update_lives()


def update_lives():
    """
    Update the lives area when the number of lives changes.
    """
    lives_offset_width = 100  # x offset
    lives_offset_height = 200  # y offset
    window.tracer(False)  # do not animate drawing
    lives_area = turtle.Turtle()
    lives_area_font = ('arial', '18', 'bold')
    lives_area.ht()  # hide the turtle

    text = 'Lives: ' + str(lives)

    # Clear text
    clear_texts(lives_area, lives_offset_width, lives_offset_height)

    # Write text
    lives_area.color("red")
    lives_area.write(text, font=lives_area_font, move=False)
    window.tracer(True)


def update_score():
    """
    Update the score area when the score changes
    """
    score_offset_width = 100  # x offset
    score_offset_height = 100  # y offset
    window.tracer(False)  # do not animate drawing
    score_area = turtle.Turtle()
    score_area_font = ('arial', '18', 'bold')
    score_area.ht()  # hide the turtle

    text = 'Score: ' + str(score)

    # Clear text
    clear_texts(score_area, score_offset_width, score_offset_height)

    # Write text
    score_area.color("blue")
    score_area.write(text, font=score_area_font, move=False)
    window.tracer(True)


def clear_texts(area_turtle, offset_width, offset_height):
    screen = turtle.Screen()
    area_turtle.penup()
    area_turtle.goto(offset_width / 2 - screen.window_width() / 2, screen.window_height() / 2 - offset_height / 2)
    area_turtle.pendown()
    area_turtle.color(turtle.bgcolor())
    area_turtle.begin_fill()
    area_turtle.fd(160)
    area_turtle.setheading(90)
    area_turtle.fd(30)
    area_turtle.setheading(180)
    area_turtle.fd(160)
    area_turtle.setheading(270)
    area_turtle.fd(30)
    area_turtle.setheading(0)
    area_turtle.fd(10)
    area_turtle.end_fill()


def game_loop():
    global lives, score, Initial_time, game_over
    Initial_time = int(time.time())

    generate_star()
    update_score()
    update_lives()

    while lives > 0:
        player.forward(pace)
        enemy_action()
        check_generate_star()
        check_boundary_collision()
        check_star_collision()
        check_enemy_collision()
    game_over = True
    playsound(os.getcwd() + '/' + sound_gameover)
    draw_gameover()
    while game_over:
        enemy_action()


def draw_gameover():
    text_offset_width = 950
    text_offset_height = 1435
    text2_offset_width = 920
    text2_offset_height = 1500
    window.tracer(False)
    gameover_area = turtle.Turtle()
    gameover_area_font = ('arial', '18', 'bold')
    gameover_area.ht()

    text = 'GAME OVER'
    text2 = 'NEW GAME? Y/N'

    # Clear text
    clear_text(gameover_area, text_offset_width, text_offset_height)

    # Write text
    gameover_area.color("red")
    gameover_area.write(text, font=gameover_area_font, move=False)

    # Clear text 2
    clear_text(gameover_area, text2_offset_width, text2_offset_height)

    # Write text 2
    gameover_area.color("blue")
    gameover_area.write(text2, font=gameover_area_font, move=False)

    window.tracer(True)


def clear_text(area_turtle, offset_width, offset_height):
    screen = turtle.Screen()
    area_turtle.penup()
    area_turtle.goto(offset_width / 2 - screen.window_width() / 2, screen.window_height() / 2 - offset_height / 2)
    area_turtle.pendown()
    area_turtle.color(turtle.bgcolor())
    area_turtle.begin_fill()
    area_turtle.fd(160)
    area_turtle.setheading(90)
    area_turtle.fd(30)
    area_turtle.setheading(180)
    area_turtle.fd(160)
    area_turtle.setheading(270)
    area_turtle.fd(30)
    area_turtle.setheading(0)
    area_turtle.fd(10)
    area_turtle.end_fill()


def clear_gameover():
    """
    Clear the game over text area
    """
    text_offset_width = 950
    text_offset_height = 1435
    text2_offset_width = 910
    text2_offset_height = 1500
    gameover_area = turtle.Turtle()
    gameover_area.ht()
    window.tracer(False)
    clear_text(gameover_area, text_offset_width, text_offset_height)
    clear_text(gameover_area, text2_offset_width, text2_offset_height)
    window.tracer(True)


# Starting the game
def start():
    global pace, score, lives
    pace = 5
    score = 0
    lives = 3

    set_window()
    border()
    window.update()
    window.tracer(True)

    create_player()
    create_enemy()
    create_star()

    init_controls()
    game_loop()


start()