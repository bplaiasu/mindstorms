"""
In this step the robot resolves MISSION 1 and 2 by
traveling first to mission  2 and then to mission 1
Execution time: 16 sec
"""

from functions import move_straight, arc
from pybricks.tools import wait


def run(robot, left_motor, right_motor, attachment_motor1, attachment_motor2):
    MOTOR_SPEED = 250
    ATCH_MOTOR1_ARM_DEGREES = 140  # degrees
    DISTANCE_TO_MISSION_2 = 645  # mm
    DISTANCE_MISSION2_OBJECT = 160  # mm
    ATCH_MOTOR2_ARM_DEGREES = 100  # degrees
    DISTANCE_TO_MISSION1 = 65  # mm
    DISTANCE_MISSION1_OBJECT = 120  # mm
    DISTANCE_TO_BASE = 500
    ATCH_MOTOR1_ARM_DEGREES_MISSION1 = 400  # degrees
    LIFT_DISTANCE_REV = 220
    LIFT_DISTANCE_FWD = 100

    # Reset the MotorE at position 0 >>> this can be add at the final step2
    attachment_motor1.run_target(MOTOR_SPEED, 0)
    attachment_motor2.run_target(MOTOR_SPEED, 0)
    if attachment_motor2.angle() < 10 or attachment_motor2.angle() > -10:
        attachment_motor2.run_angle(MOTOR_SPEED, -attachment_motor2.angle())
        attachment_motor2.run_target(MOTOR_SPEED, 0)

    robot.settings(800, 400)

    # ---------------------------
    # -- GOING TO MISSION NO.2 --
    # ---------------------------
    # From the base move fwd
    move_straight(robot, DISTANCE_TO_MISSION_2)

    # Then move left 35 degrees
    arc(robot, -100, 35)

    # Move fwd
    move_straight(robot, DISTANCE_MISSION2_OBJECT)

    # Raise MotorF by 100 degrees
    attachment_motor2.run_angle(MOTOR_SPEED, ATCH_MOTOR2_ARM_DEGREES)

    # ---------------------------
    # -- GOING TO MISSION NO.1 --
    # ---------------------------
    robot.settings(turn_rate=300, turn_acceleration=300)
    arc(robot, -50, -70)

    # Move backwards
    move_straight(robot, -DISTANCE_TO_MISSION1)

    arc(robot, 50, -37)

    move_straight(robot, -LIFT_DISTANCE_REV)
    move_straight(robot, LIFT_DISTANCE_FWD)

    # # ATTENTION: on training possible to adjust the wait
    # wait(500)

    # The lift movement
    attachment_motor1.run_angle(MOTOR_SPEED, -ATCH_MOTOR1_ARM_DEGREES_MISSION1)
    attachment_motor1.run_angle(MOTOR_SPEED, ATCH_MOTOR1_ARM_DEGREES_MISSION1)

    # ----------------------
    # -- BACK TO THE BASE --
    # ----------------------
    robot.settings(1150, 1150)
    move_straight(robot, -DISTANCE_TO_BASE)

    # Reset the MotorE at position 0 >>> this can be add at the final step2
    attachment_motor1.run_target(MOTOR_SPEED, 0)
    attachment_motor2.run_target(MOTOR_SPEED, 0)
