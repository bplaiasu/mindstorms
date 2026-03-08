"""
In this step the robot resolves MISSION 11 and 12
Execution time: 17 sec
"""


def run(
    robot,
    left_motor=None,
    right_motor=None,
    motor_e=None,
    motor_f=None,
):
    # print("step 2")
    robot.reset()

    # Define robot constants
    DISTANCE = 603
    ARM_SPEED_MOTOR1 = 1000
    ARM_SPEED_MOTOR2 = 3000
    ARM_SPEED_MOTOR1_DEGREES = 2200
    ARM_SPEED_MOTOR2_DEGREES2 = 4100
    ARM_SPEED_MOTOR2_DEGREES1 = 4000

    robot.settings(350, 250, 1300, 1300)

    # # Raise the arm coresponding to MotorF
    # motor_f.run_angle(ARM_SPEED_MOTOR2, -ARM_SPEED_MOTOR2_DEGREES1)

    # Move robot fwd
    robot.straight(DISTANCE)

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
    robot.straight(-DISTANCE)

    # reset motors >>> preparation for next step
    motor_e.run_target(ARM_SPEED_MOTOR1, 0)
    motor_f.run_target(ARM_SPEED_MOTOR1, 0)
