"""
In this step the robot resolves MISSION 5, 6, 7, 9 and 10
Execution time: 33 sec
"""

from functions import move_straight, turn, arc


def run(
    robot,
    left_motor=None,
    right_motor=None,
    motor_e=None,
    motor_f=None,
):
    robot.settings(450, 450)
    motor_e.run_target(250, 0)
    motor_f.run_target(250, 0)

    # Reset motors to 0 angle if arms aren't in the original position
    if motor_e.angle() < 10 or motor_e.angle() > -10:
        motor_e.run_angle(350, -motor_e.angle())
        motor_e.run_target(350, 0)
    if motor_f.angle() < 10 or motor_f.angle() > -10:
        motor_f.run_angle(350, -motor_f.angle())
        motor_f.run_target(350, 0)

    # Raise the arms
    motor_e.run_angle(350, -175)
    motor_f.run_angle(350, -150)

    # ----------------------
    # -- MISSION no.6, 5 and 7 --
    # ----------------------
    move_straight(robot, 735)
    robot.settings(350, 350)
    move_straight(robot, -55)
    right_motor.run_angle(150, 143)
    move_straight(robot, -60)
    right_motor.run_angle(150, 174)
    move_straight(robot, -285)
    motor_f.run_angle(350, 150)
    move_straight(robot, -160)
    motor_f.run_angle(250, -130)

    # ------------------
    # -- MISSION no.9 --
    # ------------------
    # robot.settings(straight_speed=350, straight_acceleration=150)
    move_straight(robot, 420)
    left_motor.run_angle(170, 155)
    move_straight(robot, -75)
    # right_motor.run_angle(200, -267)  # ???
    robot.settings(turn_rate=150, turn_acceleration=150)
    arc(robot, 30, 50)
    move_straight(robot, -105)
    arc(robot, 32, 40)
    move_straight(robot, -520)

    # # Turn left
    arc(robot, -50, 65)

    # -------------------
    # -- MISSION no.10 --
    # -------------------
    # motor_e.run_angle(350, -100)
    move_straight(robot, 108)
    motor_e.run_angle(350, 150)

    # Turn left
    robot.settings(
        turn_rate=200,
        turn_acceleration=200,
    )
    move_straight(robot, -150)
    turn(robot, -52)

    # ------------------
    # -- BASE TO Base --
    # ------------------
    robot.settings(
        straight_speed=1000,
        straight_acceleration=1000,
    )
    move_straight(robot, -500)


"""
    robot.use_gyro(False)
    right_motor.run_angle(150, 143)
    robot.reset() 
    robot.use_gyro(True)
"""
