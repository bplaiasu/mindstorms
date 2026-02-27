"""In this step the robot resolves MISSION 3, 4, 8, 9 and 13"""

from functions import move_straight, turn
from pybricks.tools import wait


def run(robot, attachment_motor1, attachment_motor2):
    # Define robot constants
    DISTANCE = 939
    ARM_SPEED_MOTOR1 = 350
    ARM_SPEED_MOTOR1_DEGREES = 200

    robot.settings(
        straight_speed=350,
        straight_acceleration=350,
        turn_rate=150,
        turn_acceleration=150,
    )

    # Reset the MotorE at position 0 >>> this can be add at the final step2
    attachment_motor1.run_target(ARM_SPEED_MOTOR1, 0)

    # Raise the arm of MotorE
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, ARM_SPEED_MOTOR1_DEGREES)

    # Move robot fwd
    move_straight(robot, DISTANCE)

    # Turn right
    turn(robot, 89)

    # Move robot rev
    move_straight(robot, -30)

    # Lower the arm of MotorE
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, -167)

    # Move robot fwd
    move_straight(robot, 96)

    # Raise the arm of MotorE
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, 19)

    move_straight(robot, -100)

    # Raise the arm of MotorE
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, 120)

    # Turn right
    turn(robot, 40)
    move_straight(robot, 222)
    turn(robot, -40)
    move_straight(robot, 232)
    move_straight(robot, -140)
    turn(robot, 70)

    # Reset the MotorE at position 0 >>> this can be add at the final step2
    attachment_motor1.run_target(ARM_SPEED_MOTOR1, 0)
    move_straight(robot, 48)

    # Raise the arm of MotorE
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, 60)
    turn(robot, -35)

    move_straight(robot, -50)
    turn(robot, 55)

    # Reset the MotorE at position 0 >>> this can be add at the final step2
    attachment_motor1.run_target(ARM_SPEED_MOTOR1, 0)

    move_straight(robot, -30)
    turn(robot, -90)
