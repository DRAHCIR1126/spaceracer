def clear_text(area_turtle, offset_width, offset_height):
    """
    Clear an area before overwriting it
    :param area_turtle: the turtle for the area to clear
    :param offset_width: the x offset of the area
    :param offset_height: the y offset of the area
    """

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
