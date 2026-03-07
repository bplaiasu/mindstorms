"""
In this step the robot resolves MISSION 1 and 2 by
traveling first to mission  2 and then to mission 1
Execution time: 16 sec
"""

from pybricks.tools import wait


def run(
    robot,
    left_motor=None,
    right_motor=None,
    motor_e=None,
    motor_f=None,
):
    MOTOR_SPEED = 250
    DISTANCE_TO_MISSION_2 = 645  # mm
    DISTANCE_MISSION2_OBJECT = 165  # mm
    ATCH_MOTOR2_ARM_DEGREES = 100  # degrees
    DISTANCE_TO_MISSION1 = 65  # mm
    DISTANCE_TO_BASE = 500
    ATCH_MOTOR1_ARM_DEGREES_MISSION1 = 400  # degrees
    LIFT_DISTANCE_REV = 220
    LIFT_DISTANCE_FWD = 100

    # # Reset arms to absolute zero
    # motor_e.run_target(MOTOR_SPEED, 0)
    # motor_f.run_target(MOTOR_SPEED, 0)

    # Going to Mission No.2
    robot.settings(straight_speed=800, straight_acceleration=400)

    # Drive to Mission No.2
    robot.straight(DISTANCE_TO_MISSION_2)
    robot.arc(-100, 37)
    robot.straight(DISTANCE_MISSION2_OBJECT)
    motor_f.run_target(MOTOR_SPEED, ATCH_MOTOR2_ARM_DEGREES)

    # Transition to Mission No.1
    robot.settings(turn_rate=300, turn_acceleration=300)
    robot.arc(-50, -70)

    # Move backwards
    robot.straight(-DISTANCE_TO_MISSION1)
    robot.arc(50, -37)
    robot.straight(-LIFT_DISTANCE_REV)
    robot.straight(LIFT_DISTANCE_FWD)

    # ATTENTION: on training possible to adjust the wait
    wait(250)

    # The lift movement
    motor_e.run_angle(MOTOR_SPEED, -ATCH_MOTOR1_ARM_DEGREES_MISSION1)
    motor_e.run_angle(MOTOR_SPEED, ATCH_MOTOR1_ARM_DEGREES_MISSION1)

    # -- Back to Base
    robot.settings(1150, 1150)
    robot.straight(-DISTANCE_TO_BASE)

    # Reset the MotorE at position 0 >>> preparation for next step
    motor_e.run_target(MOTOR_SPEED, 0)
    motor_f.run_target(MOTOR_SPEED, 0)
