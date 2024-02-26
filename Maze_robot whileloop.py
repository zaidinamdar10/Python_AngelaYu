def turn_right():
    turn_left()
    turn_left()
    turn_left()
def ex():
    turn_right()
    if wall_in_front():
        turn_left()
    else:
        move()
    while wall_on_right():
        if wall_in_front():
            turn_left()
        else:
              move()
  
    while front_is_clear():
        move()

while not at_goal():
    if front_is_clear():
        move()
    else:
        ex()


    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
