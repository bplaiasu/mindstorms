# 🤖 LEGO Inventor Robot - Pybricks Project

A modular control system for a LEGO Inventor Hub robot using the `Pybricks` library. This project uses a differential drivebase and dual attachment motors to navigate points and interact with objects.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| **`main.py`** | The entry point. Initializes hardware (Hub, Motors, DriveBase) and runs the mission sequence. |
| **`functions.py`** | A library of simplified movement wrappers (`move_straight`, `turn`, `arc`) used by all steps. |
| **`step1.py`** | Mission 1 logic: objecttives 1 & 2 |
| **`step2.py`** | Mission 2 logic: |

---

## ⚙️ Hardware Configuration

### Drivetrain

- **Left Motor:** Port A (Counter-Clockwise)
- **Right Motor:** Port B (Clockwise)
- **Wheel Diameter:** 68.7 mm
- **Axle Track:** 103 mm (Distance between wheels)

### Attachment Motors (Robot Arms)

- **Motor 1 (Left Arm):** Port E (Counter-Clockwise)
- **Motor 2 (Right Arm):** Port F (Clockwise)

---

## 🚀 How to Use

1. **Preparation:** Ensure your Hub is running the [Pybricks Firmware](https://pybricks.com/install/).
2. **Deployment:** Upload all four `.py` files to your Hub.
3. **Execution:** Run `main.py`.
    - The robot will immediately begin with the execution of `Step 1`.
    - The attachment motors (E and F) will automatically re-align to their zero-point positions before moving.

---

## 🛠 Movement API (`functions.py`)

The following helper functions are used to simplify robot navigation:

- **`move_straight(robot, distance)`**: Moves the robot in a straight line.
  - *Distance:* Millimeters (positive = forward).
- **`turn(robot, angle)`**: Rotates the robot in place on its center axis.
  - *Angle:* Degrees (positive = clockwise).
- **`arc(robot, radius, angle)`**: Drives the robot along a curved path.
  - *Radius:* Radius of the circle in mm.
  - *Angle:* Degrees of the circle to travel.

---

## 📊 Technical Settings

The robot is configured for a balance of speed and precision:

- **Top Speed:** 350 mm/s
- **Acceleration:** 350 $mm/s^2$
- **Gyroscope:** Enabled (`True`) for active heading correction and straight-line stability.
