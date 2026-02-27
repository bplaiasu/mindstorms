from pybricks.parameters import Stop


def move_straight(robot, distance):
    """
    Moves the robot in a straight line for a specified distance.
    Args:
        robot (DriveBase): The initialized DriveBase object.
        distance (int): Distance to travel in millimeters
                        (positive for forward, negative for backward).
    """
    # Use the DriveBase straight method to move the robot
    robot.straight(distance, Stop.HOLD, wait=True)


def turn(robot, angle):
    """
    Rotates the robot in place by a specific angle.
    Args:
        robot (DriveBase): The initialized DriveBase object.
        angle (int): Degrees to turn
                    (positive for clockwise, negative for counter-clockwise).
    """
    # Rotate the robot on its center axis
    robot.turn(angle)


def arc(robot, radius, angle):
    """
    Moves the robot along a curved path (an arc).
    Args:
        robot (DriveBase): The initialized DriveBase object.
        radius (int): The radius of the circle the robot follows in millimeters
        angle (int): How many degrees of the circle to travel
                    (e.g., 90 for a quarter turn).
    """
    # Drive along a curve defined by the radius and degrees of rotation
    robot.arc(radius, angle)
