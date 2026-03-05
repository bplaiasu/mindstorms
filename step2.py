"""
In this step the robot resolves MISSION 11 and 12
Execution time: 17 sec
"""

from functions import move_straight
from pybricks.parameters import Stop


def run(
    robot,
    left_motor=None,
    right_motor=None,
    motor_e=None,
    motor_f=None,
):
    # Telescope distance = 1,25 cm

    # Define robot constants
    DISTANCE = 587
    ARM_SPEED_MOTOR1 = 1000
    ARM_SPEED_MOTOR2 = 3000
    ARM_SPEED_MOTOR1_DEGREES = 2200
    ARM_SPEED_MOTOR2_DEGREES2 = 3700
    ARM_SPEED_MOTOR2_DEGREES1 = 4000

    robot.settings(350, 350, 1300, 1300)

    # # Raise the arm coresponding to MotorF
    # motor_f.run_angle(ARM_SPEED_MOTOR2, -ARM_SPEED_MOTOR2_DEGREES1)

    # Move robot fwd
    move_straight(robot, DISTANCE)

    # Lower the arm of MotorF
    motor_f.run_angle(
        ARM_SPEED_MOTOR2,
        ARM_SPEED_MOTOR2_DEGREES1,
        # then=Stop.HOLD,   # improvements ????!!
    )

    # Start the wheels of MotorE
    motor_e.run_angle(ARM_SPEED_MOTOR1, -ARM_SPEED_MOTOR1_DEGREES)

    # Raise the arm of MotorF
    motor_f.run_angle(ARM_SPEED_MOTOR2, -ARM_SPEED_MOTOR2_DEGREES2)

    # Back to the BASE
    move_straight(robot, -DISTANCE)
