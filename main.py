from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize hub
hub = InventorHub()

# Import individual programs as functions
import step1, step2, step3, step4

# Create a list of all steps modules
program_list = [step2, step3, step4]
current_index = 0

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

# Run step1 file
step4.run(robot, left_motor, right_motor, attachment_motor1, attachment_motor2)

# Display the current step number
hub.display.number(1)


# while True:
#     # Wait for a button press
#     pressed_buttons = hub.buttons.pressed()

#     # If Right Button is pressed, run the current program
#     if Button.RIGHT in pressed_buttons:
#         # Display the current program number on the hub
#         hub.display.number(current_index + 2)

#         hub.speaker.beep()

#         # Execute the run function from the current module
#         program_list[current_index].run(
#             robot,
#             left_motor,
#             right_motor,
#             attachment_motor1,
#             attachment_motor2
#         )

#         # This "releases" the motors so you can move the robot by hand
#         # back to the starting area for the next mission!
#         robot.stop()

#         # After the program finishes, move to the next index
#         # current_index = (current_index + 1) % len(program_list)
#         current_index += 1

#         # Wait until the button is released so it doesn't double-trigger
#         while Button.RIGHT in hub.buttons.pressed():
#             wait(10)

#         # hub.speaker.beep(frequency=1000, duration=100) # Finish beep
#         # Check if we just finished the very last step
#         if current_index >= len(program_list):
#             break # Exit the while loop immediately

#     wait(50)

# # 6. Final execution after the loop finishes (after step 5)
# hub.display.text("BYE")
# hub.speaker.beep(frequency=500, duration=500)
# print("All steps completed. Goodbye!")

# # Stop the robot after completing the steps
# robot.stop()
