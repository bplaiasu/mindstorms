"""In this step the robot resolves MISSION 3, 4, 8, 9 and 13"""

from functions import move_straight, turn, arc
from pybricks.tools import wait


def run(robot, left_motor, right_motor, attachment_motor1, attachment_motor2):
    # Define robot constants
    DISTANCE = 939
    ARM_SPEED_MOTOR1 = 350
    ARM_SPEED_MOTOR1_DEGREES = 170

    # Reset the MotorE at position 0 >>> this can be add at the final step2
    attachment_motor1.run_target(ARM_SPEED_MOTOR1, 0)
    attachment_motor2.run_target(ARM_SPEED_MOTOR1, 0)

    if attachment_motor1.angle() < 10 or attachment_motor1.angle() > -10:
        attachment_motor1.run_angle(ARM_SPEED_MOTOR1, -attachment_motor1.angle())
        attachment_motor1.run_target(ARM_SPEED_MOTOR1, 0)

    # ---------------------------
    # -- GOING TO MISSION NO.4 --
    # ---------------------------
    # Raise the arm of MotorE
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, ARM_SPEED_MOTOR1_DEGREES)

    robot.settings(straight_speed=500, straight_acceleration=200)

    # Move robot fwd
    move_straight(robot, DISTANCE)

    # Turn right
    robot.settings(turn_rate=100, turn_acceleration=100)
    turn(robot, 89)

    left_motor.stop()
    right_motor.stop()
    move_straight(robot, -30)
    left_motor.stop()
    right_motor.stop()
    # Lower the arm of MotorE
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, -136)

    # Move robot fwd to collect the artefact
    move_straight(robot, 115)

    # Move rev with the collected artefact
    robot.settings(turn_rate=35, turn_acceleration=35)
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, 20)
    robot.settings(straight_speed=250, straight_acceleration=100)
    move_straight(robot, -120)

    # Raise the arm of MotorE
    attachment_motor1.run_angle(ARM_SPEED_MOTOR1, 90)

    # ---------------------------
    # -- GOING TO MISSION NO.3 --
    # ---------------------------
    # Turn right
    robot.settings(
        straight_speed=350,
        straight_acceleration=350,
        turn_rate=200,
        turn_acceleration=200,
    )
    turn(robot, 40)
    move_straight(robot, 230)
    turn(robot, -40)
    move_straight(robot, 263)

    # ----------------------------
    # -- GOING TO MISSION NO.10 --
    # ----------------------------
    move_straight(robot, 450)
    robot.settings(turn_rate=200, turn_acceleration=200)
    turn(robot, -45)
    arc(robot, 100, 83)
    move_straight(robot, 130)

    # ---------------------------
    # -- GOING TO MISSION NO.8 --
    # ---------------------------
    move_straight(robot, -100)
    turn(robot, -25)
    attachment_motor2.run_angle(ARM_SPEED_MOTOR1, 400)
    move_straight(robot, 350)
    robot.settings(straight_speed=1150)
    attachment_motor2.run_angle(ARM_SPEED_MOTOR1, 3000)

    # ----------------------------
    # -- GOING TO MISSION NO.13 --
    # ----------------------------
