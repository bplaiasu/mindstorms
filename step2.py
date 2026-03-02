"""
In this step the robot resolves MISSION 11 and 12
Execution time: 17 sec
"""

from functions import move_straight


def run(robot, left_motor, right_motor, attachment_motor1, attachment_motor2):
    # Telescope distance = 1,25 cm

    # Define robot constants
    DISTANCE = 585
    ARM_SPEED_MOTOR1 = 1000
    ARM_SPEED_MOTOR2 = 3000
    ARM_SPEED_MOTOR1_DEGREES = 2200
    ARM_SPEED_MOTOR2_DEGREES2 = 3700
    ARM_SPEED_MOTOR2_DEGREES1 = 4000

    robot.settings(350, 350, 1000, 1000)

    # # Raise the arm coresponding to MotorF
    # attachment_motor2.run_angle(ARM_SPEED_MOTOR2, -ARM_SPEED_MOTOR2_DEGREES1)

    # Move robot fwd
    move_straight(robot, DISTANCE)

    # Lower the arm of MotorF
    attachment_motor2.run_angle(ARM_SPEED_MOTOR2, ARM_SPEED_MOTOR2_DEGREES1)

    # Start the wheels of MotorE
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, -ARM_SPEED_MOTOR1_DEGREES)

    # Raise the arm of MotorF
    attachment_motor2.run_angle(ARM_SPEED_MOTOR2, -ARM_SPEED_MOTOR2_DEGREES2)

    # Back to the BASE
    move_straight(robot, -DISTANCE)
