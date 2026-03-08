"""In this step the robot resolves MISSION 3, 4, 8, 9 and 13"""

from pybricks.tools import wait


def run(
    robot,
    left_motor=None,
    right_motor=None,
    motor_e=None,
    motor_f=None,
):
    # print("step 3")
    robot.reset()

    # Define robot constants
    DISTANCE = 939
    ARM_SPEED_MOTOR1 = 350
    ARM_SPEED_MOTOR1_DEGREES = 170

    # ------------------
    # -- MISSION NO.4 --
    # ------------------
    # Raise the arm of MotorE
    motor_f.run_target(ARM_SPEED_MOTOR1, 150)
    motor_e.run_target(ARM_SPEED_MOTOR1, ARM_SPEED_MOTOR1_DEGREES)
    robot.settings(straight_speed=500, straight_acceleration=200)
    robot.straight(DISTANCE)

    # Turn right
    robot.settings(turn_rate=100, turn_acceleration=100)
    robot.turn(90)

    left_motor.stop()
    right_motor.stop()
    robot.straight(-30)
    left_motor.stop()
    right_motor.stop()
    # Lower the arm of MotorE
    motor_e.run_target(ARM_SPEED_MOTOR1, 32)

    # Move robot fwd to collect the artefact
    robot.settings(turn_rate=100, turn_acceleration=50)
    robot.straight(115)

    # Move rev with the collected artefact
    robot.settings(turn_rate=35, turn_acceleration=35)
    motor_e.run_angle(ARM_SPEED_MOTOR1, 22)
    robot.settings(straight_speed=250, straight_acceleration=100)
    robot.straight(-120)

    # Raise arm slightly to secure the artefact while turning
    motor_e.run_angle(ARM_SPEED_MOTOR1, 90)

    # ---------------------------
    # -- GOING TO MISSION NO.3 --
    # ---------------------------
    # Turn right
    robot.settings(
        straight_speed=350,
        straight_acceleration=350,
        turn_rate=200,
        turn_acceleration=150,
    )
    robot.turn(40)
    robot.straight(235)
    robot.turn(-40)
    robot.straight(295)

    wait(250)

    # ----------------------------
    # -- GOING TO MISSION NO.10 --
    # ----------------------------
    robot.straight(430)
    robot.settings(turn_rate=200, turn_acceleration=200)
    robot.turn(-45)
    robot.arc(83, 80)
    robot.straight(158)

    # ---------------------------
    # -- GOING TO MISSION NO.8 --
    # ---------------------------
    robot.straight(-100)
    robot.turn(-15)
    robot.straight(365)
    motor_f.run_angle(ARM_SPEED_MOTOR1, 420)
    robot.settings(straight_speed=1150)
    motor_f.run_angle(ARM_SPEED_MOTOR1, 2000)

    # ----------------------------
    # -- GOING TO MISSION NO.13 --
    # ----------------------------
    robot.settings(straight_speed=1150, straight_acceleration=1150)
    robot.straight(-130)
    robot.turn(37)
    robot.straight(500)

    # wait(5000)
    # reset motors >>> preparation for next step
    motor_e.run_target(ARM_SPEED_MOTOR1, 0)
    motor_f.run_target(ARM_SPEED_MOTOR1, 0)
