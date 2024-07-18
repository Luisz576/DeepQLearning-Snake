LEFT = 1
TOP = 2
RIGHT = 3
BOTTOM = 4


def new_direction_based_on_turn_left_or_right(current_direction, is_left):
    new_direction = current_direction
    if is_left:
        new_direction += 1
        if new_direction > 4:
            new_direction = 1
    else:
        new_direction -= 1
        if new_direction < 1:
            new_direction = 4
    return new_direction
