from pybricks.parameters import Stop


def move_straight(robot, distance, stop_type=Stop.HOLD, wait=True):
    """
    Moves the robot in a straight line for a specified distance.
    Args:
        robot (DriveBase): The initialized DriveBase object.
        distance (int): Distance to travel in millimeters
                        (positive for forward, negative for backward).
    """
    # Use the DriveBase straight method to move the robot
    robot.straight(distance, then=stop_type, wait=wait)


def turn(robot, angle, stop_type=Stop.HOLD, wait=True):
    """
    Rotates the robot in place by a specific angle.
    Args:
        robot (DriveBase): The initialized DriveBase object.
        angle (int): Degrees to turn
                    (positive for clockwise, negative for counter-clockwise).
    """
    # Rotate the robot on its center axis
    robot.turn(angle, then=stop_type, wait=wait)


def arc(robot, radius, angle, stop_type=Stop.HOLD, wait=True):
    """
    Moves the robot along a curved path (an arc).
    Args:
        robot (DriveBase): The initialized DriveBase object.
        radius (int): The radius of the circle the robot follows in millimeters
        angle (int): How many degrees of the circle to travel
                    (e.g., 90 for a quarter turn).
    """
    # Drive along a curve defined by the radius and degrees of rotation
    robot.curve(radius, angle, then=stop_type, wait=wait)
