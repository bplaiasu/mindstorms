from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

import step1
import step2
import step3
import step4
import step5

# Initialize hub
hub = InventorHub()

# Create a list of all steps modules
program_list = [step1, step2, step3, step4]
current_index = 0

# Adjust robot dimensions
wheel_diameter = 68.7  # mm
axle_track = 103  # mm

# Initialize both motors.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)

# Initialize left and right arm motors
motor_e = Motor(Port.E, Direction.COUNTERCLOCKWISE)
motor_f = Motor(Port.F)

# Configure the movement controller
robot = DriveBase(
    left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=axle_track
)

# Set movement speed and enable gyro for heading correction
robot.settings(straight_speed=350, straight_acceleration=350)
robot.use_gyro(True)


while True:
    # Wait for a button press
    pressed_buttons = hub.buttons.pressed()

    # If Right Button is pressed, run the current program
    if Button.RIGHT in pressed_buttons:
        # Check if we just finished the very last step
        if current_index >= len(program_list):
            break

        # Check if index is valid
        if current_index < len(program_list):
            # Display the current program number on the hub
            hub.display.number(current_index + 1)
            hub.speaker.beep()

            # Execute the missions
            program_list[current_index].run(
                robot, left_motor, right_motor, motor_e, motor_f
            )

            # This "releases" the motors so you can move the robot by hand
            # back to the starting area for the next mission!
            robot.stop()

            # After the program finishes, move to the next index
            current_index += 1

            # Wait until the button is released so it doesn't double-trigger
            while Button.RIGHT in hub.buttons.pressed():
                wait(10)
    wait(50)

# Finalize the execution
hub.display.text("BYE")
hub.speaker.beep(frequency=500, duration=500)
print("All steps completed. Goodbye!")
