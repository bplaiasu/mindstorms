"""
In this step the robot resolves MISSION 1 and 2 by
traveling first to mission  2 and then to mission 1
"""

from functions import move_straight, arc


def run(robot, attachment_motor1, attachment_motor2):
    MOTOR_SPEED = 250
    ATCH_MOTOR1_ARM_DEGREES = 140  # degrees
    DISTANCE_TO_MISSION_2 = 645  # mm
    DISTANCE_MISSION2_OBJECT = 160  # mm
    ATCH_MOTOR2_ARM_DEGREES = 100  # degrees
    DISTANCE_TO_MISSION1 = 60  # mm
    DISTANCE_MISSION1_OBJECT = 120  # mm
    DISTANCE_TO_BASE = 600
    ATCH_MOTOR1_ARM_DEGREES_MISSION1 = 85  # degrees

    # Reset the MotorE at position 0 >>> this can be add at the final step2
    attachment_motor1.run_target(MOTOR_SPEED, 0)
    attachment_motor2.run_target(MOTOR_SPEED, 0)

    # Raise the arm of MotorE by 150 degrees
    attachment_motor1.run_angle(MOTOR_SPEED, ATCH_MOTOR1_ARM_DEGREES)

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
    # Move backwards 20 cm
    move_straight(robot, -DISTANCE_TO_MISSION1)

    arc(robot, -100, -30)
    move_straight(robot, -DISTANCE_MISSION1_OBJECT)

    attachment_motor1.run_angle(MOTOR_SPEED, -ATCH_MOTOR1_ARM_DEGREES_MISSION1)
    # Raise the arm of MotorE by 150 degrees
    attachment_motor1.run_angle(MOTOR_SPEED, ATCH_MOTOR1_ARM_DEGREES_MISSION1)

    # ----------------------
    # -- BACK TO THE BASE --
    # ----------------------
    move_straight(robot, -DISTANCE_TO_BASE)

    # Stop the robot after completing the steps
    robot.stop()
