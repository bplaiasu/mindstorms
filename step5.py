"""
In this step the robot resolves the MISSIONs:
- apucarea cartului
- place flag no.2
- mission 13
- mission 14
- place flag no.3
Execution time: 38 sec
"""


def run(
    robot,
    left_motor=None,
    right_motor=None,
    motor_e=None,
    motor_f=None,
):
    # print("step 5")
    robot.reset()

    # start from the base
    robot.settings(
        straight_acceleration=200,
        turn_rate=150,
        turn_acceleration=50,
    )
    motor_f.run_target(350, 68)
    robot.straight(500)

    # go and take cart
    robot.turn(38)
    motor_f.run_target(200, 150)
    robot.straight(320)

    # position the flag
    robot.straight(207)
    robot.straight(-120)
    robot.settings(
        turn_rate=80,
        turn_acceleration=100,
    )
    robot.arc(-30, 52)
    robot.settings(
        straight_speed=400,
        straight_acceleration=200,
        turn_rate=200,
        turn_acceleration=200,
    )

    # go to mission no.13
    robot.straight(330)
    robot.settings(
        turn_rate=150,
        turn_acceleration=50,
    )
    robot.arc(-30, 42)
    robot.straight(195)

    # put the cart down
    robot.settings(straight_speed=100, straight_acceleration=50)
    motor_f.run_target(200, 0)

    robot.settings(straight_speed=1000, straight_acceleration=1000)
    robot.straight(-40)

    # # whale lifting
    motor_f.run_target(100, 65)
    robot.settings(
        straight_speed=200,
        straight_acceleration=100,
        # turn_rate=150,
    )
    robot.straight(-90)
    motor_f.run_angle(100, 80)

    # place the artefacts in the arena
    robot.straight(-50)
    robot.arc(-30, -39)
    robot.straight(430)
    motor_e.run_angle(100, -150)

    # place the final flag and finalize the campaign
    robot.settings(straight_acceleration=(1000, 200))
    robot.straight(140)
    robot.turn(20)

    # # reset motors
    # motor_e.run_target(250, 0)
    # motor_f.run_target(250, 0)
