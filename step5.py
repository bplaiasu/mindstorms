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
    motor_e=None,
    motor_f=None,
):
    motor_e.run_target(250, 0)
    motor_f.run_target(250, 0)

    # Reset motors to 0 angle if arms aren't in the original position
    if motor_e.angle() < 10 or motor_e.angle() > -10:
        motor_e.run_angle(350, -motor_e.angle())
        motor_e.run_target(350, 0)
    if motor_f.angle() < 10 or motor_f.angle() > -10:
        motor_f.run_angle(350, -motor_f.angle())
        motor_f.run_target(350, 0)

    # Raise arm of motorF
    motor_f.run_angle(350, 70)

    # ------------------------
    # -- Going to pick cart --
    # ------------------------
    move_straight(robot, 485)
    robot.stop()
    robot.settings(turn_rate=100, turn_acceleration=100)
    arc(robot, -30, 40)
    # robot.settings(turn_rate=200, turn_acceleration=200)
    move_straight(robot, 500)
    motor_f.run_angle(350, 50)
    move_straight(robot, -80)
    arc(robot, -30, 50)

    # -----------------------
    # -- Put the cart down --
    # -----------------------
    move_straight(robot, 575)
    arc(robot, -30, 38)
    move_straight(robot, 110)
    arc(robot, -30, 40)
    motor_f.run_angle(150, -75)

    # ----------------------------
    # -- Put down the artefacts --
    # ----------------------------
    move_straight(robot, -80)
    arc(robot, -30, -60)
    move_straight(robot, 150)
    motor_e.run_angle(750, -130)

    # ------------------------
    # -- Put down flag no.3 --
    # ------------------------
    move_straight(robot, 80)
    arc(robot, -30, -23)
