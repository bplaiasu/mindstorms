"""In this step the robot resolves MISSION 5, 6, 7, 9 and 10"""

from functions import move_straight, turn
from pybricks.tools import wait


def run(robot, left_motor, right_motor, attachment_motor1, attachment_motor2):
    attachment_motor1.run_target(500, 0)
    attachment_motor2.run_target(500, 0)
    attachment_motor1.run_angle(600, 400)
    attachment_motor2.run_angle(500, -200)
    # robot.settings(straight_speed=200)
    move_straight(robot, 700)
    move_straight(robot, -75)
    right_motor.run_angle(150, 200)
    move_straight(robot, -30)
    right_motor.run_angle(150, 150)
    move_straight(robot, -235)
    attachment_motor2.run_angle(300, 200)
    move_straight(robot, -115)
    attachment_motor2.run_angle(250, -200)
    move_straight(robot, 250)
    left_motor.run_angle(200, 170)
    right_motor.run_angle(200, -150)
    move_straight(robot, -320)
    right_motor.run_angle(300, 148)
    move_straight(robot, 70)
    right_motor.run_angle(500, 85)
    move_straight(robot, -150)
    left_motor.run_angle(500, -180)
    move_straight(robot, 390)
    left_motor.run_angle(500, 385)
    move_straight(robot, -13)
    attachment_motor1.run_angle(1000, -400)
    move_straight(robot, -50)
    attachment_motor2.run_target(500, 0)
    attachment_motor1.run_target(500, 0)
