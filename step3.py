"""In this step the robot resolves MISSION 3, 4, 8, 9 and 13"""

from functions import move_straight, turn, arc
from pybricks.parameters import Stop


def run(
    robot,
    left_motor=None,
    right_motor=None,
    motor_e=None,
    motor_f=None,
):
    # Define robot constants
    DISTANCE = 939
    ARM_SPEED_MOTOR1 = 350
    ARM_SPEED_MOTOR1_DEGREES = 170

    # Reset the MotorE at position 0 >>> this can be add at the final step2
    motor_e.run_target(ARM_SPEED_MOTOR1, 0, wait=False)
    motor_f.run_target(ARM_SPEED_MOTOR1, 0, wait=False)

    if motor_e.angle() < 10 or motor_e.angle() > -10:
        motor_e.run_angle(ARM_SPEED_MOTOR1, -motor_e.angle())
        motor_e.run_target(ARM_SPEED_MOTOR1, 0)

    # ------------------
    # -- MISSION NO.4 --
    # ------------------
    # Raise the arm of MotorE
    robot.settings(straight_speed=500, straight_acceleration=200)
    motor_e.run_angle(ARM_SPEED_MOTOR1, ARM_SPEED_MOTOR1_DEGREES, wait=False)
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
    motor_e.run_angle(ARM_SPEED_MOTOR1, -136)

    # Move robot fwd to collect the artefact
    move_straight(robot, 115)

    # Move rev with the collected artefact
    robot.settings(turn_rate=35, turn_acceleration=35)
    motor_e.run_angle(ARM_SPEED_MOTOR1, 20)
    robot.settings(straight_speed=250, straight_acceleration=100)
    move_straight(robot, -120)

    # Raise arm slightly to secure the artefact while turning
    motor_e.run_angle(ARM_SPEED_MOTOR1, 90, wait=False)

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
    motor_f.run_angle(ARM_SPEED_MOTOR1, 400)
    move_straight(robot, 350)
    robot.settings(straight_speed=1150)
    motor_f.run_angle(ARM_SPEED_MOTOR1, 3000)

    # ----------------------------
    # -- GOING TO MISSION NO.13 --
    # ----------------------------
