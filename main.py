from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# import steps
import step1
import step2

# Initialize hub
hub = InventorHub()

# Adjust robot dimensions
wheel_diameter = 68.7  # mm
axle_track = 103  # mm


# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

# Initialize left and right arm motors
attachment_motor1 = Motor(Port.E, Direction.COUNTERCLOCKWISE)
attachment_motor2 = Motor(Port.F)

# Configure the movement controller for precise distance and rotation tracking
robot = DriveBase(
    left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=axle_track
)

# Set movement speed and enable gyro for heading correction
robot.settings(straight_speed=350, straight_acceleration=350)
robot.use_gyro(True)

# # Run step1 file
# step1.run(robot, attachment_motor1, attachment_motor2)

# Run step2 file
step2.run(robot, attachment_motor1, attachment_motor2)

# while True:
#     buttons = hub.buttons.pressed()

#     if Button.RIGHT in buttons:
#         wait(300)
#         step2.run(robot, attachment_motor1, attachment_motor2)
#         break

# Stop the robot after completing the steps
robot.stop()
