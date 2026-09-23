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
