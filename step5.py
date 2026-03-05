"""
In this step the robot resolves MISSION
    - apucarea cartului
    - steag 2
    - 13 !!!!???
    - 14
    - steag 3
Execution time:  sec
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

    # Raise arm of motorF
    attachment_motor2.run_angle(350, 70)

    # ------------------------
    # -- Going to pick cart --
    # ------------------------
    move_straight(robot, 485)
    robot.stop()
    robot.settings(turn_rate=100, turn_acceleration=100)
    arc(robot, -30, 40)
    # robot.settings(turn_rate=200, turn_acceleration=200)
    move_straight(robot, 500)
    attachment_motor2.run_angle(350, 50)
    move_straight(robot, -80)
    arc(robot, -30, 50)

    # -----------------------
    # -- Put the cart down --
    # -----------------------
    move_straight(robot, 575)
    arc(robot, -30, 38)
    move_straight(robot, 110)
    arc(robot, -30, 40)
    attachment_motor2.run_angle(150, -75)

    # ----------------------------
    # -- Put down the artefacts --
    # ----------------------------
    move_straight(robot, -80)
    arc(robot, -30, -60)
    move_straight(robot, 150)
    attachment_motor1.run_angle(750, -130)

    # ------------------------
    # -- Put down flag no.3 --
    # ------------------------
    move_straight(robot, 80)
    arc(robot, -30, -23)
