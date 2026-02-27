"""
In this step the robot resolves MISSION 5, 6, 7, 9 and 10
Execution time: 38 sec
"""

from functions import move_straight, turn, arc
from pybricks.tools import wait


def run(
    robot,
    left_motor=None,
    right_motor=None,
    attachment_motor1=None,
    attachment_motor2=None,
):
    attachment_motor1.run_target(250, 0)
    attachment_motor2.run_target(250, 0)

    # Reset motors to 0 angle if arms aren't in the original position
    if attachment_motor1.angle() < 10 or attachment_motor1.angle() > -10:
        attachment_motor1.run_angle(350, -attachment_motor1.angle())
        attachment_motor1.run_target(350, 0)
    if attachment_motor2.angle() < 10 or attachment_motor2.angle() > -10:
        attachment_motor2.run_angle(350, -attachment_motor2.angle())
        attachment_motor2.run_target(350, 0)

    # Raise the arms
    attachment_motor1.run_angle(350, -100)
    attachment_motor2.run_angle(350, -170)

    # ----------------------
    # -- MISSION no.7 & 5 --
    # ----------------------
    move_straight(robot, 740)
    move_straight(robot, -55)
    right_motor.run_angle(150, 170)
    move_straight(robot, -45)
    right_motor.run_angle(150, 189)
    move_straight(robot, -285)
    attachment_motor2.run_angle(350, 170)
    move_straight(robot, -160)
    attachment_motor2.run_angle(250, -170)

    # ------------------
    # -- MISSION no.9 --
    # ------------------
    move_straight(robot, 420)
    left_motor.run_angle(200, 170)
    move_straight(robot, -75)
    right_motor.run_angle(200, -250)
    move_straight(robot, -290)
    right_motor.run_angle(200, 220)
    move_straight(robot, -160)

    # Turn right
    arc(robot, -50, -120)

    # -------------------
    # -- MISSION no.10 --
    # -------------------
    move_straight(robot, -325)

    # Turn left
    robot.settings(
        turn_rate=200,
        turn_acceleration=200,
    )
    arc(robot, -30, 90)
    move_straight(robot, 80)
    attachment_motor1.run_angle(350, 106)
    robot.settings(
        straight_speed=50,
        straight_acceleration=50,
        turn_rate=50,
        turn_acceleration=50,
    )
    move_straight(robot, -100)

    # ------------------
    # -- BASE TO Base --
    # ------------------
    robot.settings(
        straight_speed=200,
        straight_acceleration=200,
        turn_rate=50,
        turn_acceleration=50,
    )
    turn(robot, -90)
    move_straight(robot, -600)
