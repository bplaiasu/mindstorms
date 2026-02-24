"""In the first step the robot needs to go to points 1, 2 and 3"""

from functions import move_straight, arc, turn


def run(robot):
    move_straight(robot, 200)
    arc(robot, 100, 35)
    move_straight(robot, 200)
    turn(robot, 180)
    move_straight(robot, 300)
