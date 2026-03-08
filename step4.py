"""
In this step the robot resolves MISSION 5, 6, 7, 9 and 10
Execution time: 33 sec
"""


def run(
    robot,
    left_motor=None,
    right_motor=None,
    motor_e=None,
    motor_f=None,
):
    # print("step 4")
    robot.reset()
    robot.settings(450, 450)

    # Raise the arms
    motor_e.run_target(350, 100)
    motor_f.run_target(350, -150)

    # ----------------------
    # -- MISSION no.6, 5 and 7 --
    # ----------------------
    robot.straight(740)
    robot.settings(350, 350)
    robot.straight(-55)
    right_motor.run_angle(150, 143)
    robot.straight(-60)
    right_motor.run_angle(150, 176)
    robot.straight(-285)
    motor_f.run_angle(350, 150)
    robot.straight(-160)
    motor_f.run_angle(250, -130)

    # ------------------
    # -- MISSION no.9 --
    # ------------------
    # robot.settings(straight_speed=350, straight_acceleration=150)
    robot.straight(420)
    left_motor.run_angle(170, 155)
    robot.straight(-70)
    # right_motor.run_angle(200, -267)  # ???
    robot.settings(turn_rate=150, turn_acceleration=150)
    robot.arc(30, 50)
    robot.straight(-150)
    robot.arc(32, 40)
    robot.straight(-480)

    # # Turn left
    robot.arc(-50, 65)

    # -------------------
    # -- MISSION no.10 --
    # -------------------
    # motor_e.run_angle(350, -100)
    robot.straight(118)
    motor_e.run_angle(350, -150)

    # Turn left
    robot.settings(
        turn_rate=200,
        turn_acceleration=200,
    )
    robot.straight(-150)
    robot.turn(-52)

    # ------------------
    # -- BASE TO Base --
    # ------------------
    robot.settings(
        straight_speed=1000,
        straight_acceleration=1000,
    )
    robot.straight(-500)

    # reset motors >>> preparation for next step
    motor_e.run_target(450, 0)
    motor_f.run_target(450, 0)
