from utils.types import Direction

def getDirection(x_speed, y_speed):
    if x_speed == 0:
        if y_speed > 0:
            return Direction.DOWN
        elif y_speed < 0:
            return Direction.UP
    elif y_speed == 0:
        if x_speed > 0:
            return Direction.LEFT
        elif x_speed < 0:
            return Direction.RIGHT

def isFoodEaten(x_snake_pos, y_snake_pos,
        x_food_pos, y_food_pos):
    return (x_snake_pos == x_food_pos and
            y_snake_pos == y_food_pos)

