"""In this step the robot must travel to point 2 then to point 1"""

from functions import move_straight, arc


def run(robot, attachment_motor1, attachment_motor2):
    MOTOR_SPEED = 250

    # Re-align motors E and F to their zero-point positions
    current_angle_motor1 = attachment_motor1.angle()
    current_angle_motor2 = attachment_motor2.angle()

    # Return motor E to the zero position via the shortest path
    if current_angle_motor1 > 0:
        attachment_motor1.run_angle(MOTOR_SPEED, -current_angle_motor1)
    else:
        attachment_motor1.run_angle(MOTOR_SPEED, current_angle_motor1)

    # Return motor F to the zero position via the shortest path
    if current_angle_motor2 > 0:
        attachment_motor2.run_angle(MOTOR_SPEED, -current_angle_motor2)
    else:
        attachment_motor2.run_angle(MOTOR_SPEED, current_angle_motor2)

    # Raise the arm of MotorE by 150 degrees
    attachment_motor1.run_angle(MOTOR_SPEED, 150)

    # From the base move fwd 64,5 cm
    move_straight(robot, 645)

    # Then move left 35 degrees
    arc(robot, -100, 35)

    # The move fwd 17 cm
    move_straight(robot, 170)

    # Raise MotorF by 100 degrees
    attachment_motor2.run_angle(MOTOR_SPEED, 100)

    # Move backwards 20 cm
    move_straight(robot, -200)

    # #
    # arc(robot, 100, 35)
