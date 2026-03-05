"""
In this step the robot resolves MISSION 1 and 2 by
traveling first to mission  2 and then to mission 1
Execution time: 16 sec
"""

from functions import move_straight, arc
from pybricks.parameters import Stop


def run(
    robot,
    left_motor=None,
    right_motor=None,
    motor_e=None,
    motor_f=None,
):
    MOTOR_SPEED = 250
    DISTANCE_TO_MISSION_2 = 645  # mm
    DISTANCE_MISSION2_OBJECT = 160  # mm
    ATCH_MOTOR2_ARM_DEGREES = 100  # degrees
    DISTANCE_TO_MISSION1 = 65  # mm
    DISTANCE_TO_BASE = 500
    ATCH_MOTOR1_ARM_DEGREES_MISSION1 = 400  # degrees
    LIFT_DISTANCE_REV = 220
    LIFT_DISTANCE_FWD = 100

    # Reset arms to absolute zero
    motor_e.run_target(MOTOR_SPEED, 0, wait=False)
    motor_f.run_target(MOTOR_SPEED, 0, wait=True)

    if motor_f.angle() < 10 or motor_f.angle() > -10:
        motor_f.run_angle(MOTOR_SPEED, -motor_f.angle())
        motor_f.run_target(MOTOR_SPEED, 0)

    # Going to Mission No.2
    robot.settings(straight_speed=800, straight_acceleration=400)

    # Start lifting motor F while moving
    motor_f.run_angle(
        MOTOR_SPEED,
        ATCH_MOTOR2_ARM_DEGREES,
        wait=False,
    )

    # Drive to Mission No.2
    move_straight(robot, DISTANCE_TO_MISSION_2)
    arc(robot, -100, 35)
    move_straight(robot, DISTANCE_MISSION2_OBJECT)

    # Transition to Mission No.1
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
    motor_e.run_angle(MOTOR_SPEED, -ATCH_MOTOR1_ARM_DEGREES_MISSION1)
    motor_e.run_angle(MOTOR_SPEED, ATCH_MOTOR1_ARM_DEGREES_MISSION1)

    # -- Back to Base
    robot.settings(1150, 1150)
    move_straight(robot, -DISTANCE_TO_BASE, then=Stop.COAST)

    # Reset the MotorE at position 0 >>> this can be add at the final step2
    motor_e.run_target(MOTOR_SPEED, 0)
    motor_f.run_target(MOTOR_SPEED, 0)
