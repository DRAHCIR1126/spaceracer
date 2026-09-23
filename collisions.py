def check_boundary_collision():
    """
    Detect when the player collides with the wall
    On collision, play a sound and reduce player lives
    Also turn the player 180 degrees
    """

    global LIVES
    if player.xcor() > 290 or player.xcor() < -290:  # check x coordinates
        player.right(180)  # turn 180 derees
        playsound(SOUND_HURT)
        LIVES -= 1
        update_lives()
    elif player.ycor() > 290 or player.ycor() < -290:  # check y coordinates
        player.left(180)
        playsound(SOUND_HURT)
        LIVES -= 1
        update_lives()


def check_star_collision():
    """
    Detect when the player collides with a star
    On collision, play a sound and increase player score
    Also generate a new star
    """

    global SCORE, INITIAL_TIME
    if is_collision(player, star):
        star.setposition(random.randint(-290, 290), random.randint(-290, 290))  # set star in new position
        INITIAL_TIME = int(time.time())  # refresh starting time for new star
        SCORE += 1  # increase score by 1
        update_score()
        playsound(SOUND_STAR)


def check_enemy_collision():
    """
    Detect when the player collides with the enemy
    On collision, play a sound and decrease player lives
    Also move the enemy to a random location
    """
    global LIVES
    if abs(player.xcor() - enemy.xcor()) < 10 and abs(player.ycor() - enemy.ycor()) < 10:
        playsound(SOUND_EXPLOSION)
        LIVES -= 1
        enemy.setposition(random.randint(-290, 290), random.randint(-290, 290))


def is_collision(entity1, entity2):
    """
    Check for collisions between two entities.
    If entities are within 9 pixels of each other, this is seen as a collision.
    :param entity1: the first entity (Ex: the player)
    :param entity2: the second entity (Ex: the enemy or a star)
    :return: true if a collision is detected
    """

    if abs(entity1.xcor() - entity2.xcor()) < 9 and abs(entity1.ycor() - entity2.ycor()) < 9:
        return True
    else:
        return False
