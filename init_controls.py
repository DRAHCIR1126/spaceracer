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
    turtle.onkey(reset_game, "Y")
    turtle.onkey(reset_game, "y")
